
# 1
## 机械臂安装
https://www.cn.ufactory.cc/xarm-download  
下载用户手册，进行安装
实验室机械臂型号为xarm 6
## connect xarm
### network config

<img src="pictures/network_config01.jpg" alt="networkconfig" width="500"/>
<img src="pictures/network_config02.jpg" alt="networkconfig" width="500"/>
<img src="pictures/network_config03.jpg" alt="networkconfig" width="300"/>
<img src="pictures/network_config04.jpg" alt="networkconfig" width="300"/>
<img src="pictures/network_config05.jpg" alt="networkconfig" width="300"/>

ping 192.168.1.222 to check the connection  


#### 访问ufactory studio
ip + :18333  
192.168.1.222:18333  
<img src="pictures/network_config06.jpg" alt="networkconfig" width="600"/>

## installation

```
python setup.py install
```


Before running the example, please modify the IP in robot.conf to corresponding IP you want to control.  
robot ip:192.168.1.222  



## api rewrapper code 
默认物体放置于水平面 进行抓取  
api_test\example\wrapper\target_on_horizon_plane.py  

测试用例  
api_test\example\wrapper\test_xarm.py


