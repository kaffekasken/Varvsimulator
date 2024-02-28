data_for_quadratic_equation = []

with open('testfil.txt', 'r', encoding='utf-8') as file:
    for i in file.readline().split():
        data_for_quadratic_equation.append(f"1 {i} {i}^2;")

data = '[' + ', '.join(data_for_quadratic_equation) + ']'

print(data)