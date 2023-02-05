# Heterogeneous-robots-ws

This repository includes a variety of robot models and a single launch file for launching many robots inside a simulation. The purpose of this repository is to make the process of spawning various robots simpler and more comfortable for the user. This repository allows the user to launch many robots with a single command, speeding simulation setup and decreasing preparation time. Whether you are investigating novel robot models or doing sophisticated simulations, this repository offers a straightforward and effective solution for your requirements.

This repository contains various types of robots, including:

1. Mobile robots
2. Manipulator robots
3. Drone robots

The collection of mobile robots in particular is extensive, offering a variety of models, including:

* Two-wheeled robots
* Four-wheeled robots
* Simple robots
* Neuronbot robots

Each model has been carefully crafted and optimized for use in simulations, providing the user with a diverse range of options for their needs. Whether you are exploring new robotic designs or running complex simulations, this repository has you covered with its comprehensive collection of robots.



1. clone the repository: `git clone https://github.com/khalidbourr/Heterogeneous-robots-ws.git`
2. import your world inside `cd Heterogeneous-robots-ws/src/Hetero_robots/src/multi_robot/worlds`
3. in case of new model "custom_model", copy them inside :`cd Heterogeneous-robots-ws/src/Hetero_robots/src/multi_robot/worlds/custom_model`
4. and then inside gazeebo, example below:
```
cd Heterogeneous-robots-ws/src/Hetero_robots/src/multi_robot/worlds
sudo cp -r custom_model ~/.gazebo/models
```
4- Modify the launch file, with the type and the model of the robots

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
  
5- build the workspace 
```
cd Heterogeneous-robots-ws/
rosdep install --from-paths src --ignore-src -r -y
catkin_make
```
Launch
```
source devel/setup.bash
roslaunch multi_robot multi_robot.launch
```
