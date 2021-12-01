# Create a Spot Painting using the cologram and turtle package

# import colorgram
import turtle, random
# colors = colorgram.extract('image.jpg', 30)

# rgb_colors = []
# for color in colors:
#   r = color.rgb.r
#   g = color.rgb.g
#   b = color.rgb.b
#    rgb_tuple = (r, g, b)
#    rgb_colors.append(rgb_tuple)

# print(rgb_colors)

turtle.colormode(255)
tmnt = turtle.Turtle()
tmnt.speed("fastest")
tmnt.penup()
tmnt.hideturtle()
color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
              (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]
tmnt.setheading(270)
tmnt.forward(400)
tmnt.setheading(0)
dots = 100

for dot_count in range (1, dots + 1):
    tmnt.dot(20, random.choice(color_list))
    tmnt.forward(50)

    if dot_count % 10 == 0:
        tmnt.setheading(90)
        tmnt.forward(50)
        tmnt.setheading(180)
        tmnt.forward(500)
        tmnt.setheading(0)

screen = turtle.Screen()
screen.exitonclick()
