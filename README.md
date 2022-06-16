# Heterogeneous-robots-ws
A repository that contains different models of robots and a launch file for spawning multi-robots 

Clone
```
git clone https://github.com/khalidbourr/Heterogeneous-robots-ws.git
```

Insert new models in gazebo:
```
cd Heterogeneous-robots-ws/src/Hetero_robots/src/multi_robot/worlds
sudo cp -r red_flag ~/.gazebo/models
sudo cp -r basic_box ~/.gazebo/models
sudo cp -r walls_evry ~/.gazebo/models
```
Build 
```
cd
cd Heterogeneous-robots-ws/
rosdep install --from-paths src --ignore-src -r -y
catkin_make
```
Launch
```
source devel/setup.bash
roslaunch multi_robot multi_robot.launch
```
