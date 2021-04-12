import numpy as np
import matplotlib.pyplot as plt

generator = np.random.default_rng()
#generator.seed(0)

def random_direction(dimension):
    """ Generates random direction in the dimension-dimensional space by generating a point
        in a unit cube and deciding whether it lies inside a unit sphere.
        In higher dimension it is highly ineffective because a majority of points lie outside
        of the sphere.
    """
    while True:                                 # This should be used with care - infinite cycle
        random_vector = 2 * generator.random(dimension) - 1
        norm = np.linalg.norm(random_vector)    # Norm of the vector
        if norm <= 1:                           # We are within the unit cube
            return random_vector / norm
        

def random_direction_gaussian(dimension):
    """ Generates random direction in the dimension-dimensional space 

        References:
        [1] M.E. Muller, A note on a method for generating points uniformly on n-dimensional spheres,
                Communications of the Asociation for Computing Machinery 2, 19 (1959)
        [2] G. Marsaglia, Choosing a Point from the Surface of a Sphere,
                The Annals of Mathematical Statistics 43, 645 (1972)
    """
    random_vector_gaussian = generator.normal(size=dimension)
    return random_vector_gaussian / np.linalg.norm(random_vector_gaussian)
    

def random_walk(dimension=3, num_steps=1000, step_size=1, box_size=10, initial_condition=0, direction=random_direction, cyclic=False):
    """ Generates and plots a random walk in an arbitrary dimension.
        If the trajectory leaves the given box, the calculation is interrupted.
    """
    if initial_condition == 0:                   # We start from the origin
        initial_condition = np.zeros(dimension)
    
    position = np.array(initial_condition)
    path = [position]

    box = np.full(dimension, box_size)          # Creates an array with size=dimension whose each element has value box_size                                            

    for _ in range(0, num_steps):
        new_position = position + step_size * direction(dimension)

        if (new_position < -box).any() or (new_position > box).any(): # A check whether we are within the given box
            if not cyclic:                      # Not cyclic boundary conditions - leave the for cycle
                break

            new_position = (new_position + box) % (2 * box) - box
        
        path.append(new_position)
        position = new_position

    path = np.array(path)
    return path


def histogram_circle(direction=random_direction, dimension=3, iterations=30000, axis1=0, axis2=1, bins=60):
    """ Visualize the probabilty density on a circle in the plane given by axis1, axis2. (thanks to Samuel J.) """
    angles = []
    for _ in range(iterations):
        step = direction(dimension)
        angles.append(np.arctan2(step[axis1], step[axis2]))
        
    plt.hist(angles, bins=bins, label=f"dim={dimension}, axes=({axis1},{axis2})")
    plt.legend()
    plt.show()


print(random_walk(dimension=10, num_steps=100))

histogram_circle(dimension=2)
histogram_circle(dimension=3)
histogram_circle(dimension=3, axis1=1, axis2=2)