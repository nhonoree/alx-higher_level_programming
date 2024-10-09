#!/usr/bin/python3
Rectangle = __import__('2-rectangle').Rectangle

myrectangle = Rectangle(2, 4)
print("{} - {} => {}".format(myrectangle.width, myrectangle.height, myrectangle.area()))

myrectangle = Rectangle(2, 4)
print("{} - {} => {}".format(myrectangle.width, myrectangle.height, myrectangle.perimeter()))

myrectangle = Rectangle(10, 10)
print("{} - {} => {} / {}".format(myrectangle.width, myrectangle.height, myrectangle.area(), myrectangle.perimeter()))

myrectangle = Rectangle(10)
print("{} - {} => {} / {}".format(myrectangle.width, myrectangle.height, myrectangle.area(), myrectangle.perimeter()))

myrectangle = Rectangle()
print("{} - {} => {} / {}".format(myrectangle.width, myrectangle.height, myrectangle.area(), myrectangle.perimeter()))
