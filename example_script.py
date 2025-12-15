import turtlethread

needle = turtlethread.Turtle()
with needle.triple_stitch(20):
    for square in range(8):
        for side in range(4):
            needle.forward(200)
            needle.right(90)
        needle.right(45)

needle.show_info()
needle.save("square_flower.jef")
needle.visualise()
needle.save("square_flower.svg")
