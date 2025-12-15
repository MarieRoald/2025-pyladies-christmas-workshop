from js import Uint8Array, File, URL, document
import pyembroidery
import functools
import base64
import turtlethread

old_write = pyembroidery.write


def display_svg(filename: str, content: bytes) -> None:
    svg_data = content.decode()
    svg_container = document.createElement("div")
    svg_container.innerHTML = svg_data
    svg_container.setAttribute("download", filename)
    document.getElementById("turtlethreadOutput").append(svg_container)


def display_png(filename: str, content: bytes) -> None:
    base64_img = base64.b64encode(content)
    png_container = document.createElement("img")
    png_container.src = f"data:image/png;base64, {base64_img}"
    png_container.setAttribute("download", filename)
    document.getElementById("turtlethreadOutput").append(png_container)


def display_other(filename: str, content: bytes) -> None:
    js_array = Uint8Array.new(len(content))
    js_array.assign(memoryview(content))

    file = File.new([js_array], filename, {type: "application/octet-stream"})
    url = URL.createObjectURL(file)

    link = document.createElement("a")
    # The second parameter here is the actual name of the file that will appear in the user's file system
    link.setAttribute("download", filename)
    link.setAttribute("href", url)
    link.innerHTML = "Download embroidery file"

    document.getElementById("turtlethreadOutput").append(link)


@functools.wraps(old_write)
def write(pattern, filename, settings=None) -> None:
    old_write(pattern=pattern, filename=filename, settings=settings)
    with open(filename, "rb") as f:
        content = f.read()

    if filename.lower().endswith(".svg"):
        display_svg(filename, content)
    elif filename.lower().endswith(".png"):
        display_png(filename, content)
    else:
        display_other(filename, content)


def patch_turtlethread_turtle() -> None:
    turtlethread.turtle.write = write
