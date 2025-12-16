import turtlethread

needle = turtlethread.Turtle()
with needle.running_stitch(20):
    needle.forward(200)
    needle.right(120)
    needle.forward(200)
    needle.right(120)
    needle.forward(200)
    needle.right(120)

needle.show_info()
needle.save("triangle.jef")
needle.visualise()
needle.save("triangle.svg")
