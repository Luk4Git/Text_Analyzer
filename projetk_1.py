"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Lukáš Matela
email: lukas.matela@innogy.cz, Lukas.Matela@gmail.com
discord: Lukáš M., Lukáš#8477
"""

#Anylyzovaný text
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.
''']

#Vyžádá si od uživatele přihlašovací jméno a heslo a ověří shodu dle slovníku users
#Špatná kombinace přihlašovacího jména a hesla ukončí program.
separator = "----------------------------------------"
users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
username = input("Username: ")
password = input("Password: ")

if users.get(username) == password:
    print(f"{separator} \n"
          f"Welcome to the app {username}! \n"
          f"We have 3 texts to be analyzed.\n"
          f"{separator}")
else:
    print("unregistered user, terminating the program..")
    quit()

#Výběr textu pomocí čísla
choice_text = input(f"Enter a number btw. 1 and 3 to select: ")
number_t = int(choice_text)-1

#Ukončení programu při špatné volbě
if int(choice_text) not in [1, 2, 3]:
    print("Wrong choice, terminating the program..")

#Počet čísel a číslíc
words_cut=TEXTS[number_t].split()
words_sum = int()
numbers_sum = int()

for word in words_cut:
    if isinstance(word, str) and not word.isnumeric():
       words_sum += 1
    else:
        numbers_sum +=1

#Soucet čisel (ne cifer)
sum_digit=0
for number in words_cut:
    if number.isdigit() == True:
        sum_mid = int(number)
        sum_digit= sum_digit + sum_mid

#Počet slov psaných velkými písmeny a počet slov psaných malými
uppercase_sum=0
lowercase_sum=0

for i in words_cut:
      if(i.islower()):
            lowercase_sum=lowercase_sum+1
      elif(i.isupper()):
            uppercase_sum=uppercase_sum+1

#Počet slov kde je na začátku velke pismeno
titlecase_sum = 0

for b in words_cut:
    if b.istitle() == True:
        titlecase_sum = titlecase_sum + 1

#Počitadlo délek slov
lenword1_sum = 0
lenword2_sum = 0
lenword3_sum = 0
lenword4_sum = 0
lenword5_sum = 0
lenword5_sum = 0
lenword6_sum = 0
lenword7_sum = 0
lenword8_sum = 0
lenword9_sum = 0
lenword10_sum = 0
lenword11_sum = 0


for word_length in words_cut:
    if word_length.isdigit() == False and len(word_length) == 1:
        lenword1_sum += 1
        stars1= lenword1_sum * '*'
    if word_length.isdigit() == False and len(word_length) == 2:
        lenword2_sum += 1
        stars2 = lenword2_sum * '*'
    if word_length.isdigit() == False and len(word_length) == 3:
        lenword3_sum += 1
        stars3 = lenword3_sum * '*'
    if word_length.isdigit() == False and len(word_length) == 4:
        lenword4_sum += 1
        stars4 = lenword4_sum * '*'
    if word_length.isdigit() == False and len(word_length) == 5:
        lenword5_sum += 1
        stars5 = lenword5_sum * '*'
    if word_length.isdigit() == False and len(word_length) == 6:
        lenword6_sum += 1
        stars6 = lenword6_sum * '*'
    if word_length.isdigit() == False and len(word_length) == 7:
        lenword7_sum += 1
        stars7 = lenword7_sum * '*'
    if word_length.isdigit() == False and len(word_length) == 8:
        lenword8_sum += 1
        stars8 = lenword8_sum * '*'
    if word_length.isdigit() == False and len(word_length) == 9:
        lenword9_sum += 1
        stars9 = lenword9_sum * '*'
    if word_length.isdigit() == False and len(word_length) == 10:
        lenword10_sum += 1
        stars10 = lenword10_sum * '*'
    if word_length.isdigit() == False and len(word_length) == 11:
        lenword11_sum += 1
        stars11 = lenword11_sum * '*'

#Zobrazení výsledků
print(f"{separator} \n"
      f"There are {words_sum} words in the selected text.\n"
      f"There are {titlecase_sum} titlecase words.\n"
      f"There are {uppercase_sum} uppercase words.\n"
      f"There are {lowercase_sum} lowercase words.\n"
      f"There are {numbers_sum} numeric strings.\n"
      f"The sum of all the numbers {sum_digit}.\n"
      f"{separator} \n"
      f"LEN|  OCCURENCES  |NR.\n"
      f"{separator} \n"
      f"1\t|{stars1}\t\t|{lenword1_sum}\n"
      f"2\t|{stars2}\t\t|{lenword2_sum}\n"
      f"3\t|{stars3}\t\t|{lenword3_sum}\n"
      f"4\t|{stars4}\t\t|{lenword4_sum}\n"
      f"5\t|{stars5}\t\t|{lenword5_sum}\n"
      f"6\t|{stars6}\t\t|{lenword6_sum}\n"
      f"7\t|{stars7}\t\t|{lenword7_sum}\n"
      f"8\t|{stars8}\t\t|{lenword8_sum}\n"
      f"9\t|{stars9}\t\t|{lenword9_sum}\n"
      f"10\t|{stars10}\t\t|{lenword10_sum}\n"
      f"11\t|{stars11}\t\t|{lenword11_sum}\n"
      )