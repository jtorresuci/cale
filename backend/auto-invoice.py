class Student:
    def __init__(self, name, weeks_book=None):
        self.name = name
        if weeks_book==None:
            weeks_book = []
        self.weeks_book = weeks_book
        

    def display_info(self):
        print(f"Name: {self.name}")
        if len(self.weeks_book) == 0:
            print("No Weeks")
        else:
            print(f"Weeks Booked {self.weeks_book}")


class WeekBook:
    def __init__(self, week_from, total_number_of_weeks, number_of_hours):
        self.week_from = week_from
        self.total_number_of_weeks = total_number_of_weeks
        self.number_of_hours = number_of_hours


class Week:
    def __init__(self, dates, hours, rate, amount, subtotal):
        self.dates = dates
        self.hours = hours
        self.rate = rate
        self.amount = amount
        self.subtotal = subtotal


class Gas:
    def __init__(self, dates, miles, rate, amount):
        self.dates = dates
        self.miles = miles
        self.rate = rate
        self.amount = amount


def initialize_student():
    name = input("Enter the student's name: ")
    student = Student(name)
    return student

jon_cache = initialize_student()

jon_cache.display_info()




    