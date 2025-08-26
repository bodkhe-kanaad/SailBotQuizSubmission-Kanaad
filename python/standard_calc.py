def bound_to_180(angle):
    """Bounds the provided angle between [-180, 180) degrees.

    e.g.)
        bound_to_180(135) = 135.0
        bound_to_180(200) = -160.0

    Args:
        angle (float): The input angle in degrees.

    Returns:
        float: The bounded angle in degrees.
    """
   # Step 1: Reduce the angle into a single circle [0, 360)
    wrapped = angle % 360

    # Step 2: Shift into [-180, 180)
    # If the angle is less than 180, it's already fine (e.g. 90 stays 90).
    # If the angle is ≥ 180, it means we went "too far" counterclockwise,
    # so we subtract 360 to get the equivalent negative angle.
    if wrapped >= 180:
        wrapped -= 360

    return wrapped


def is_angle_between(first_angle, middle_angle, second_angle):
    """Determines whether an angle is between two other angles.

    e.g.)
        is_angle_between(0, 45, 90) = True
        is_angle_between(45, 90, 270) = False

    Args:
        first_angle (float): The first bounding angle in degrees.
        middle_angle (float): The angle in question in degrees.
        second_angle (float): The second bounding angle in degrees.

    Returns:
        bool: True when `middle_angle` is not in the reflex angle of `first_angle` and `second_angle`, false otherwise.
    """

       # Normalize into [0, 360)
    a = first_angle % 360
    b = middle_angle % 360
    c = second_angle % 360

    # Arc angles measured counterclockwise
    arc_ac = (c - a) % 360     # distance from a to c
    arc_ab = (b - a) % 360     # distance from a to b

    # middle is between if it lies inside arc_ac
    return 0 < arc_ab < arc_ac
