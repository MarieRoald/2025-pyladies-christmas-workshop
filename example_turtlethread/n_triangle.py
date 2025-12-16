import argparse
import math

import turtlethread


def find_last_side(side_length: int, number_of_triangles: int) -> float:
    """Use law of cosines to find the unknown side in an isosceles (=likebeint) triangle"""
    angle = 360 / number_of_triangles
    radian_angle = math.radians(angle)

    side_squared = (
        side_length**2
        + side_length**2
        - 2 * side_length * side_length * (math.cos(radian_angle))
    )
    return math.sqrt(side_squared)


def make_n_part_triangle(
    same_side_length: int,
    middle_side_length: int,
    rotate_angle: float,
    needle,
):
    needle.forward(same_side_length)
    needle.left(rotate_angle)
    needle.forward(middle_side_length)
    needle.left(rotate_angle)
    needle.forward(same_side_length)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Draw an N-part triangle pattern.")
    parser.add_argument(
        "n",
        type=int,
        nargs="?",
        default=10,
        help="How many triangles to stitch around the circle (default: %(default)s)",
    )
    parser.add_argument(
        "same_side_length",
        nargs="?",
        type=int,
        default=150,
        help="Length of the two equal sides in each triangle (default: %(default)s)",
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

    rotate_angle = 180 - angle_u

    needle = turtlethread.Turtle()

    with needle.running_stitch(20):  # 2mm
        for i in range(n):
            make_n_part_triangle(
                same_side_length=same_side_length,
                middle_side_length=middle_side_length,
                rotate_angle=rotate_angle,
                needle=needle,
            )
            needle.left(180)

    needle.show_info()
    needle.save(f"triangles_{n}.jef")
    needle.visualise(scale=0.5)


if __name__ == "__main__":
    main()
