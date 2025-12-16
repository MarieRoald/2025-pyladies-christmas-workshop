import turtlethread

needle = turtlethread.Turtle()

def kvart_hjerte(kant_lengde: int, needle):
    needle.forward(kant_lengde)
    needle.circle(radius=kant_lengde/2, extent=180)
    needle.right(90)
    needle.circle(radius=kant_lengde/2, extent=180)
    needle.forward(kant_lengde)

with needle.running_stitch(20): # 2mm
    for i in range(4):
        kvart_hjerte(kant_lengde=150, needle=needle)

needle.show_info()
needle.save("waffle.jef")
needle.visualise(scale=0.5)