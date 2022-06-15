#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Pose
from random import gauss
from random import seed

class Correction:
    def __init__(self):
        seed(1) #Init
        rospy.init_node("Correction", anonymous = True)
        rospy.Subscriber("/odom", Odometry, self.callback)
        self.pub = rospy.Publisher("/pose_robot", Pose, queue_size = 1)

        rospy.spin() #Wait the end



    def callback(self, data):
        P = Pose()
        P.position.x = data.pose.pose.position.x + gauss(0,0.1)
        P.position.y = data.pose.pose.position.y + gauss(0,0.1)
        P.position.z = data.pose.pose.position.z + gauss(0,0.1)

        P.orientation.x = data.pose.pose.orientation.x
        P.orientation.y = data.pose.pose.orientation.y
        P.orientation.z = data.pose.pose.orientation.z
        P.orientation.w = data.pose.pose.orientation.w


        self.pub.publish(P)

Correction()
