import numpy as np
import matplotlib.pyplot as plt

def func(x, a, b, c, d, e):
    return a*x**4*np.sin(np.cos(x)) + b*x**3 + c*x**2 + d*x + e

KF = [-12, -18, 5, 10, -30]
x_limit = [-10, 10]
x = np.arange(x_limit[0], x_limit[1], 0.1)
color = 'r'
x_change = []
x_point = []
func_direct = -1

def change_color():
    global color
    if color == 'r':
        color = 'b'
    else:
        color = 'r'
    return color

for i in range(len(x) - 1):
    if func_direct == -1:
        if func(x[i], *KF) < func(x[i+1], *KF):
            func_direct = 1
            x_change.append((x[i], func(x[i], *KF)))
else:
    if func(x[i], *KF) > func(x[i+1], *KF):
        func_direct = -1
        x_change.append((x[i], func(x[i], *KF)))

for i in range(len(x)-1):
    if (func(x[i], *KF) > 0 and func(x[i+1], *KF) < 0) or (func(x[i], *KF) < 0 and func(x[i+1], *KF)>0):
        x_point.append((x[i], func(x[i], *KF)))
    
print(len(x_point))
print(x_point)

x_cur = np.arange(x_limit[0], x_change[0][0], 0.1)
plt.plot(x_cur, func(x_cur, *KF), change_color())
for i in range(len(x_change) -1):
    x_cur = np.arange(x_change[i][0], x_change[i+1][0], 0.1)
    plt.plot(x_cur, func(x_cur, *KF), change_color())
x_cur = np.arange(x_change[-1][0], x_limit[1], 0.1)
plt.plot(x_cur, func(x_cur, *KF), change_color())

for x_cur in x_point:
    plt.plot(x_cur[0], func(x_cur[0], *KF), 'rx')

plt.grid(visible=True)
plt.show()
