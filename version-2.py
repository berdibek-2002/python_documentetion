import random

print("******************************************************************************* \n"
      "* Don-don ziki o'yiniga xush kelibsiz! Quyidagi variantlardan birini tanlang. (yakunlash uchun 'stop' yozing!) * \n"
      "*******************************************************************************")


def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Durrang!"
    elif (player_choice == "Tosh" and computer_choice == "Qog'oz") or \
         (player_choice == "Qog'oz" and computer_choice == "Qaychi") or \
         (player_choice == "Qaychi" and computer_choice == "Tosh"):
        return "Yutdingiz! {} ustun {}".format(player_choice, computer_choice)
    else:
        return "Yutqazdingiz! {} yopib qo'ydi {}".format(player_choice, computer_choice)


def play_game():
    tanlov = ["Tosh", "Qog'oz", "Qaychi"]
    comp_hisob = 0
    oyinchi_hisob = 0

    while True:
        oyinchi = input("Tosh, Qog'oz, Qaychi?\n").capitalize()

        if oyinchi == 'Tugat' or oyinchi == "Stop":
            print("Yakuniy hisob:")
            print(f"Computer: {comp_hisob}")
            print(f"O'yinchi: {oyinchi_hisob}")

            if comp_hisob > oyinchi_hisob:
                print("Kompyuter yutdi! Afsus... Yana urinib ko'ring.")
            elif comp_hisob < oyinchi_hisob:
                print("O'yinchi g'olib! Tabriklaymiz!")
            else:
                print("Durrang!")
            break

        if oyinchi not in tanlov:
            print("Noto'g'ri tanlov! Iltimos, Tosh, Qog'oz yoki Qaychi tanlang.")
            continue

        computer = random.choice(tanlov)
        result = determine_winner(oyinchi, computer)

        print(result)

        if "Yutdingiz" in result:
            oyinchi_hisob += 1
        elif "Yutqazdingiz" in result:
            comp_hisob += 1


if __name__ == "__main__":
    play_game()
