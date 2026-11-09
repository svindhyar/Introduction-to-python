class student:
    def __init__(self, name):
        self.name = name
        self.grades = []
    def add_grade(self, g):
        self.grades.append(g)
    def compute_average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

ana = student("Ana")
for g in [90, 80, 70]:
    ana.add_grade(g)
ben = student("Ben")
print(ana.name, ana.compute_average())
print(ben.name, ben.compute_average())