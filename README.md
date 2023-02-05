# Heterogeneous-robots-ws

This repository includes a variety of robot models and a single launch file for launching many robots inside a simulation. The purpose of this repository is to make the process of spawning various robots simpler and more comfortable for the user. This repository allows the user to launch many robots with a single command, speeding simulation setup and decreasing preparation time. Whether you are investigating novel robot models or doing sophisticated simulations, this repository offers a straightforward and effective solution for your requirements.

```
 <include file="$(find gazebo_ros)/launch/empty_world.launch">
    <arg name="world_name" value="$(find multi_robot)/worlds/flags.world"/>
    <arg name="paused" value="false"/>
    <arg name="use_sim_time" value="true"/>
    <arg name="gui" value="true"/>
    <arg name="headless" value="false"/>
    <arg name="debug" value="false"/>
  </include>
  ```

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
