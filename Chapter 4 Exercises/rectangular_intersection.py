from collections import namedtuple as nt
Rectangle = nt("Rectangle", ('x', 'y', 'width', 'height'))

'''
Funtion that looks for the intersection of rectangles in the XY plane.
Intersection is found using Rectangle objects (namedtuples) with x, y (location)
of vertex closest to the origin, width (along x direction), and hieght (along the
y direction).
'''

def intersect(R1, R2):
    def is_intersect(R1, R2):
        '''
        Looking to make sure there is overlap. If R1.x is less than or equal to
        (including boundary of rectangle) the furthest point along the x-axis
        of R2, then R1 has to be to the left of R1. If the furthest point of R1
        along the x axis is bigger than R2.x, then that tells us that the two
        rectangles share some region of x values. To see if there is true overlap,
        we do the same thing for the y value.
        '''
        return (R1.x <= R2.x + R2.width and R1.x + R1.width >= R2.x and R1.y <= R2.y + R2.height and R1.y + R1.height >= R2.y)


    if not is_intersect(R1, R2):
        print("\nNo overlap found")
        return Rectangle(0, 0, -1, -1) ##No intersection, return a null overlap rectangle

    ##return the dimensions of the regions of overlap
    print("\nOverlap found")
    return Rectangle(
        max(R1.x, R2.x),
        max(R1.y, R2.y),
        max(R1.x + R1.width, R2.x + R2.width) - max(R1.x, R2.x),
        max(R1.y + R1.height, R2.y + R2.height) - max(R1.y, R2.y))

r1 = Rectangle(1, 2, 3, 4)
r2 = Rectangle(5, 6, 2, 5)
r3 = Rectangle(3, 3, 2, 2)
print(intersect(r1, r2))
print(intersect(r1, r3))
print(intersect(r2, r3))
