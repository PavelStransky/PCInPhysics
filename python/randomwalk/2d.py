import random
import numpy as np
import matplotlib.pyplot as plt

# random.seed(0)                                            # For always the same walk uncomment this

def random_direction_2d():
    """ Generates a random direction in the 2D plane """
    phi = random.uniform(0, 2 * np.pi)
    return np.array([np.cos(phi), np.sin(phi)])
    

def random_walk_2d(num_steps=1000, step_size=1, box_size=10, initial_condition=[0,0]):
    """ Generates and plots a random walk in a 2D plane.
        If the trajectory leaves the given box, the calculation is interrupted.
    """    
    position = np.array(initial_condition)
    path = [position]

    box = np.array([box_size, box_size])

    for _ in range(0, num_steps):                           # _ means unused variable
        position = position + step_size * random_direction_2d() # for some unknown reason the command
                                                            # position += random_direction_2d()
                                                            # doesn't work here

        if (position < -box).any() or (position > box).any(): # A check whether we leave the given box
            break

        path.append(position)

    path = np.array(path)

    plt.ioff()
    plt.plot(path[:,0], path[:,1], label=f"N={len(path)}")
    plt.xlim(-box_size, box_size)
    plt.ylim(-box_size, box_size)
    plt.legend()
    plt.show()

    return path


def random_walk_2d_interactive(num_steps=1000, step_size=1, box_size=10, initial_condition=[0,0], cyclic=False):
    """ Generates and interactivelly plots a random walk in a 2D plane.
    """    
    position = np.array(initial_condition)
    path = [position]

    box = np.array([box_size, box_size]) 

    # Switch on the interactive mode (in order to plot more random walks into one graph)
    # - In Spyder you have to write the command "%matplotlib auto" into the REPL first
    plt.ion()
    plt.xlim(-box_size, box_size)
    plt.ylim(-box_size, box_size)
    
    for i in range(0, num_steps):
        new_position = position + step_size * random_direction_2d()            

        if (new_position < -box).any() or (new_position > box).any(): # A check whether we are within the given box
            if not cyclic:                              # Not cyclic boundary conditions - leave the for cycle
                break

            shift_new_position = (new_position + box) % (2 * box) - box

            ### This part of the code is just for aesthetic reasons
            shift_position = position + (shift_new_position - new_position)
            plt.plot([position[0], new_position[0]], [position[1], new_position[1]], 'blue')
            plt.plot([shift_position[0], shift_new_position[0]], [shift_position[1], shift_new_position[1]], 'blue')
            ###

            new_position = shift_new_position

        else:                                           # Plot only if we don't apply the cyclic boundary conditions
            plt.plot([position[0], new_position[0]], [position[1], new_position[1]], 'blue')
            plt.title(i)
            plt.show()
            plt.pause(0.1)

        path.append(new_position)
        position = new_position

    path = np.array(path)
    return path

#random_walk_2d()
random_walk_2d_interactive(cyclic=True)