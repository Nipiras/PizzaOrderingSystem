# Libraries and Modules
import csv
import datetime
from my_classes import *

# Main Function
with open("Menu.txt", "r") as menu:
  lines = menu.readlines()

# set/dict of valid choices
valid_p_choices = {"p1": p1, "p2": p2, "p3": p3, "p4": p4}

# Welcome text
print("Welcome to Pizza Nipiras"\
      + "\n" +lines[0].strip("* "))

# Pizza lines
for line in lines[1:5]:
  print(line)

while True:
  p_choice = "p" + input("Please enter your pizza number: ")
  if p_choice in valid_p_choices:
    break
  else:
    print("Please choose a value between 1 and 4!")

# 6th line
print(lines[5].strip("* "))

# Ingredient lines
for line in lines[6:12]:
  print(line)

while True:
  s_choice = "s" + input("Please enter your additional ingredient number: ")
  if s_choice == "s11":
    selected_pizza = Olive(valid_p_choices[p_choice])
    break
  elif s_choice == "s12":
    selected_pizza = Mushroom(valid_p_choices[p_choice])
    break
  elif s_choice == "s13":
    selected_pizza = Mozarella(valid_p_choices[p_choice])
    break
  elif s_choice == "s14":
    selected_pizza = Oregano(valid_p_choices[p_choice])
    break
  elif s_choice == "s15":
    selected_pizza = SalameNapoli(valid_p_choices[p_choice])
    break
  elif s_choice == "s16":
    selected_pizza = Tomato(valid_p_choices[p_choice])
    break
  else:
    print("Please choose a value between 11 and 16!\n")  

print(f"""\nYour order: {selected_pizza.get_description()}
The price of your pizza: {selected_pizza.get_cost()} Eu
Please enter your information for the payment process.\n""")
# -Unique value
while True:
  email = input("E-mail address: ").lower()
  if len(email) >= 11 and "@" in email:
    break
  else:
    print("\nPlease enter a valid e-mail address! ")
while True:
  name = input("Name: ").capitalize()
  if len(name) >= 3:
    break
  else:
    print("\nPlease make sure you enter your name correctly! ")
while True:
  surname = input("Surname: ").capitalize()
  if len(surname) >= 3:
    break
  else:
    print("\nPlease make sure you enter your surname correctly! ")
# -Unique value
while True:
  card_id = input("Credit Card Number: ").replace(" ", "")
  if len(card_id) == 16 and card_id.isdigit():
    break
  else:
    print("""\nPlease re-enter your 16-digit card number,
    which consists only of numbers! """)
while True:
  card_cvc = input("CVC: ")
  if len(card_cvc) == 3 and card_cvc.isdigit():
    order_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    break
  else:
    print("""\nPlease re-enter your 3-digit security code
    on the back of your card! """)

# Thank you text
print("""\nYour order will be delivered to your address
as soon as possible...
Thank you for choosing us.,\n""" +
lines[12].strip("* "))

# Order information
order = [email, name, surname, card_id, card_cvc, \
         selected_pizza.get_description(), \
         selected_pizza.get_cost(), order_time]

# csv file
with open('Orders_Database.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["email", "name", "surname", "card_id", \
                     "card_cvc", "order_descr", "order_cost", "order_time"])
    writer.writerow(order)

input("\nPress the 'Enter' key to close the program.")