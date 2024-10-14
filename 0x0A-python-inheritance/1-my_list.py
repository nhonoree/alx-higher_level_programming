#!usr/bin/ppython3
class MyList(list):
    """Class that inherits from list and has an additional method to print the list sorted."""

    def print_sorted(self):
        """Prints the list, sorted in ascending order."""
        print(sorted(self))
