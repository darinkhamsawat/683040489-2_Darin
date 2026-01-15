"""
Darin Khamsawat
683040489-2
P1
"""
from abc import ABC, abstractmethod

class Room(ABC):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @abstractmethod
    def get_purpose(self):
        """Returns a string describing purposes of the room"""
        pass

    @abstractmethod
    def get_recommended_lighting(self):
        """Returns recommended lighting in lumens per square foot"""
        pass

    def calculate_area(self):
        return self.length * self.width

    def describe_room(self):
        area = self.calculate_area()
        return f"A {self.__class__.__name__} of {area} sq ft used for {self.get_purpose()}"


class Bedroom(Room):
    def __init__(self, length, width, bed_size):
        super().__init__(length, width)
        self.bed_size = bed_size  # in feet

    def get_purpose(self):
        return "sleeping and resting"

    def get_recommended_lighting(self):
        # Typical bedroom lighting
        return 10  # lumens per square foot


class Kitchen(Room):
    def __init__(self, length, width, has_island=True):
        super().__init__(length, width)
        self.has_island = has_island

    def get_purpose(self):
        return "cooking and food preparation"

    def get_recommended_lighting(self):
        return 30  

    def calculate_counter_space(self):
        """
        Docstring for calculate_counter_space

        Args:
           No argument

        Returns:
           float: the area of island counter 
           float: the aread of wall counter

        Raises:
           Nothing

        Example:
           >>> obj.calculate_counter_space()
           (12.0,15.0)
        """
  
        area = self.calculate_area()

        if self.has_island == True:
            island_counter =  area /5
            wall_counter =  area /4
        else:
            island_counter = 0
            wall_counter =  area /2

        return island_counter, wall_counter