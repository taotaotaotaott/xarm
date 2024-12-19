"""
Description: test
"""

#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2019, UFACTORY, Inc.
# All rights reserved.
#
# Author: Vinman <vinman.wen@ufactory.cc> <vinman.cub@gmail.com>

import os
import sys
import time
from configparser import ConfigParser
from xarm.wrapper import XArmAPI

def initialize_arm():
    # 读取配置文件
    sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
    parser = ConfigParser()
    parser.read('./robot.conf')
    try:
        ip = parser.get('xArm', 'ip')
    except:
        ip = input('Please input the xArm ip address[192.168.1.194]:')
        if not ip:
            ip = '192.168.1.222'

    # 初始化机械臂
    arm = XArmAPI(ip)
    arm.motion_enable(enable=True)
    arm.set_mode(0)
    arm.set_state(state=0)
    time.sleep(1)
    arm.move_gohome(speed=8)
    return arm

def grasp_object(arm, x, y, z, width):
    arm.goto_grasp(x, y, z, width)

def main():
    arm = initialize_arm()

    # 输入信息 
    x, y, z = map(float, input("请输入物品顶部中心坐标x, y, z（用逗号分隔）：").split(","))
    width = float(input("请输入物体的宽（单位mm）："))

    grasp_object(arm, x, y, z, width)

if __name__ == "__main__":
    main()
