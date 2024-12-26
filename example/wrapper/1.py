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
import numpy as np
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

def grasp_object(arm, x, y, z, width):
    arm.goto_grasp(x, y, z, width)




# 输入信息 
    # x, y, z,roll,pitch,yaw = map(float, input("请输入物品顶部中心坐标x, y, z,row,pitch,yaw（用逗号分隔）：").split(","))
    # width = float(input("请输入物体的宽（单位mm）："))
    
    # arm._set_position_absolute(x,y,z,_check_tcp_limit=True,check=True)
    # arm.set_position(x,y,z,row=180,pitch=0,yaw=0,_check_tcp_limit=True,check=True,wait=5)
    # grasp_object(arm, x, y, z, width)
    # arm.move_gohome(speed=10)

def main():
    arm = initialize_arm()
    #  目前工具就有坐标 xyz 相当于向量  如果传进来三个tool向量，查看哪个相对于基座标系方向没变，那就是绕哪个轴旋转，变了的向量与基坐标系的夹角，即旋转角度
    #  输入以目标的几何中心为 目标空间坐标系的原点的 xyz轴向量，例如长方体，垂直于顶面以顶面为正方向的为z轴；垂直于宽，的方向设置为y轴（向量2） ；垂直于长的方向设置为x轴（向量1）
    #  传进来三条向量  这三条向量坐标 相对于基座标系
    #  分别计算向量1、2、3 与基座标系xyz轴的夹角，角度传给roll、pitch、yaw
    
    # 输入三条向量
    # 计算夹角  calculate_angle_between_vectors(v1, v2, is_radian=False)
    # 赋值


    
# 坐标系初始化
    target_vectors, tool_vectors = arm.get_vectors(use_default_tool_vectors=False)
    
    
    #初始化 工具坐标系当前位置，默认x(1,0,0) y(0,-1,0)z(0,0,-1) 提示用户输入，如果不输入，就按照默认值处理
    tool_vectors = arm.get_tool_vectors()
    print("too_vector is :",tool_vectors)
    # 获取用户输入的目标坐标系向量  
    x, y, z = map(float, input("请输入物品顶部中心坐标x, y, z（用逗号分隔）：").split(",")) #命名改一下，改成target
    target_vectors = arm.get_target_vectors()  #获取了目标坐标系
    print("target_vector is :",target_vectors)

    roll, pitch, yaw = arm.calculate_rotation(tool_vectors, target_vectors) #工具坐标系如何  转换到  目标坐标系

    # arm.set_position(x,y,z,roll,pitch,yaw,wait=3,speed=10)




    #加一个 检测这个转换是否合理
    code=arm.test_path_valid(x=x,y=y,z=z,roll=roll,pitch=pitch,yaw=yaw)
    if code == 0:# 合法则执行
        print("code 等于 0 要执行")
        
        arm.set_position(x,y,z,roll,pitch,yaw,wait=3,speed=10)
        # arm.set_position(x,y,z,roll,pitch,yaw,_check_tcp_limit=True,check=True,wait=5) #wait 等待是否超时

    print(f"工具坐标轴通过 roll:{roll},pitch:{pitch},yaw:{yaw} 旋转到 目标坐标轴")
    # arm.set_position(x,y,z,roll,pitch,yaw,wait=3,speed=10)
    # arm.set_position(0,0,0,roll,pitch,yaw,reltive=True,speed=10) #进行tool的旋转
    
    
    





    # 传进来的xyz row pitch yaw 判断路径是否合法
    # code :-8        out of range           例如 300,300,300,1900000,30,30
    # code : 0        success                例如 300,300,300,180,0,0  
    # code :-6        cartesian pos limit    例如 100000000000,2000000,10000,180,0,0
    

    # grasp_object(arm, x, y, z, width)
    

    # arm.set_only_check_type(3)  # 重置检查类型
    # code = arm.set_position(x,y,z,row=180,pitch=0,yaw=0,_check_tcp_limit=True,check=True,wait=5)  # 移动到点 A
    # print("*******")
    # print(f"code:{code}")
    # c=arm.only_check_result
    # print(c)

    # arm.set_only_check_type(1)  # 开启路径检查，检查自碰撞和超速
    # code = arm.set_position(B)  # 尝试移动到点 B
    # if code != 0:
    #     # 如果返回值不为0，说明路径检查未通过，可以通过 arm.only_check_result 查看具体错误代码
    #     print(arm.only_check_result)
    # arm.set_only_check_type(0)  # 恢复到不做检查的状态


    

if __name__ == "__main__":
    main()
    