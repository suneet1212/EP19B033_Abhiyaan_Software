#!/usr/bin/env python
import rospy
from std_msgs.msg import String

class Subs:
    def __init__(self):
        self.str1 = ""
        self.str2 = ""
        self.marker = 0
        self.sub1 = rospy.Subscriber('/team_abhiyaan', String, self.callback1)
        self.sub2 = rospy.Subscriber('/autonomy', String, self.callback2)

        # print(self.str1 + self.str2)

    def callback1(self, msg):
        self.str1 = msg.data + ' '
        # self.printmsg()
        # print(self.str1 + self.str2)

    def callback2(self, msg):
        self.str2 = msg.data
        # self.printmsg()
        if self.marker == 0:
            self.marker = 1
        else:
            print(self.str1 + self.str2)

if __name__ == "__main__":
    rospy.init_node('subscriber')
    sub = Subs()
    rospy.spin()