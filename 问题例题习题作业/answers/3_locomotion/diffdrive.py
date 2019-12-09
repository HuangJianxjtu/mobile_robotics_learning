from math import sin,cos,pi

def diffDrive(x, y, theta, v_l, v_r, t, l):
    # where x, y, and θ is the pose of the robot, vl and vr are the
    # speed of the left and right wheel, t is the driving time, and 
    # l is the distance between the wheels of the robot.

    # straight line
    if(v_l == v_r):
        theta_n = theta
        x_n = x + v_l*t*cos(theta)
        y_n = y+ v_l*t*sin(theta)

    # circular motion
    else:
        R = l*(v_l+v_r)/(2*(v_r-v_l))
        ICC_x = x-R*sin(theta)
        ICC_y = y+R*cos(theta)
        w_ = (v_r-v_l)/l
        x_n = cos(w_*t)*(x-ICC_x)-sin(w_*t)*(y-ICC_y)+ICC_x
        y_n = sin(w_*t)*(x-ICC_x)+cos(w_*t)*(y-ICC_y)+ICC_y
        theta_n = theta+w_*t

    return x_n,y_n,theta_n
