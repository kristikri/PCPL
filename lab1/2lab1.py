import math

def is_float(string):
    try:
        float(string)
        return True
    except:
        return False

def get_coef(prompt):
    coef_str = 'test'
    while is_float(coef_str) == False:
        coef_str = input(prompt)
    coef = float(coef_str)
    return coef

class Solver:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def solve(self):
        D = self.b ** 2 - 4 * self.a * self.c
        if D < 0:
            return []
        elif D == 0:
            x = -self.b/2*self.a
            return [x]
        else:
            x1 = (-self.b + math.sqrt(D)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(D)) / (2 * self.a)
            return [x1, x2]


while(True):
    a = get_coef("Введите коэффициент a: ")
    b = get_coef("Введите коэффициент b: ")
    c = get_coef("Введите коэффициент c: ")

    solver = Solver(a, b, c)
    solutions = solver.solve()
    print("Результаты:")

    if not solutions:
        print("Уравнение не имеет действительных корней")
    elif len(solutions) == 1:
        print(f"Уравнение имеет один корень: {solutions[0]}")
    elif len(solutions) == 2:
        print(f"Уравнение имеет два корня: {solutions[0]} и {solutions[1]}")
    elif len(solutions) == 4:
        print(f"Уравнение имеет четыре корня: {solutions[0]}, {solutions[1]}, {solutions[2]} и {solutions[3]}")
    print("")