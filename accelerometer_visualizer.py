import matplotlib.pyplot
import typing

def create_accelerometer_plot(accel_vector : typing.List) -> str:
    """
    Return filename
    """

    x, y, z = accel_vector

    fig = matplotlib.pyplot.figure()

    ax = fig.add_subplot(111, projection='3d')

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    ax.quiver(0, 0, 0, x, y, z)

    matplotlib.pyplot.savefig("figure.png")

    return "figure.png"

