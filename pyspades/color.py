from math import floor
from typing import Tuple

ColorTuple = Tuple[float, float, float]


def wrap(minimum: float, maximum: float, value: float) -> float:
    return value - floor(
        (value - minimum) / (maximum - minimum)) * (maximum - minimum)


def hsb_to_rgb(hue: float, sat: float, bri: float) -> ColorTuple:
    bri_n = bri * 255.0
    if sat == 0.0:
        # greyscale
        r, g, b = bri_n, bri_n, bri_n
    else:
        hue_n = wrap(0.0, 1.0, hue) * 6  # wrap hue
        hue_i = floor(hue_n)  # get integer part
        hue_f = hue_n - hue_i  # fractional part
        if hue_i % 2 == 0:
            hue_f = 1.0 - hue_f
        m = bri_n * (1.0 - sat)
        n = bri_n * (1.0 - (sat * hue_f))
        if hue_i == 0 or hue_i == 6:
            r, g, b = bri_n, n, m
        elif hue_i == 1:
            r, g, b = n, bri_n, m
        elif hue_i == 2:
            r, g, b = m, bri_n, n
        elif hue_i == 3:
            r, g, b = m, n, bri_n
        elif hue_i == 4:
            r, g, b = n, m, bri_n
        elif hue_i == 5:
            r, g, b = bri_n, m, n
    return int(r), int(g), int(b)


def interpolate_rgb(xyz1, xyz2, t):
    (r1, g1, b1) = xyz1
    (r2, g2, b2) = xyz2
    return (int(r1 + (r2 - r1) * t),
            int(g1 + (g2 - g1) * t),
            int(b1 + (b2 - b1) * t))


def interpolate_hsb(xyz1: ColorTuple, xyz2: ColorTuple, t: float) -> ColorTuple:
    (h1, s1, b1) = xyz1
    (h2, s2, b2) = xyz2
    return (h1 + (h2 - h1) * t, s1 + (s2 - s1) * t, b1 + (b2 - b1) * t)


def rgb_distance(xyz1, xyz2):
    (r1, g1, b1) = xyz1
    (r2, g2, b2) = xyz2
    return int(abs(r1 - r2) + abs(g1 - g2) + abs(b1 - b2))
