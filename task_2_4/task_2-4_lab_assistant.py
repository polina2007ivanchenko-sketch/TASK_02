volume = float(input("Объем раствора (в мл): "))
salt_mass = volume * 0.009
with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
    file.write("------------------------:\n")
    file.write(f"Общий объем:\t{round(volume,2)}\tмл\n")
    file.write(f"Масса соли:\t{round(salt_mass,2)}\tг\n")
    file.write(f"Объем воды:\t{round(volume,2)}\tмл\n")