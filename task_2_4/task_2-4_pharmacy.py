kol_kaps = int(input("How many kaps do you want? "))
kol_ypak = int(input("сколько капсул в упаковке? "))

print(f"--- Отчет фасовочного цеха ---\nПолных упаковок\t {kol_kaps // kol_ypak}\nОстаток капсул\t {kol_kaps % kol_ypak}")