import unittest
from unittest.mock import patch, MagicMock
from grasp_object import main, initialize_arm

class TestMainFunction(unittest.TestCase):

    @patch('grasp_object.XArmAPI')
    @patch('builtins.input', return_value='192.168.1.222')
    def test_main(self, mock_input, MockXArmAPI):
        mock_arm = MockXArmAPI.return_value
        mock_arm.get_object_info.return_value = {
            "object_x_coordinate": 100,
            "object_y_coordinate": 200,
            "object_z_coordinate": 300,
            "object_width": 50,
            "object_height": 75,
            "grasp_axis_unit_vector_x": 1,
            "grasp_axis_unit_vector_y": 0,
            "grasp_axis_unit_vector_z": 0
        }
    
        main()
        
        mock_arm.grasp_object.assert_called_once_with(
            x=100, y=200, z=300, width=50, height=75,
            grasp_axis_unit_vector_x=1, grasp_axis_unit_vector_y=0, grasp_axis_unit_vector_z=0
        )

    @patch('grasp_object.XArmAPI')
    @patch('builtins.input', return_value='192.168.1.222')
    def test_initialize_arm(self, mock_input, MockXArmAPI):
        
        arm = initialize_arm()
        
        arm.motion_enable.assert_called_once_with(enable=True)

if __name__ == '__main__':
    unittest.main()