import os, random, time

intro = """
Witaj w grze papier-nozyce-kamien.
1 - Papier
2 - Nozyce
3 - Kamien
0 - Koniec gry
"""

possible_moves = {1: "Papier", 2: "Nozyce", 3: "Kamien"}

play = True

# tutaj bedziemy powtarzac petle z gra do czasu az uzytkownik wybierze 0
while play:
    # czyscimy ekran
    # to komenda dla windowsa os.system("cls")
    os.system("clear")
    print(intro)
    a = int(input("Wybierz swoj ruch (0-3):"))
    if a == 0:
        print("papa, dzieki za gre")
        # break w tym miejscu przerywa petle while
        break
    elif a > 0 and a < 4:
        your_move = a
        computer_move = random.choice((1, 2, 3))
        print("Wybrales:", possible_moves.get(your_move))
        print("Komputer wylosowal:", possible_moves.get(computer_move))
        if (your_move == computer_move):
            print("Mamy remis")
        elif (your_move == 1 and computer_move == 2) or (your_move == 2 and computer_move == 3) or (
                your_move == 3 and computer_move == 1):
            print("Komputer wygral")
        else:
            print("Wygrałes z komputerem")
    else:
        print("Przegrales - zagraj jeszcze raz.")
    # dajmy pauze na 4 sekundy zeby przeczytac wynik gry
    time.sleep(4)
