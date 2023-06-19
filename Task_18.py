#
# class Teachers:
#     def __init__(self):
#         self.diary = diary
#     def give_task(self):
#     def teach(self, info, *pupil):
#         for i in pupil:
#             i.take(info)
#             self.work += 1
#     def check(self):
# class Pupils:
#     def __init__(self):
#         self.knowledge = []
#     def take(self, info):
#         self.knowledge.append(info)
#
# Exercises= ['Упражнение 1']
# marvanna = Teachers()
# vasy = Pupils()
# pety = Pupils()
# marvanna.teach(lesson[2], vasy, pety)
# marvanna.teach(lesson[0], pety)
# print(vasy.knowledge)
# print(pety.knowledge)
# print(marvanna.work)


class Teacher():
    def __init__(self, name_t):
        self.reses = []
        self.name_t = name_t
        self.list_of_students = []


    def sent_hw(self, task1, *stud):
        for i in stud:
            i.get_hw(task1)


    def take_res(self, results):
        self.reses.append(results)

    def show_res(self):
        print(self.reses)


    def check(self):
        for i in self.reses:
            n = int(input(f"Введите 1 если принято, 0 если нет {i[0]} --> "))
            i.append(n)
        print(self.reses)
        for i in self.reses:
            for j in self.list_of_students:
                for k, v in j.items():
                    if v in i[0]:
                        k.take_res_hw(i)


    def take_lst_stud(self, name):
        self.list_of_students.extend(name)
        print(self.list_of_students)


    def sent_marks(self, *stud, reses):
        for i in reses: pass


class Pupils():
    nam = []

    def __init__(self, name):
        self.name = name
        self.task = []
        self.d = {self: self.name}
        Pupils.nam.append(self.d)
        self.my_res_hw = []


    def get_hw(self, task):
        self.task.append(task)


    def sent_res(self, teach, result_hw):
        teach.take_res([self.name, result_hw])


    def take_res_hw(self, t):
        self.my_res_hw.append(t)


    def show_marks(self):
        print(self.my_res_hw)


tasks = ["Задание №1"]

mar = Teacher("Мария")
vas = Pupils("Вася")
pet = Pupils("Петя")
mar.take_lst_stud(Pupils.nam)

mar.sent_hw(tasks[0], vas, pet)

pet.sent_res(mar, "Отправленно выполнение задания № 1")
vas.sent_res(mar, "Отправленно выполнение задания № 1")
mar.show_res()
mar.check()
vas.show_marks()