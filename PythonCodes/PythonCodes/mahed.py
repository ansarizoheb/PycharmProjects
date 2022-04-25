from cmath import pi, sqrt

def circumference(r):
    c = 2*pi*r
    return c

def quadratic(a, b, c):
    d = (b**2) - (4*a*c)

    sol1 = (-b-sqrt(d))/(2*a)
    sol2 = (-b+sqrt(d))/(2*a)
    return sol1, sol2

print('''If you want to calculate quadratic equation press q.
If you want to calculate circumference of the circle press c.''')
qw = input()

if (qw == 'q' or qw == 'Q'):
    result = quadratic(float(input("Enter coefficients of 2 degree quadratic equation: ")), float(input()), float(input()))
    print(result)

elif (qw == 'c' or qw == 'C'):
    result = circumference(float(input("Enter radius of the circle: ")))
    print('The solution are {0} and {1}'.format(result))