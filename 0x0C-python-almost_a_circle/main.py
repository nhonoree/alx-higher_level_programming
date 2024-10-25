from rectangle import Rectangle
from square import Square

def main():
    r1 = Rectangle(3, 4)
    r2 = Rectangle(5, 6)
    s1 = Square(7)

    print(r1.to_dictionary())  # Example usage
    print(s1.to_dictionary())   # Example usage

    Rectangle.save_to_file([r1, r2])
    Square.save_to_file([s1])

    r_list = Rectangle.load_from_file()
    s_list = Square.load_from_file()

    print(r_list)  # Should print loaded rectangles
    print(s_list)  # Should print loaded squares

if __name__ == "__main__":
    main()
