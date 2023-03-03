# -*- coding: utf-8 -*-

#@title Libraries and Modules
import csv
import datetime
from my_classes import *

#@title Main Function
with open("Menu.txt", "r", encoding="utf-8") as menu:
  lines = menu.readlines()

# set/dict of valid choices
valid_p_choices = {"p1": p1, "p2": p2, "p3": p3, "p4": p4}
valid_s_choices = {"s11", "s12", "s13", "s14", "s15", "s16"}

# Welcome text
print("Pizza Nipiras'a Hoş geldiniz"\
      + "\n" +lines[0].strip("* "))

# Pizza lines
for line in lines[1:5]:
  print(line)

while True:
  p_choice = "p" + input("Pizzanızın numarasını giriniz: ")
  if p_choice in valid_p_choices:
    break
  else:
    print("Lütfen 1 ve 4 arasında bir değer seçiniz!")

# 6th line
print(lines[5].strip("* "))

# Ingredient lines
for line in lines[6:12]:
  print(line)

while True:
  s_choice = "s" + input("Sosunuzun numarasını giriniz: ")
  if s_choice == "s11":
    selected_pizza = Zeytin(valid_p_choices[p_choice])
    break
  if s_choice == "s12":
    selected_pizza = Mantar(valid_p_choices[p_choice])
    break
  if s_choice == "s13":
    selected_pizza = Peynir(valid_p_choices[p_choice])
    break
  if s_choice == "s14":
    selected_pizza = Et(valid_p_choices[p_choice])
    break
  if s_choice == "s15":
    selected_pizza = Sogan(valid_p_choices[p_choice])
    break
  if s_choice == "s16":
    selected_pizza = Misir(valid_p_choices[p_choice])
    break
  else:
    print("Lütfen 11 ve 16 arasında bir değer seçiniz!\n")  

print(f"""\nSeçiminiz: {selected_pizza.get_description()}
Ödemeniz gereken tutar: {selected_pizza.get_cost()}TL
Ödeme işlemi için lütfen bilgilerinizi giriniz.\n""")
# -Unique value
while True:
  tc_id = input("T.C. kimlik numaranız: ").replace(" ", "")
  if len(tc_id) == 11 and tc_id.isdigit():
    break
  else:
    print("""\nLütfen sadece rakamlardan oluşan
11 haneli T.C. kimlik numaranızı yeniden giriniz! """)
while True:
  name = input("Adınız: ").capitalize()
  if len(name) >= 3:
    break
  else:
    print("""\nLütfen adınızı doğru yazdığınıza emin olun! """)
while True:
  surname = input("Soyadınız: ").capitalize()
  if len(surname) >= 3:
    break
  else:
    print("""\nLütfen soyadınızı doğru yazdığınıza emin olun! """)
# -Unique value
while True:
  card_id = input("Kredi kartı numaranız: ").replace(" ", "")
  if len(card_id) == 16 and card_id.isdigit():
    break
  else:
    print("""\nLütfen sadece rakamlardan oluşan
16 haneli kart numaranızı yeniden giriniz! """)
while True:
  card_pwd = input("Kredi kartı şifreniz: ")
  if len(card_pwd) == 6:
    order_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    break
  else:
    print("""\nLütfen 6 haneli şifrenizi
yeniden giriniz! """)

# Thank you text
print("""\nSiparişiniz en kısa zamanda
adresinize teslim edilecektir...
Bizi tercih ettiğiniz için,\n""" +
lines[12].strip("* "))

# Order information
order = [tc_id, name, surname, card_id, card_pwd, \
         selected_pizza.get_description(), \
         selected_pizza.get_cost(), order_time]

# csv file
with open('Orders_Database.csv', 'w', encoding="utf-8", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["tc_id", "name", "surname", "card_id", \
                     "card_pwd", "order_descr", "order_cost", "order_time"])
    writer.writerow(order)

