import heapq

class Group:

    def __init__(self):
        self.instances = []
        self.groupsize = 0

    def addstud(self, newstud):
        self.instances.append(newstud)
        self.groupsize += 1

    def topfive(self, rank_place):
        all_averages = []
        for stud in self.instances:
            all_averages.append(stud.average)
        all_averages = heapq.nlargest(5, all_averages)
        for stud in self.instances:
            if (stud.average == all_averages[rank_place]):
                return stud.surname, stud.name, stud.average, stud.number

    def display_top(self):
        if (self.groupsize > 5):
            print("\nFive best students:\n")
            for i in range(0, 5):
                print(self.topfive(i))
        elif (self.groupsize <= 5 and self.groupsize > 0):
            print("\nAll students ranked by average score:\n")
            for i in range(0, self.groupsize):
                print(self.topfive(i))
        else:
            print("\nThe group is currently empty\n")


class Student():
    name = None
    surname = None
    number = None
    grades = []
    average = None

    def __init__(self, n, sur, num, gr):
        self.name = n
        self.surname = sur
        self.number = num
        self.grades = gr
        self.calc_average()

    def calc_average(self):
        sum = 0
        for i in self.grades:
            sum += i
        self.average = sum / len(self.grades)

if __name__ == '__main__':
    tv_twelve_thousand = Group()
    a1 = Student("Anton", "Antonenko", "TV-1299", [92, 80, 80, 96])
    tv_twelve_thousand.addstud(a1)
    a2 = Student("Artem", "Boyko", "TV-1298", [64, 72, 70, 90])
    tv_twelve_thousand.addstud(a2)
    a3 = Student("Ihor", "Melnyk", "TV-1242", [100, 100, 100, 100])
    tv_twelve_thousand.addstud(a3)
    a4 = Student("Petro", "Petrenko", "TV-1297", [83, 84, 93, 91])
    tv_twelve_thousand.addstud(a4)
    a5 = Student("Volodymyr", "Hordienko", "TV-1296", [70, 79, 90, 97])
    tv_twelve_thousand.addstud(a5)
    a6 = Student("Ivan", "Shevchenko", "TV-1295", [94, 95, 91, 89])
    tv_twelve_thousand.addstud(a6)
    a7 = Student("Denys", "Taranenko", "TV-1294", [83, 76, 89, 67])
    tv_twelve_thousand.addstud(a7)
    a8 = Student("Spyrydon", "Spyrydonenko", "TV-1293", [63, 64, 61, 66])
    tv_twelve_thousand.addstud(a8)
    tv_twelve_thousand.display_top()