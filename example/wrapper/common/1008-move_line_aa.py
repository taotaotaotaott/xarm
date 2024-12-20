#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2019, UFACTORY, Inc.
# All rights reserved.
#
# Author: Vinman <vinman.wen@ufactory.cc> <vinman.cub@gmail.com>

"""
Description: Set the pose represented by the axis angle pose
"""

import os
import sys
import time

sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))

from xarm.wrapper import XArmAPI


#######################################################
"""
Just for test example
"""
if len(sys.argv) >= 2:
    ip = sys.argv[1]
else:
    try:
        from configparser import ConfigParser
        parser = ConfigParser()
        parser.read('../robot.conf')
        print(" reading robt conf")
        for section in parser.sections():
            print(f"Section: {section}")
            for option in parser.options(section):
                print(f"  {option} = {parser.get(section, option)}")
        
        ip = parser.get('xArm', 'ip')
        print("reading done")
    except Exception as e:
        print(f"erro reading,{e}")
        ip = input('Please input the xArm ip address:')
        if not ip:
            print('input error, exit')
            sys.exit(1)
########################################################


arm = XArmAPI(ip)
arm.motion_enable(enable=True)
arm.set_mode(0)
arm.set_state(state=0)
time.sleep(1)
# go to "Zero Position"
arm.move_gohome()


arm.set_position(300, 0, 0,180, 0, 0,speed=8) #移动到的位置和姿态

# # test pitch, pitch +50
# ret = arm.set_position_aa(axis_angle_pose=[0,10000, 0, 0,0, 0], speed=20,relative=True,wait=True) #这里是相对运动的情况
# print('set_position_aa, ret={}'.format(ret))
# # arm.move_gohome()


# ===移动到一点之后再相对移动==================


# arm.set_position(300, 0, 300, 180, 0, 0)
# # test pitch, pitch +50
# ret = arm.set_position_aa(axis_angle_pose=[0, 0, 0, 0, 50, 0], speed=20,relative=True, wait=True)
# print('set_position_aa, ret={}'.format(ret))



# test pitch, pitch -50
# ret = arm.set_position_aa(axis_angle_pose=[0, 0, 0, 0, -50, 0], relative=True, wait=True)
# print('set_position_aa, ret={}'.format(ret))

# # test yaw, yaw +80
# ret = arm.set_position_aa(axis_angle_pose=[100, 0, 0, 0, 0, 80], relative=True, wait=True)
# print('set_position_aa, ret={}'.format(ret))

# # test yaw, yaw -80
# ret = arm.set_position_aa(axis_angle_pose=[0, 0, 0, 0, 0, -80], relative=True, wait=True)
# print('set_position_aa, ret={}'.format(ret))


