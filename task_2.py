import turtle


def draw_koch_line(pen, length, level):
    if level == 0:
        pen.forward(length)
        return

    draw_koch_line(pen, length / 3, level - 1)
    pen.left(60)
    draw_koch_line(pen, length / 3, level - 1)
    pen.right(120)
    draw_koch_line(pen, length / 3, level - 1)
    pen.left(60)
    draw_koch_line(pen, length / 3, level - 1)


if __name__ == "__main__":
    try:
        level = int(input("Enter the recursion level (0 or higher): "))
        if level < 0:
            raise ValueError
    except ValueError:
        print("Please enter a whole number of 0 or higher.")
    else:
        screen = turtle.Screen()
        screen.title("Koch Snowflake")
        screen.setup(800, 600)
        screen.tracer(0)

        pen = turtle.Turtle()
        pen.hideturtle()
        pen.penup()
        pen.goto(-150, 90)
        pen.pendown()

        for _ in range(3):
            draw_koch_line(pen, 300, level)
            pen.right(120)

        screen.update()
        screen.mainloop()

