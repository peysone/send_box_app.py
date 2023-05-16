"""
Napisz program do obsługi ładowarki paczek.
Po uruchomieniu, aplikacja pyta ile paczek chcesz wysłać,
a następnie wymaga podania wagi dla każdej z nich.

Na koniec działania program powinien wyświetlić w podsumowaniu:

Liczbę paczek wysłanych
Liczbę kilogramów wysłanych
Suma "pustych" - kilogramów (brak optymalnego pakowania). Liczba paczek * 20 - liczba kilogramów wysłanych
Która paczka miała najwięcej "pustych" kilogramów, jaki to był wynik

Restrykcje:

Waga elementów musi być z przedziału od 1 do 10 kg.
Każda paczka może maksymalnie zmieścić 20 kilogramów towaru.
W przypadku, jeżeli dodawany element przekroczy wagę towaru, ma zostać dodany do nowej paczki, a obecna wysłana.
W przypadku podania wagi elementu mniejszej od 1kg lub większej od 10kg,
dodawanie paczek zostaje zakończone i wszystkie paczki są wysłane. Wyświetlane jest podsumowanie.

Przykład 1:

Ilość elementów: 2
Wagi elementów: 7, 9
Podsumowanie:

Wysłano 1 paczkę (7+9)
Wysłano 16 kg
Suma pustych kilogramów: 4kg
Najwięcej pustych kilogramów ma paczka 1 (4kg)

Przykład 2:

 Ilość elementów: 6
Wagi elementów: 3, 6, 5, 8, 2, 3
Podsumowanie:

Wysłano 2 paczki (3+6+5, 8+2+3)
Wysłano 27 kg
Suma pustych kilogramów: 13kg
Najwięcej pustych kilogramów ma paczka 2 (7kg)

Przykład 3:
 Ilość elementów: 8

Wagi elementów: 7, 14
 Podsumowanie:
Wysłano 1 paczkę (7)
Wysłano 7 kg
Suma pustych kilogramów: 13kg
Najwięcej pustych kilogramów ma paczka 13

"""

# Po uruchomieniu, aplikacja pyta ile paczek chcesz wysłać, a następnie wymaga podania wagi dla każdej z nich.
# Na koniec działania program powinien wyświetlić w podsumowaniu:
# Liczbę paczek wysłanych
# Liczbę kilogramów wysłanych
# Suma "pustych" - kilogramów
# max 20 kg

# TODO : zmienne, logika, działania


#quantity - ilość paczek

quantity = int(input("ile paczek chcesz wysłać? "))
print(f"Twoja liczba paczek to: {quantity}")
# box - pojemnik na paczke
box = 0
# box_count - ilość paczek wysłanych
box_count = 0
# box_weighr waga paczek
box_weight = 0
# light_box - kontener na zliczanie "pustych kg"
light_box_idx = 0
light_box = 0

for idx in range(1, quantity+1):
    input_weight_box = int(input("podaj wagę elementu: "))
    if input_weight_box < 1 or input_weight_box > 10:
        print("zła waga elementu")
        break
    box += input_weight_box
    box_weight += input_weight_box

    if box > 20:
        box_count += 1
        empty_space = 20 - (box - input_weight_box)
        if empty_space > light_box:
            light_box_idx = box_count
            light_box = empty_space
        box = 0
        box += input_weight_box
        print("paczka wysłana!")

if box > 0:
    box_count += 1
    empty_space = 20 - box
    if empty_space > light_box:
        light_box_idx = box_count
        light_box = empty_space
    print("paczka wysłana!")

print(f"Liczba wysłanych paczek: {box_count}")
print(f"najwięcej pustych kilogramów ma paczka: {light_box_idx} ({light_box} kg)")
print(f"najlżejsza paczka waży: {box}kg")



# print(" podaj wagę każdej paczki \n"
#                      " (paczki mogą ważyć od 1 do 10 kg)")
# #MAXWEIGHTINPKG - max suma kg w paczce
# MAXWEIGHTINPKG = 20
# # pkg - waga paczki
# # pkg weight - waga paczek podanych przez usera
# pkg = 0
# weight = 0
# for pkg in range(quantity):
#     pkg_weight = int(input())
#
#
# while weight >= MAXWEIGHTINPKG:
#     pkg_weight += weight
#     if weight > MAXWEIGHTINPKG:
#         weight - MAXWEIGHTINPKG
#         print(weight)
#
#
#
#
