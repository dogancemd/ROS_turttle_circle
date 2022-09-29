#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

rospy.init_node("circle",anonymous=True)


pub = rospy.Publisher("turtle1/cmd_vel",Twist, queue_size=1000)
ang_velo=Twist()
ang_velo.angular.z=1
ang_velo.linear.x=2
if __name__ == "__main__":
    r=rospy.Rate(1)
    while True:
        r.sleep()
        pub.publish(ang_velo)
