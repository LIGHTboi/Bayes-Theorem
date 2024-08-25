import matplotlib.pyplot as plt
import csv

data = {}
f = open('D:\Addy\Python Files\Maths Model\\bayesMean.csv')
cr = csv.reader(f)
for i in cr:
    data[int(i[0])] = float(i[1])

plt.figure(dpi=128, figsize=(11, 8))
ax = plt.axes(projection="3d")
x_data = tuple(i for i in range(1,101) for j in range(1,101))
y_data = tuple(j for i in range(1,101) for j in range(1,101))
z_data = tuple(data[i]/sum(data[k] for k in range(1, j + 1)) if j>=i else 0 for i in range(1, 101) for j in range(1, 101))

ax.plot(x_data, y_data, z_data, linewidth = 0.6)
ax.set_title("P(N Hints | Ball is Found)")
ax.set_xlabel("Number of Hints per Trial")
ax.set_ylabel("Number of Hints in Sample Space")
ax.set_zlabel("P(N Hints | Ball is Found)")

plt.show()