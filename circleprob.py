import random
import math
import numpy as np

def main():
    smaller = 0
    larger = 0
    print("""What is the probability of a randomly chosen chord in a circle having a length
greater than the radius? There are 3 different (correct!) methods of calculating this probability,
and each of the 3 methods provides a different answer. This program attempts to simulate
the three different methods of creating a random chord in order to experimentally determine
the probability.

Choice 1: Two random points on a unit circle are chosen using trigonometric functions and the distance between
them is calculated.

Choice 2: A randomly chosen point inside the circle is defined as the midpoint of a chord. The program then
calculates an endpoint of the chord from the midpoint and uses these two points to calculate the length
of the chord.

Choice 3: A radius is randomly selected from the circle. A point on that radius is randomly chosen as the midpoint of a chord.
The program then calculates an endpoint of the chord given that midpoint and uses these two points to determine the length
of the chord.""")

    # Get user choice for how to pick the random chords: accepts only 1, 2, or 3.
    while True:
        solve_method = GetInt("Enter 1, 2, or 3 to select a method: ")
        if solve_method not in [1, 2, 3]:
            print("Please select a valid method.")
            continue
        else:
            break

    # Prompt the user for the number of trials to run - requires int between 1 and 1 million
    while True:
        trials = GetInt("Enter the number of trials to perform: ")
        if trials < 1 or trials > 1000000:
            print("Please enter an integer between 1 and 1,000,000.")
            continue
        else:
            break

    # First method of solving - finds two endpoints of chords on the circle and calculate the distance between
    if solve_method == 1:
        for _ in range(trials):
            point1 = pick_point_on_circle()
            point2 = pick_point_on_circle()
            distance = calc_distance(point1,point2)
            if distance >= 1:
                larger += 1
            else:
                smaller += 1

    # Second method of solving - finds a random point in the circle to be the midpoint of the chord
    # Calculates the endpoint of a chord with that midpoint, find the distance between midpoint and endpoint
    # and then doubles to find the length of the chord
    if solve_method == 2:
        for _ in range(trials):
            point1 = pick_point_in_circle()
            chord_endpoint = find_endpoint(point1, 1)
            distance = 2 * calc_distance(point1, chord_endpoint)
            if distance >= 1:
                larger += 1
            else:
                smaller += 1

    # Third method of solving - picks a random point on a radius to be the midoint of a chord. Calculates the endpoint
    # of a chord with that midpoint, finds the distance between midpoint and endpoint and then doubles to find the length
    # of the chord.
    if solve_method == 3:
        for _ in range(trials):
            radius_point = pick_radius_point()
            chord_endpoint = find_endpoint(radius_point, 1)
            distance = 2 * calc_distance(radius_point, chord_endpoint)
            if distance >= 1:
                larger += 1
            else:
                smaller += 1

    # Print out results of our testing
    print("There were {} chords smaller than the radius".format(smaller))
    print("There were {} chords larger than the radius.".format(larger))
    prob_larger = float(larger) / trials * 100.0
    print("The probability of the chord being larger than the radius was {}.".format(prob_larger))



def pick_point_on_circle():
    ''' This function picks a random point on the unit circle. The choice is made by selecting
    a random angle between 0 and 2pi radians. The x-coord is the cosine of this angle and the
    y-coord is the sine of this angle. The function returns a point as a 2d array.'''

    angle = random.uniform(0,1)*2*math.pi
    x = math.cos(angle)
    y = math.sin(angle)
    point = np.array([x, y])
    return point


def pick_point_in_circle():
    ''' This function picks a random point inside of a circle. The choice is made by first selecting an angle (t)
    and then a radius, sort of. The radius cannot be used directly because there would be more points selected closer to
    the center of the circle. Instead, a probability distribution function is used to calculate. For the given situation,
    the probability density function for a given radius r must be equal to r^2 (since the circle has radius 1). The density
    function is then p(r) = 2r. Mapping this to a uniform variable, we integrate and say that P(r) = r^2, and this must be equal
    to the uniform density function, u. So u = r^2, which gives r = sqrt(u). The x and y coordinates are then given by r multiplied
    by either the cosine or sine of t respectively.

    The function returns a point as a 2d array.'''

    t = np.random.uniform(0.0, 2.0*np.pi)
    r = np.sqrt(np.random.uniform(0.0, 1.0))
    x = r * np.cos(t)
    y = r * np.sin(t)
    point = np.array([x,y])
    return point

def pick_radius_point():
    point = pick_point_on_circle()
    center_vector = -point
    t = np.random.uniform(0.0, 1.0)
    radius_point = np.add(point, t * center_vector)
    return radius_point


def find_endpoint(midpoint, direction):
    ''' This function determines an endpoint of a chord given its midpoint. The point is determined by moving some distance,
    t along the vector perpendicular to the radius. Points on this line are described by midpoint + T * vector. This will
    be on the edge of the circle when the distance from the origin to a given point on the line determined is equal to the radius.

    The function returns the chord endpoint as a 2d array.'''

    x = midpoint[0]
    y = midpoint[1]
    perp_vector = np.array([-y, x])
    t = ((1-x**2-y**2)/(x**2+y**2))**(1.0/2)
    endpoint = np.add(midpoint, direction * t * perp_vector)
    return endpoint

def calc_distance(point1,point2):
    '''This function calculates the distance between two points and returns that value'''

    distance = ((point1[0]-point2[0])**2 + (point1[1] - point2[1])**2) ** (1.0/2)
    return distance

def GetInt(prompt):
    while True:
        integer = input(prompt)
        try:
            integer = int(integer)
            return integer
        except ValueError:
            print("Please enter an integer.")
            continue

if __name__ == "__main__":
    main()



