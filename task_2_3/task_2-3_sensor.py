oper = input("Оператор: ")
kol_dat = input("Давление: ")
i_f = "sensor_log.txt"
with open(i_f, "w", encoding="utf-8") as fi:
    fi.write(f"{oper.upper()}\t{kol_dat}")
print("Файл успешно сформирован " + i_f+" !")