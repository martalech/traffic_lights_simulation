# -*- coding:utf-8 -*-

# 灯光模拟模拟模型
# 1. 行人出现模拟
# 2. 灯光部署模拟
# 3. 灯光强度计算
# 4. 灯光控制
# 5. 总体仿真

from turtle import pos
import numpy as np

# 全局变量
# 道路长度
road_length = 200
# 灯的高度
light_height = 10
# 灯的辐射角
light_theta = 30
# 灯部署距离
deploy_distance = 50
# 灯光最远辐射距离
light_max_distance = 3000
# 行人通过速度m/s
human_velocity = 1
# 行人所需的最小光照强度
min_intensity = 40
# 部署的所有灯数量
deploy_light_num = 0

# 根据time_interval返回当前时段行人出现概率
def getPersonProb(time_interval):
    if time_interval == 18:
        prob = 0.8
        number = 30
    elif time_interval == 19:
        prob = 0.75
        number = 25
    elif time_interval == 20:
        prob = 0.7
        number = 20
    elif time_interval == 21:
        prob = 0.65
        number = 16
    elif time_interval == 22:
        prob = 0.60
        number = 12
    elif time_interval == 23:
        prob = 0.4
        number = 8
    elif time_interval == 24:
        prob = 0.2
        number = 4
    elif time_interval == 25:
        prob = 0.1
        number = 2
    elif time_interval == 26:
        prob = 0.05
        number = 2
    elif time_interval == 27:
        prob = 0.1
        number = 4
    elif time_interval == 28:
        prob = 0.5
        number = 20
    elif time_interval == 29:
        prob = 0.7
        number = 30
    else:
        prob = 0.8
        number = 40
    return prob, number

# 根据部署距离，给出灯坐标及初始状态
# 灯的部署如下
# |-------L------L-------L------L|
def getLightDeploy():
    light_count = int(np.ceil(road_length / deploy_distance))
    print('light deploy count:{}'.format(light_count))
    light_position = []
    light_state = []
    for i in range(light_count):
        light_position.append((i + 1) * deploy_distance)
        light_state.append(0)
    global deploy_light_num
    deploy_light_num = len(light_position)
    return light_position, light_state

# 根据灯的状态返回灯的功耗, kw/h，以及对应的光源强度
def getLightPower(light_state):
    power = 0
    if light_state == 1:
        power = 100
        light_intensity = 30
    elif light_state == 2:
        power = 200
        light_intensity = 40
    elif light_state == 3:
        power = 300
        light_intensity = 50
    else:
        power = 400
        light_intensity = 60
    return power, light_intensity

# 根据行人与灯的夹角计算行人位置处的光强
def getLightIntensityByAngle(angle, light_state):
    r = light_height / np.cos(angle)
    _, light_intensity = getLightPower(light_state)
    pos_intensity = r / light_max_distance * light_intensity
    return pos_intensity

# 根据坐标，计算当前位置处的光强
# 1. position，相对起始点的坐标
# 2. light_state，灯光开关状态，0,1,2,3,4
# 返回 当前光强以及当前所在位置前一个灯的序号
def getLightIntensity(position, light_state):
    pre_id = int(np.floor(position / deploy_distance))
    next_id = int(pre_id + 1)
    angle1 = np.arctan2(position - pre_id * deploy_distance, light_height)
    angle2 = np.arctan2(next_id * deploy_distance - position, light_height)
    pre_intensity = 0
    next_intensity = 0
    if pre_id > 0 and pre_id <= deploy_light_num:
        pre_intensity = getLightIntensityByAngle(angle1, light_state[pre_id - 1])
    if next_id > 0 and next_id <= deploy_light_num:
        next_intensity = getLightIntensityByAngle(angle2, light_state[next_id - 1])
    intensity = pre_intensity + next_intensity
    return intensity, next_id

# 调整灯的等级，并计算是否满足光照需求
# position：行人位置
# light_state：灯光状态
# light_id：要调整的灯光
# level：灯光等级
def adjustLight(position, light_state, light_id, level):
    light_state[light_id] = level;
    intensity, _ = getLightIntensity(position, light_state)
    return intensity > min_intensity

# 灯光控制方法的实现，包括调亮和调暗
# 1. human_position_set：所有人的位置
# 2. light_state：路灯开关状态
def controlLight(human_position_set, light_state):
    for i in range(len(human_position_set)):
        if human_position_set[i] < 0:
            continue
        intensity, next_id = getLightIntensity(human_position_set[i], light_state)
        if intensity < min_intensity:
            satisify = False
            # 优先调整后一个灯光
            if next_id <= deploy_light_num:
                store_light_state = light_state[next_id - 1]
                cur_level = store_light_state
                while light_state[next_id - 1] < 4:
                    cur_level += 1
                    satisify = adjustLight(human_position_set[i], light_state, next_id - 1, cur_level)
                    if satisify:
                        break
            # 如果调整之后仍无法满足，调整前一个灯
            if satisify == False and next_id > 1:
                store_light_state = light_state[next_id - 2]
                cur_level = store_light_state
                while light_state[next_id - 2] < 4:
                    cur_level += 1
                    satisify = adjustLight(human_position_set[i], light_state, next_id - 2, cur_level)
                    if satisify:
                        break
            # 如果仍为满足
            print('Requirment Can not be Satisfied!')
    
    return light_state

# 计算行人当前位置，位置为-1的代表已经小时
def humanSimulate(human_position_set, step):
    for i in range(len(human_position_set)):
        if human_position_set[i] >= 0:
            human_position_set[i] = human_position_set[i] + step * human_velocity
            human_position_set[i] = -1 if human_position_set[i] > 200 else human_position_set[i]
    return human_position_set

# 综合模拟函数, 逐时段模拟
def simulate(time_start, time_stop):
    light_position, light_state = getLightDeploy()
    time_current = time_start
    humans = []
    sim_step = 1
    total_engergy = 0
    # 模拟整个夜间
    while time_current <= time_stop:
        # 每个时段模拟，1hr一个时段
        time_start_sec = 0
        person_prob, count = getPersonProb(time_current)
        print('current interval {}, person prob:{}, person count:{}'.format(time_current, person_prob, count))
        cur_time_humman_count = 0
        while time_start_sec < 3600:
            # 行人出现概率满足，且当前时段行人数量未达到上限
            if np.random.random() < person_prob and cur_time_humman_count < count:
                humans.append(0)
                cur_time_humman_count += 1
                print('current interval {}, human count:{}'.format(time_current, cur_time_humman_count))
            # 模拟人所在位置
            humans = humanSimulate(humans, sim_step)
            # 计算当前灯控制逻辑
            controlLight(humans, light_state)
            # 计算当前控制状态下等的累积功率
            for i in range(len(light_position)):
                power, _ = getLightPower(light_state[i])
                total_engergy =  total_engergy + power * sim_step / 3600
            time_start_sec = time_start_sec + sim_step
        time_current += 1
    return total_engergy

# 计算无控状态下的消耗
def calculate(time_start, time_stop):
    power, _ = getLightPower(4)
    light_position, _ = getLightDeploy()
    total_power = (time_stop - time_start) * len(light_position) *  power
    return total_power

if __name__ == '__main__':
    default_energy = calculate(18, 30)
    print('default energy:{}'.format(default_energy))
    control_engergy = simulate(18, 30)
    print('control energy:{}'.format(control_engergy))
    
