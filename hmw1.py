# class Student:
#     def __init__(self, name, student_id):
#         self.name = name
#         self.student_id = student_id
#         self.grades = []
#     def add_grade(self, grade):
#             if 0 <= grade <= 100:
#                  self.grades.append(grade)
#             else:
#                  print("Xato: Noto'gri baho")
#     def calculate_average(self):
#         return sum(self.grades) / len(self.grades)
#     def get_status(self):
#         avg = self.calculate_average()
#         if 90 <= avg <= 100:
#             return "A'lo"
#         elif 80 <= avg <= 89:
#             return "Yaxshi"
#         elif 70 <= avg <= 79:
#             return "Qoniqarli"
#         else:
#             return "Qoniqarsiz"
        
# student = Student("Nodira", "S123")

# student.add_grade(85)
# student.add_grade(90)

# print(student.calculate_average())

# print(student.get_status())
# student.add_grade(150)

# ----------------------------------

# class Employee:
#     def __init__(self, name, employee_id, hourly_rate = 15.0):
#         self.name = name
#         self.employee_id = employee_id
#         self.hourly_rate = hourly_rate
#         self.working_hours = []
#     def log_hours(self, hour):
#         if 0 <= hour <= 24:
#             self.working_hours.append(hour)
#             return True
#         return False
#     def total_hours(self):
#         return sum(self.working_hours)
#     def calculate_salary(self):
#         return self.total_hours() * self.hourly_rate
#     def reset_hours(self):
#         self.working_hours.clear()

# employee = Employee("Javlon", "E101", hourly_rate=20.0)

# print(employee.log_hours(8)) 
# print(employee.log_hours(9))
# print(employee.log_hours(10))
# print(employee.log_hours(25))

# print(employee.total_hours())
# print(employee.calculate_salary()) 

# employee.reset_hours()
# print(employee.total_hours())
# print(employee.calculate_salary())  

# ----------------------------------

# class Playlist:
#     def __init__(self, owner):
#         self.owner = owner
#         self.tracks = []
#     def add_track(self, title, artist):
#         self.tracks.append((title, artist))
#     def remove_last(self):
#         if self.tracks:
#             return self.tracks.pop() 
#         return None
#     def total_tracks(self):
#         return len(self.tracks)
#     def unique_tracks(self):
#         st = set()
#         unique_lst = []
#         for i in self.tracks:
#             if i not in st:
#                 st.add(i)
#                 unique_lst.append(i)
#         return unique_lst
#     def search_by_title(self, title):
#         return [i for i in self.tracks if i[0] == title]
#     def filter_by_artist(self, artist):
#         return [i for i in self.tracks if i[1] == artist]

# pl = Playlist("Muhammad")

# print(pl.total_tracks())

# pl.add_track("Yomg'irlar", "Shahzoda")
# pl.add_track("Gulim", "Yulduz Usmonova")
# pl.add_track("Yomg'irlar", "Shahzoda")
# pl.add_track("Xayr edi", "Lola")
# pl.add_track("Kel", "Ulug'bek Rahmatullayev")

# print(pl.total_tracks())

# print(pl.unique_tracks())               

# print(pl.remove_last())

# print(pl.total_tracks())

# print(pl.search_by_title("Yomg'irlar"))       

# print(pl.filter_by_artist("Yulduz Usmonova")) 