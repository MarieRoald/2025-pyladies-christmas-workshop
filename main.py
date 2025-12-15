import sys

modules = sys.modules  # Store this so we can reset the imported modules

import js
from js import document
from functools import wraps

js.resetEditor()


# The builtin Pyodide input method is a bit weird, so we overwrite it with this to make it a bit easier to understand
@wraps(input)
def input(prompt):
    out = js.window.prompt(prompt)
    print(f"{prompt}{out}")
    return out


__old_print = print


@wraps(print)
def print(*objects, sep=" ", end="\n", file=None, flush=False):
    if file:
        __old_print(*objects, sep=sep, end=end, file=file, flush=flush)
        return

    content = sep.join(str(obj) for obj in objects) + end
    terminal = document.getElementById("outputTerminal")
    if terminal:
        terminal.innerHTML += content


def get_code(*args):
    """Extract the content from the codemirror editor."""
    code = js.editor.getValue()
    code = (
        "import builtins\n"
        + "builtins.print = print\n"
        + "import importlib\n"
        + "import svg\n"
        + "import turtle\n"
        + "importlib.reload(svg)\n"
        + "importlib.reload(turtle)\n"
        + "import turtlethread_pyscript\n"
        + "turtlethread_pyscript.patch_turtlethread_turtle()\n"
        + "del turtlethread_pyscript, turtle, importlib, svg, builtins\n"
        + code
    )
    __old_print("code", code)
    return code


def clear(*args):
    """Clear the PyScript terminal."""
    terminal = document.getElementById("outputTerminal")
    canvas = document.getElementById("turtlethreadOutput")
    terminal.innerHTML = ""
    canvas.innerHTML = ""


def run_code(*args):
    """Reset the terminal and run the code from the editor in an empty scope."""
    import sys

    sys.modules = modules  # Reset imported modules

    code = get_code()
    clear()

    # We put the code in a try-except block so the traceback is printed in the terminal
    try:
        exec(code, {"input": input, "print": print})
    except Exception as e:
        import traceback

        for tb_line in traceback.format_exception(e):
            print(tb_line, end="")
