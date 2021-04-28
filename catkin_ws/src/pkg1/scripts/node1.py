#!/usr/bin/env python
import rospy
from std_msgs.msg import String
rospy.init_node('node1')
pub = rospy.Publisher('/team_abhiyaan', String, queue_size=1)
rate = rospy.Rate(1)
str1 = "Team Abhiyaan:"
while not rospy.is_shutdown():
    pub.publish(str1)
    rate.sleep()