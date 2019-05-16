import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.GnBu, s=20, edgecolor="none")

# title and axes labels
plt.title("Square numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square", fontsize=14)

# tick labels
plt.tick_params(axis="both", labelsize=14, which="major")

# set the range for each axis
plt.axis([0, 1100, 0, 1100000])

plt.show()
#plt.savefig("squares_plot", bbox_inches="tight")
