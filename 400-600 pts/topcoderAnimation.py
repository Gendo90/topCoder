# Problem Statement
#
# A collection of particles is contained in a linear chamber. They all have the same speed, but some are headed toward the right and others are headed toward the left. These particles can pass through each other without disturbing the motion of the particles, so all the particles will leave the chamber relatively quickly.
# We will be given the initial conditions by a string init containing at each position an 'L' for a leftward moving particle, an 'R' for a rightward moving particle, or a '.' for an empty location. init shows all the positions in the chamber. Initially, no location in the chamber contains two particles passing through each other.
# We would like an animation of the process. At each unit of time, we want a string showing occupied locations with an 'X' and unoccupied locations with a '.'. Create a class Animation that contains a method animate that is given an int speed and a string init giving the initial conditions. The speed is the number of positions each particle moves in one time unit.
# The method will return a tuple (string) in which each successive element shows the occupied locations at the next time unit. The first element of the return should show the occupied locations at the initial instant (at time = 0) in the 'X','.' format. The last element in the return should show the empty chamber at the first time that it becomes empty.
# Definition
#
# Class:
# Animation
# Method:
# animate
# Parameters:
# integer, string
# Returns:
# tuple (string)
# Method signature:
# def animate(self, speed, init):

# Gendo90 has submitted the 500-point problem for 344.02 points
# Successful on first try!

#Good job!
class Animation(object):
    def animate(self, speed, init):
        left_particles = [i for i, particle in enumerate(init) if(particle=="L")]
        right_particles = [i for i, particle in enumerate(init) if(particle=="R")]
        total_size = len(init)
        changing_chamber = ["X" if (particle=="L" or particle=="R") else particle for particle in init]
        output = ["".join(changing_chamber)]
        while(left_particles or right_particles):
            left_particles = [i-speed for i in left_particles if(i-speed>=0)]
            right_particles = [i+speed for i in right_particles if(i+speed<total_size)]
            for i in range(total_size):
                if(i in left_particles or i in right_particles):
                    changing_chamber[i] = "X"
                else:
                    changing_chamber[i] = "."
            # print(changing_chamber)
            output.append("".join(changing_chamber))

        return tuple(output)


test = Animation()

print(test.animate(2, "..R...." ))
