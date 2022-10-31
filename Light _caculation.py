# -*- coding:utf-8 -*-

# �ƹ�ģ��ģ��ģ��
# 1. ���˳���ģ��
# 2. �ƹⲿ��ģ��
# 3. �ƹ�ǿ�ȼ���
# 4. �ƹ����
# 5. �������

from turtle import pos
import numpy as np

# ȫ�ֱ���
# ��·����
road_length = 200
# �Ƶĸ߶�
light_height = 10
# �Ƶķ����
light_theta = 30
# �Ʋ������
deploy_distance = 50
# �ƹ���Զ�������
light_max_distance = 3000
# ����ͨ���ٶ�m/s
human_velocity = 1
# �����������С����ǿ��
min_intensity = 40
# ��������е�����
deploy_light_num = 0

# ����time_interval���ص�ǰʱ�����˳��ָ���
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

# ���ݲ�����룬���������꼰��ʼ״̬
# �ƵĲ�������
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

# ���ݵƵ�״̬���صƵĹ���, kw/h���Լ���Ӧ�Ĺ�Դǿ��
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

# ����������ƵļнǼ�������λ�ô��Ĺ�ǿ
def getLightIntensityByAngle(angle, light_state):
    r = light_height / np.cos(angle)
    _, light_intensity = getLightPower(light_state)
    pos_intensity = r / light_max_distance * light_intensity
    return pos_intensity

# �������꣬���㵱ǰλ�ô��Ĺ�ǿ
# 1. position�������ʼ�������
# 2. light_state���ƹ⿪��״̬��0,1,2,3,4
# ���� ��ǰ��ǿ�Լ���ǰ����λ��ǰһ���Ƶ����
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

# �����Ƶĵȼ����������Ƿ������������
# position������λ��
# light_state���ƹ�״̬
# light_id��Ҫ�����ĵƹ�
# level���ƹ�ȼ�
def adjustLight(position, light_state, light_id, level):
    light_state[light_id] = level;
    intensity, _ = getLightIntensity(position, light_state)
    return intensity > min_intensity

# �ƹ���Ʒ�����ʵ�֣����������͵���
# 1. human_position_set�������˵�λ��
# 2. light_state��·�ƿ���״̬
def controlLight(human_position_set, light_state):
    for i in range(len(human_position_set)):
        if human_position_set[i] < 0:
            continue
        intensity, next_id = getLightIntensity(human_position_set[i], light_state)
        if intensity < min_intensity:
            satisify = False
            # ���ȵ�����һ���ƹ�
            if next_id <= deploy_light_num:
                store_light_state = light_state[next_id - 1]
                cur_level = store_light_state
                while light_state[next_id - 1] < 4:
                    cur_level += 1
                    satisify = adjustLight(human_position_set[i], light_state, next_id - 1, cur_level)
                    if satisify:
                        break
            # �������֮�����޷����㣬����ǰһ����
            if satisify == False and next_id > 1:
                store_light_state = light_state[next_id - 2]
                cur_level = store_light_state
                while light_state[next_id - 2] < 4:
                    cur_level += 1
                    satisify = adjustLight(human_position_set[i], light_state, next_id - 2, cur_level)
                    if satisify:
                        break
            # �����Ϊ����
            print('Requirment Can not be Satisfied!')
    
    return light_state

# �������˵�ǰλ�ã�λ��Ϊ-1�Ĵ����Ѿ�Сʱ
def humanSimulate(human_position_set, step):
    for i in range(len(human_position_set)):
        if human_position_set[i] >= 0:
            human_position_set[i] = human_position_set[i] + step * human_velocity
            human_position_set[i] = -1 if human_position_set[i] > 200 else human_position_set[i]
    return human_position_set

# �ۺ�ģ�⺯��, ��ʱ��ģ��
def simulate(time_start, time_stop):
    light_position, light_state = getLightDeploy()
    time_current = time_start
    humans = []
    sim_step = 1
    total_engergy = 0
    # ģ������ҹ��
    while time_current <= time_stop:
        # ÿ��ʱ��ģ�⣬1hrһ��ʱ��
        time_start_sec = 0
        person_prob, count = getPersonProb(time_current)
        print('current interval {}, person prob:{}, person count:{}'.format(time_current, person_prob, count))
        cur_time_humman_count = 0
        while time_start_sec < 3600:
            # ���˳��ָ������㣬�ҵ�ǰʱ����������δ�ﵽ����
            if np.random.random() < person_prob and cur_time_humman_count < count:
                humans.append(0)
                cur_time_humman_count += 1
                print('current interval {}, human count:{}'.format(time_current, cur_time_humman_count))
            # ģ��������λ��
            humans = humanSimulate(humans, sim_step)
            # ���㵱ǰ�ƿ����߼�
            controlLight(humans, light_state)
            # ���㵱ǰ����״̬�µȵ��ۻ�����
            for i in range(len(light_position)):
                power, _ = getLightPower(light_state[i])
                total_engergy =  total_engergy + power * sim_step / 3600
            time_start_sec = time_start_sec + sim_step
        time_current += 1
    return total_engergy

# �����޿�״̬�µ�����
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
    
