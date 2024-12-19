import unittest
from unittest.mock import patch, MagicMock
from xarm.wrapper import XArmAPI
from goto_and_grasp import grasp_object,initialize_arm

class TestXArmAPI(unittest.TestCase):

    @patch('goto_and_grasp.XArmAPI')  # 替换为实际模块名
    def test_initialize_arm(self, MockXArmAPI):
        mock_arm = MockXArmAPI.return_value 
        arm = initialize_arm()
        
        self.assertEqual(arm, mock_arm)
        mock_arm.motion_enable.assert_called_once_with(enable=True)
        mock_arm.set_mode.assert_called_once_with(0)
        mock_arm.set_state.assert_called_once_with(state=0)

    @patch('goto_and_grasp.XArmAPI')
    def test_grasp_object(self, MockXArmAPI):
        mock_arm = MockXArmAPI.return_value 
        x, y, z, width = 100, 200, 300, 50
        grasp_object(mock_arm, x, y, z, width)
        mock_arm.goto_grasp.assert_called_once_with(x, y, z, width)

if __name__ == '__main__':
    unittest.main()
