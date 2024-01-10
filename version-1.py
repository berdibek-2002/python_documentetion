import random
tanlov = ["Tosh", "Qog'oz", "Qaychi"]
oyinchi = False
comp_hisob = 0
oyinchi_hisob = 0
print(" *******************************************************************************\n",
      "* Don-don ziki o'yiniga xush kelibsiz! Quyidagi variantlardan birini tanlang. *\n",
      "*******************************************************************************")
while True:
    oyinchi = input("Tosh, Qog'oz, Qaychi?\n").capitalize()
    computer = random.choice(tanlov)
    if oyinchi == computer:
        print("Durrang!")
        comp_hisob+=1
        oyinchi_hisob+=1
    elif oyinchi == "Tosh":
        if computer == "Qog'oz":
            print("Yutqazdingiz!", computer, " yopdi ", oyinchi, "ni")
            comp_hisob+=1
        else:
            print("Yutdingiz!", oyinchi, " ustun ", computer, "dan")
            oyinchi_hisob+=1
    elif oyinchi == "Qog'oz":
        if computer == "Qaychi":
            print("Yutqazdingiz!", computer, " kesdi ", oyinchi, "ni")
            comp_hisob+=1
        else:
            print("Yutdingiz!", oyinchi, "yopib qo'ydi ", computer, "ni")
            oyinchi_hisob+=1
    elif oyinchi == "Qaychi":
        if computer == "Tosh":
            print("Yutqazdingiz...", computer, " sindirdi ", oyinchi, "ni")
            comp_hisob+=1
        else:
            print("Yutdingiz!", oyinchi, "kesdi", computer, "ni")
            oyinchi_hisob+=1
    elif oyinchi=='Tugat' or oyinchi=="Stop":
        print("Yakuniy hisob: \n")
        print(f"Computer:{comp_hisob}")
        print(f"O'yinchi:{oyinchi_hisob}")
        if comp_hisob>oyinchi_hisob:
            print("Kompyuter yutdi! Afsus... Yana urinib ko'ring.")
        elif comp_hisob<oyinchi_hisob:
            print("O'yinchi g'olib! Tabriklaymiz!")
        else:
            print("Durrang!")
        break
