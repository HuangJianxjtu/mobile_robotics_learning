from math import sin,cos,pi
import matplotlib.pyplot as plt
from diffdrive import diffDrive

# testing
# motion c1
x_1,y_1,theta_1 = diffDrive(1.5, 2.0, pi/2, 0.3, 0.3, 3.0, 0.5)
print(x_1, y_1, theta_1)

# motion c2
x_2,y_2,theta_2 = diffDrive(x_1, y_1, theta_1, 0.1, -0.1, 1.0, 0.5)
print(x_2, y_2, theta_2)

# motion c3
x_3,y_3,theta_3 = diffDrive(x_2, y_2, theta_2, 0.2, 0.0, 2.0, 0.5)
print(x_3, y_3, theta_3)

# visualization
# quiver(x,y,u,v)
# A quiver plot displays the velocity vectors as arrows with components (u,v) at the points (x,y).
plt.quiver(1.5, 2.0, cos(pi/2), sin(pi/2))
plt.quiver(x_1, y_1, cos(theta_1), sin(theta_1))
plt.quiver(x_2, y_2, cos(theta_2), sin(theta_2))
plt.quiver(x_3, y_3, cos(theta_3), sin(theta_3))
plt.xlim([0.5, 2.5])
plt.ylim([1.5, 3.5])
plt.show()
