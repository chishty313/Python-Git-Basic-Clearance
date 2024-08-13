import math
def circle(radius):
    area = math.pi * (radius ** 2)
    circumference = 2 * math.pi * radius
    return area, circumference
area, circumference = circle(3)
print('Area:', round(area, 2), 'Circumference:', round(circumference, 2))