import numpy as np
kurva = []
kurvlängdlista = []
rakalängdlista = []
vinkel = [70, 110, 57, 75, 40, 75, 175, 76, 94, 110, 25, 10, 43, 20, 80, 75, 55, 45, 45, 145, 55, 61, 90, 122, 145, 105, 19, 90, 135, 110, 120, 50, 85, 95, 70, 55, 27, 155, 25, 50, 125, 80, 30, 212, 130, 55]
raka = [23, 3, 4, 46, 0, 27, 0, 0, 19.5, 54, 7.4, 7, 0, 17, 15, 0, 52, 0, 28, 15, 48.5, 0, 8, 0, 0, 27, 25, 32, 5, 5, 12, 6, 0, 0, 0, 10.2, 10.5, 6, 8, 14, 12, 5, 19, 11, 66, 0]
with open('testbana.txt', 'r', encoding='utf-8') as file:
    for i, radie in enumerate(file.readline().split()):
        kurvlängd = vinkel[i]/360 * 2*float(radie)*np.pi
        kurva.append(kurvlängd)

rakalängdlista.append(raka[0])

for i in range(len(raka)-1):
        kurvlängdlista.append(rakalängdlista[i] + kurva[i])
        rakalängdlista.append(rakalängdlista[i] + kurva[i] + raka[i+1])
print(f"Kurvlängd: {" ".join(map(str, kurvlängdlista))}", end= " ")
print(f"{rakalängdlista[-1] + kurva[-1]}")
print("\n")
print(f"Rakalängd: {" ".join(map(str, rakalängdlista))}", end= " ")