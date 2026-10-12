weight = float(input("Введите вес (кг): "))
height = float(input("Введите рост (cм): "))/100

bmi = weight / (height ** 2)
print(f"---Отчет о состоянии здоровья---\nРост\t\t{height} см\nВес\t\t\t{weight} кг\nИндекс массы тела пациента: {bmi:.2f}")