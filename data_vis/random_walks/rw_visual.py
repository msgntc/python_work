import matplotlib.pyplot as plt

from random_walk import RandomWalk

#keep making new walks as long as the program is active
while True:
    
    # make a random walk
    rw = RandomWalk(100_000)
    rw.fill_walk()

    #plot the pionts in the walk
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(15, 8))
    piont_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=piont_numbers, cmap=plt.cm.Reds, edgecolors="none", s=.5)
    ax.set_aspect('equal')

    # Emphasize the first and last points
    ax.scatter(0, 0, c='red', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='blue', edgecolors='none', s=100)

    # remove the axis 
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? y/n:")
    if keep_running == "n":
        break
    