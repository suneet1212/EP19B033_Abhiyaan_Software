#!/usr/bin/env python
import rospy
from std_msgs.msg import String
rospy.init_node('node2')
pub = rospy.Publisher('/autonomy', String, queue_size=1)
rate = rospy.Rate(1)
str1 = "Fueled By Autonomy"
while not rospy.is_shutdown():
    pub.publish(str1)
    rate.sleep()