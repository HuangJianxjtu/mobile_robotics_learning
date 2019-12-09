import numpy as np
import math
import matplotlib.pyplot as plt

scan = np.loadtxt('laserscan.dat')
angle = np.linspace(-math.pi/2, math.pi/2,np.shape(scan)[0], endpoint='true')

def plot_ranges():
    x = np.multiply(scan, np.cos(angle))
    y = np.multiply(scan, np.sin(angle))
    plt.scatter(x,y,marker='.',s=20.0)
    plt.gca().set_aspect('equal', adjustable = 'box')
    plt.show()

plot_ranges()

theta_r = np.pi/4
T_wb = np.array([[np.cos(theta_r), -np.sin(theta_r), 1.0],[np.sin(theta_r), np.cos(theta_r), 0.5],[0.0, 0.0, 1.0]])
theta_l = np.pi
T_bl = np.array([[np.cos(theta_l), -np.sin(theta_l), 0.2],[np.sin(theta_l), np.cos(theta_l), 0.0],[0.0, 0.0, 1.0]])
T_wl = np.matmul(T_wb, T_bl)

# plot the center of robot
plt.scatter([T_wb[0][2]],[T_wb[1][2]],c='r',marker='s')

# plot the center of laser range finder
plt.scatter([T_wl[0][2]],[T_wl[1][2]],c='r',marker='*')

# laser end-points
laserPs_x_l = np.multiply(scan, np.cos(angle))
laserPs_y_l = np.multiply(scan, np.sin(angle))
ones = np.ones(np.shape(scan)[0])
ts_l = np.column_stack((laserPs_x_l, laserPs_y_l,ones))

# print(np.transpose(ts_l).shape)
laserPs_x_w = np.matmul(ts_l, T_wl[0])
laserPs_y_w = np.matmul(ts_l, T_wl[1])
plt.scatter(laserPs_x_w, laserPs_y_w,s=5.0)
plt.gca().set_aspect('equal', adjustable = 'box')
plt.show()
