#find the distance from point a to point b.
from math import sqrt
x1 = float(input("please give me the coordinate of x1 on the 2D plane: "))
y1 = float(input("please give me the coordinate of y1 on the 2D plane: "))
x2 = float(input("please give me the coordinate of x2 on the 2D plane: "))
y2 = float(input("please give me the coordinate of y2 on the 2D plane: "))
point1 =  pow(( x2 - x1 ), 2)
point2 =  pow(( y2 - y1 ), 2)
d = sqrt((point1 + point2))
print("the distance from point a and point b is", round(d, 2), "units")
#Reflection:
#When I first encountered the math library, sqrt(), and pow(), i was not sure if those were going to be useful in my journey as a student and as a beginner in coding, but when I used it in my code for the very first time, i was amazed by its function for it helped me in making my code a lot shorter.
#I am grateful for the new things I discovered for it prevented my code from becoming longer and more complicated than it has to be.
