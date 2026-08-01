"""Write a monitor class definition"""

class Monitor:
    """Represent a computer monitor"""

    def __init__(self, model: str, width: int, height: int):
        """Initialise the Monitor with mode, width, height"""
        self.model = model
        self.width = width
        self.height = height


    def get_resolution(self) -> tuple:
        """Get the resolution of the monitor"""
        return self.width, self.height

    def get_total_pixels(self) -> int:
        """Get total number of pixels pn the monitor"""
        return self.width * self.height


    def __eq__(self, other) -> bool:
        """Compare if two Monitor objects are equal based on their width and height."""
        return self.width == other.width and self.height == other.height


    def __ne__(self, other) -> bool:
        """Compare if two monitor objects are not equal based on their width and height."""
        return not self == other



def run_tests():
    # Example usage and tests:
    monitor1 = Monitor("Dell UltraSharp", 1920, 1080)
    monitor1b = Monitor("Dell UltraSharp", 1920, 1080)
    monitor2 = Monitor("HP EliteDisplay", 1920, 1080)
    monitor3 = Monitor("Acer Predator", 2560, 1440)

    print(monitor1.get_resolution())  # Output: (1920, 1080)
    print(monitor1.get_total_pixels())  # Output: 20733600

    assert monitor1 == monitor1b # THIS WOULD BE ASSERTION ERROR
    # because in memory even if same values, they are different objects

    # Test 1: Comparing two monitors with the same resolution
    print(monitor1 == monitor2)  # Output: True
    assert monitor1 == monitor2
    # Test 2: Comparing two monitors with different resolution
    print(monitor1 == monitor3)  # Output: False
    assert not monitor1 == monitor3

    assert monitor1 != monitor3
    assert not monitor1 != monitor2

run_tests()
#
# BoxLayout:
# #    orientation: 'vertical'
#      orientation: 'horizontal'
#      BpxLayout:
#         orientation: 'vertical'
# #