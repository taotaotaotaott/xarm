'''
Description:
    assume that the target object is placed on a horizontal plane
'''

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


sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))


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


def main():
    arm = initialize_arm()

    
    obj_name = "cup"  
    obj_info = arm.get_object_info(obj_name)  
    object_x_coordinate= obj_info["object_x_coordinate"]
    object_y_coordinate= obj_info["object_y_coordinate"]
    object_z_coordinate= obj_info["object_z_coordinate"]
    object_width= obj_info["object_width"]
    object_height= obj_info["object_height"]
    grasp_axis_unit_vector_x= obj_info["grasp_axis_unit_vector_x"]
    grasp_axis_unit_vector_y= obj_info["grasp_axis_unit_vector_y"]
    grasp_axis_unit_vector_z= obj_info["grasp_axis_unit_vector_z"]


    arm.grasp_object(x=object_x_coordinate,y=object_y_coordinate, z=object_z_coordinate, width=object_width,height=object_height,
                     grasp_axis_unit_vector_x=grasp_axis_unit_vector_x,grasp_axis_unit_vector_y=grasp_axis_unit_vector_y,grasp_axis_unit_vector_z=grasp_axis_unit_vector_z)
    # arm.move_gohome(speed=10)
    

if __name__ == "__main__":
    main()
    