phenotype_D = input("Введите фенотип группы крови донора (I, II, III, IV): ").strip().upper()
phenotype_R = input("Введите фенотип группы крови   пациета (реципиента)  (I, II, III, IV): ").strip().upper()
if phenotype_D == "I":
    print("Группа крови: 0 (I)- можно переливать рецепиенту ")
elif phenotype_D == "II" :
    if phenotype_R == "IV" or phenotype_R == "II":
        print("Группа крови: A (II) - можно переливать")
    else:
        print("Переливать нельзя")
elif phenotype_D == "III":
    if phenotype_R == "IV" or phenotype_R == "III":
        print("Группа крови: B (III) - переливать можно")
    else:
        print("Переливать нельзя")
elif phenotype_D == "IV":
    if phenotype_R == "IV" or phenotype_R == "II":
        print("Группа крови: A (IV) - можно переливать")
    else:
        print("Переливать нельзя")

