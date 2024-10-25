"""Main file for demonstrating functionality."""

from models.rectangle import Rectangle
from models.square import Square

def main():
    """Main function to demonstrate Rectangle and Square."""
    r = Rectangle(4, 5)
    s = Square(3)
    
    print(r)
    print(s)

if __name__ == "__main__":
    main()
