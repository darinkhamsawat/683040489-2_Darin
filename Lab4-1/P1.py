""" 
Darin Khamsawat
683040489-2
P1
"""
from cat import Cat
from datetime import timedelta, datetime

cat1 = Cat("Milo", "Persian", 2, "Alice")
cat2 = Cat("Luna", "Siamese", 3, "Bob")
cat3 = Cat("Oliver", "British Shorthair", 1, "Chris")

print(cat1.get_time_in())
cat1.greet()

print(cat2.get_time_out())
cat2.set_time_out(datetime.now() + timedelta(days=2))
print(cat2.get_time_out())

cat3.owner = "David"
cat3.age = 4

cat1.print_cat()
cat2.print_cat()
cat3.print_cat()

print(Cat.get_num())

Cat.reset_cat()

print(Cat.get_num())