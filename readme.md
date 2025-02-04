sudo ifconfig enP8p1s0 down
sudo ifconfig enP8p1s0 192.168.123.162/24
sudo ifconfig enP8p1s0 up

#method 2 to config ip
sudo ip addr flush dev enP8p1s0  
sudo ip addr add 192.168.123.162/24 dev enP8p1s0
sudo ip link set enP8p1s0 up

#run these for every new window opened
source ~/ros2_venv/bin/activate
source_ros2

#set wifi:=false for ethernet connection
ros2 launch unitree_ros unitree_driver_launch.py wifi:=false
#in a new terminal
ros2 run teleop_twist_keyboard teleop_twist_keyboard


colcon build --symlink-install


#demo code for publishing velocity command to go1
ros2 run vlm_api command_publisher

cd ros2_ws/
python src/vlm_api/vlm_api/test_camera.py 


# trouble shooting
## ip adress is not updating use ifconfig
sudo systemctl stop NetworkManager
sudo systemctl start NetworkManager

