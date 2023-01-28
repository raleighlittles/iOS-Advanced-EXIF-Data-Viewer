import matplotlib.pyplot
import typing

def create_accelerometer_plot(image_basename : str, accel_vector : typing.List):
    """
    Creates a matplotlib 3D quiver plot of the acceleration vector:
    https://matplotlib.org/stable/gallery/mplot3d/quiver3d.html
    """

    x, y, z = accel_vector

    fig = matplotlib.pyplot.figure()

    ax = fig.add_subplot(projection='3d')

    ax.set_title("Acceleration (g) in image " + image_basename)

    ax.set_xlabel("X - (+) Left / (-) Right")
    ax.set_xlim(-1, 1)

    ax.set_ylabel("Y - (+) Down / (-) Up")
    ax.set_ylim(-1, 1)

    ax.set_zlabel("Z - (+) Into phone / (-) Out of")
    ax.set_zlim(-1, 1)

    # Coordinate at the origin
    ax.scatter(0,0,0)

    # Plot individual components, use CIE color space, then plot overall
    ax.quiver(0, 0, 0, x, 0, 0, color='red')
    ax.quiver(0, 0, 0, 0, y, 0, color = 'green')
    ax.quiver(0, 0, 0, 0, 0, z, color='blue')
    ax.quiver(0, 0, 0, x, y, z, color = 'black')


    matplotlib.pyplot.savefig(image_basename + ".png")