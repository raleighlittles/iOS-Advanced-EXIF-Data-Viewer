import matplotlib.pyplot
import typing

def create_accelerometer_plot(accel_vector : typing.List) -> str:
    """
    Return filename
    """

    x, y, z = accel_vector

    fig = matplotlib.pyplot.figure()

    ax = fig.add_subplot(projection='3d')

    # TODO: print `g` in LaTeX format
    ax.set_title("Acceleration (g)")

    ax.set_xlabel("X")
    ax.set_xlim(-1, 1)

    ax.set_ylabel("Y")
    ax.set_ylim(-1, 1)

    ax.set_zlabel("Z")
    ax.set_zlim(-1, 1)

    #ax.axis('equal')

    #ax.set_aspect('equal')

    ax.quiver(0, 0, 0, x, y, z, normalize=True)
    
    #ax.set_box_aspect([1,1,1])


    matplotlib.pyplot.savefig("figure.png")

    return "figure.png"

