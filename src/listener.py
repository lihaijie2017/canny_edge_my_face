#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge
import numpy as np

def callback(imgmsg):
	
	# Read in a ros image from "talker.py"
	# Convert image to cv2 type
	# Apply canny filter using opencv
	# Tranform img into ros image type
	# Publish modified image
    bridge = CvBridge()
    img = bridge.imgmsg_to_cv2(imgmsg, "bgr8")
    edge = cv2.Canny(img, 50,200)
    edge_ros = bridge.cv2_to_imgmsg(edge)
    pub.publish(edge_ros)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("my_camera/image_raw", Image, callback)
    rospy.spin()

if __name__ == '__main__':
    pub = rospy.Publisher('my_img/edge', Image, queue_size=1)
    listener()
