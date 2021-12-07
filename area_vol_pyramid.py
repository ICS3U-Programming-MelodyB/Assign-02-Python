#!/usr/bin/env python3
# Created by: Melody Berhane
# Created on: Dec 4, 2021
# This program asks the user for the unit, length, height and
# width of the pyramid. It then
# calculates and displays the surface area and
# volume.
import math


def main():
    # input
    print("Today we will calculate the surface area and")
    print("volume of a pyramid")
    unit = (input("\033[1;35;38mEnter the units:"))
    length = float(input("\033[1;35;38mEnter the length:"))
    width = float(input("\033[1;35;38mEnter the width:"))
    height = float(input("\033[1;35;38mEnter the height:"))

    # process
    base_area = length * width
    slant_area = length * (math.sqrt((width/2)**2 + height**2))
    side_area = width * (math.sqrt((length/2)**2 + height**2))
    surface_area = base_area + side_area + slant_area
    volume = (length * width * height)/3

    # output
    print("")
    print("\033[1;32;38mSurface Area ={:.2f} {}^2". format(surface_area, unit))
    print("\033[1;32;38mVolume ={:.2f} {}^3". format(volume, unit))


if __name__ == "__main__":
    main()
