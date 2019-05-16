import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making walks
while True:
    # Make a random walk, and plot the points
    # rw = RandomWalk(50000)
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Adjust window size
    plt.figure(figsize=(10, 6))

    number_points = list(range(1, rw.num_points + 1))
    plt.scatter(rw.x_values, rw.y_values, s=1, cmap=plt.cm.GnBu, c=number_points)
    # plt.plot(rw.x_values, rw.y_values, linewidth=2)
    # plt.scatter(rw.x_values, rw.y_values, s=1, cmap=plt.cm.tab20, c=number_points)

    # Emphasize first and last point
    plt.scatter([0], [0], c='green', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)

    # clean up axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk?")
    if keep_running == 'n':
        break
