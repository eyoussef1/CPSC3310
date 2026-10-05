import turtle

SQUARE = "1"
CIRCLE = "2"
TRIANGLE = "3"
QUIT = "4"


def main():
    choice = ""

    while choice != QUIT:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == SQUARE:
            square(0, 0, 100, "blue")
        elif choice == CIRCLE:
            circle(0, 0, 50, "red")
        elif choice == TRIANGLE:
            equilateral_triangle(0, 0, 100, "green")
        elif choice != QUIT:
            print("Invalid choice. Please try again.")

    if choice == QUIT:
        turtle.bye()


def display_menu():
    print()
    print("Shape Menu")
    print("1) Draw a Square")
    print("2) Draw a Circle")
    print("3) Draw an Equilateral Triangle")
    print("4) Quit")


def square(x, y, side, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()

    for count in range(4):
        turtle.forward(side)
        turtle.left(90)

    turtle.end_fill()


def equilateral_triangle(x, y, side, color):

    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()

    for count in range(3):
        turtle.forward(side)
        turtle.left(120)

    turtle.end_fill()


def circle(x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


if __name__ == "__main__":
    main()
