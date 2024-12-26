def get_object_info(object_name:str)->str|dict:
    # 输入信息 
        object_x_coordinate, object_y_coordinate, object_z_coordinate = map(float, input("请输入物品顶部中心坐标x, y, z（用逗号分隔）：").split(","))
        object_width = float(input("请输入物体的宽（单位mm）："))
        object_height = float(input("请输入物体的高（单位mm）:"))
        grasp_axis_unit_vector_x,grasp_axis_unit_vector_y,grasp_axis_unit_vector_z = map(float,input("请输入抓取轴向量的三个分量:").split(","))

        object_info_dict = {
            object_name: {
                "object_x_coordinate": object_x_coordinate,
                "object_y_coordinate": object_y_coordinate,
                "object_z_coordinate": object_z_coordinate,
                "object_width": object_width,
                "object_height": object_height,
                "grasp_axis_unit_vector_x": grasp_axis_unit_vector_x,
                "grasp_axis_unit_vector_y": grasp_axis_unit_vector_y,
                "grasp_axis_unit_vector_z": grasp_axis_unit_vector_z,
                }
        }

        if object_name not in object_info_dict:
            return "Can't obtain the position, orientation, and size information of the object: {}, please check the object_name.".format(object_name)

        obj_info = object_info_dict[object_name]

        return obj_info