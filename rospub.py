#!/usr/bin/env python
# license removed for brevity

import rospy
import cv2
from geometry_msgs.msg import Twist
    
def pubvel():

    ret, frame = cap.read()
    frame = np.reshape(frame,[1,480,640,3])
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    model = load_model('1.h5')

    vel_msg = Twist()
    vel_msg.linear.x = 0.2
    vel_msg.angular.z = float(model.predict(frame, batch_size=1))
    
    pub = rospy.Publisher('pubvel', , queue_size=10)
    rospy.init_node('pubvel', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    
    while not rospy.is_shutdown():
        hello_str = "angle publishing %s" % rospy.get_time()
        rospy.loginfo(vel_msg.angular.z)
        pub.publish(vel_msg)
        rate.sleep()

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    try:
        pubvel()
    except rospy.ROSInterruptException:
        pass