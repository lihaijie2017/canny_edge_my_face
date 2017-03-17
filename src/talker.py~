#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

def talker():
	
	# Read cv2 image from camera
	# Convert cv2 image to ros image type
	# Publish ros image 
    pub = rospy.Publisher('my_camera/image_raw', Image, queue_size=1) 
    rospy.init_node('talker', anonymous=True) 
    rate = rospy.Rate(30)
    bridge = CvBridge()
    Video = cv2.VideoCapture(0)
    while not rospy.is_shutdown():
        ret, img = Video.read()
        cv2.imshow("talker", img)
        cv2.waitKey(3)
        pub.publish(bridge.cv2_to_imgmsg(img, "bgr8"))
        rate.sleep()

if __name__ == '__main__':
     try:
         talker()
     except rospy.ROSInterruptException:
         pass
