"""
Darin Khamsawat
683040489-2
P1
"""
from room import Bedroom, Kitchen

print("---- Bedroom Test ----")
bedroom = Bedroom(12, 10, 5)
print(bedroom.describe_room())
print("Area:", bedroom.calculate_area(), "sq ft")
print("Bed size:", bedroom.bed_size, "ft")
print("Recommended lighting:", bedroom.get_recommended_lighting(), "lumens/sq ft")

print("\n---- Kitchen Test (with island) ----")
kitchen1 = Kitchen(15, 12)
print(kitchen1.describe_room())
print("Area:", kitchen1.calculate_area(), "sq ft")
print("Recommended lighting:", kitchen1.get_recommended_lighting(), "lumens/sq ft")
island, wall = kitchen1.calculate_counter_space()
print("Island counter area:", island, "sq ft")
print("Wall counter area:", wall, "sq ft")

print("\n---- Kitchen Test (no island) ----")
kitchen2 = Kitchen(15, 12, has_island=False)
print(kitchen2.describe_room())
island, wall = kitchen2.calculate_counter_space()
print("Island counter area:", island, "sq ft")
print("Wall counter area:", wall, "sq ft")
