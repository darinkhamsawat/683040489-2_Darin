"""
Darin Khamsawat
683040489-2
P2
"""

from datetime import datetime
from University import *

print("----Professor----")
prof = Professor(
    "Dr. Somchai", 49, "1976-04-12", "A", True,
    "Physics", 2008, professorship=3, admin_position=1
)
prof.display_info()

print("\n----Administrator----")
admin = Administrator(
    "Cake", 20, "2006-1-20", "O", True,
    "Digital", 2025, admin_position=1
)
admin.display_info()

print("\n----Undergraduated Student----")
ug = UndergraduateStudent(
    "Namfah", 21, "2005-15-08", "O", False,
    2022, "Engineering",
    grade_list=[(3, 'A'), (3, 'B')], club = "ENPhoto"
)
ug.register_course("EN101")
ug.register_course("IC010")
ug.display_info()

print("\n----Graduate Student----")
gs = GraduateStudent(
    "Neo", 26, "1998-09-06", "O", False,
    2024, "Computer Data Science",
    grade_list=[(3, 'A'), (3, 'A')],
    advisor_name= "Dr.Melvin Sona Calixton"
)
gs.set_thesis_name("Student's perception recognization of cannabis")
gs.set_proposal_date(datetime(2025, 6, 1))
gs.display_info()