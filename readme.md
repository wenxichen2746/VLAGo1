# Go1 Robot Setup and Control Guide

## 1. Configuring IP Address
To set up the Ethernet connection for Go1, you can use one of the following methods.

### **Method 1: Using ifconfig**
```bash
sudo ifconfig enP8p1s0 down
sudo ifconfig enP8p1s0 192.168.123.162/24
sudo ifconfig enP8p1s0 up
```

### **Method 2: Using ip commands**
```bash
sudo ip addr flush dev enP8p1s0  
sudo ip addr add 192.168.123.162/24 dev enP8p1s0
sudo ip link set enP8p1s0 up
```

## 2. ROS2 Setup
Before running ROS2 commands, activate your ROS2 virtual environment in every new terminal window:
```bash
source ~/ros2_venv/bin/activate
source_ros2
```

## 3. Launching the Go1 Driver
To launch the Go1 driver with an Ethernet connection:
```bash
ros2 launch unitree_ros unitree_driver_launch.py wifi:=false
```

## 4. Running Teleoperation
In a new terminal, run the teleoperation keyboard controller:
```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

## 5. Building the ROS2 Workspace
Before running ROS2 packages, ensure the workspace is built:
```bash
colcon build --symlink-install
```

## 6. Running Demo Code
### **Publish Velocity Commands to Go1**
```bash
ros2 run vlm_api command_publisher
```

### **Running Camera Test Script**
```bash
cd ros2_ws/
python src/vlm_api/vlm_api/test_camera.py
```

