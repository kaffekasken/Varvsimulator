data_for_quartic_equation = []
insertingsemicolons = []
data_for_hexic_equation = []

with open('sparadata.txt', 'r', encoding='utf-8') as file:
    for i in file.readline().split():
        #data_for_quartic_equation.append(f"1 {i} {i}^2 {i}^3 {i}^4;")
        #insertingsemicolons.append(f"{i}; ")
        data_for_hexic_equation.append(f"1 {i} {i}^2 {i}^3 {i}^4 {i}^5 {i}^6;")

#data = ''.join(data_for_quartic_equation)
#data = ''.join(insertingsemicolons)
data = ''.join(data_for_hexic_equation)

print(data)

        # OBSERVERA FILSKRIVNING
with open('testfil.txt', 'w', encoding='utf-8') as file:
    file.write(str(data))

#for i in range(21):
#    print(200 + (350-200)*i/20, end=';')