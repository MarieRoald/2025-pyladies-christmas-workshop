import argparse

import turtlethread
from n_triangle import find_last_side


def make_n_part_heart(
    same_side_length: int,
    middle_side_length: int,
    rotate_angle: float,
    needle,
):
    needle.forward(same_side_length)
    needle.left(rotate_angle)
    needle.circle(radius=middle_side_length / 4, extent=180)
    needle.right(180)
    needle.circle(radius=middle_side_length / 4, extent=180)
    needle.left(rotate_angle)
    needle.forward(same_side_length)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Draw a Norwegian waffle (of n hearts).",
    )
    parser.add_argument(
        "n",
        type=int,
        nargs="?",
        default=5,
        help="How many hearts in the waffle (default: %(default)s)",
    )
    parser.add_argument(
        "same_side_length",
        nargs="?",
        type=int,
        default=150,
        help="Length of the two equal sides in each heart (default: %(default)s)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    n = args.n
    same_side_length = args.same_side_length
    middle_side_length = find_last_side(
        side_length=same_side_length,
        number_of_triangles=n,
    )
    # inner angle between the two sides of equal length
    angle_v = 360 / n
    # angle between the unknown side and either of the known sides
    angle_u = (180 - angle_v) / 2
    rotate_angle = 180 - angle_u - 90

    needle = turtlethread.Turtle()

    with needle.running_stitch(20):  # 2mm
        for _ in range(n):
            make_n_part_heart(
                same_side_length=same_side_length,
                middle_side_length=middle_side_length,
                rotate_angle=rotate_angle,
                needle=needle,
            )
            needle.left(180)

    needle.show_info()
    needle.save(f"waffle_{n}.jef")
    needle.visualise(scale=0.5)


if __name__ == "__main__":
    main()
