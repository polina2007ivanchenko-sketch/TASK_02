name_eat =input("Введите название питательной среды: ")
kol_konc = input("введите концентрацию агара(%): ")
tempr_cter = input ("Введите температуру стерилизации(С): ")
with open("recipe.txt", "w", encoding="utf-8") as fi:
    fi.write(f"{name_eat.upper()}\n\nконцентрация агара(%)\t\t{kol_konc}\nтемпература стерилизации(С)\t{tempr_cter}")
print("Файл успешно сформирован!")