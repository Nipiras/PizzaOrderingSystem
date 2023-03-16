# Pizza Ordering System [OOP]
Hands-on project of Object Oriented Programming exercise on Python

# Overview
The project aims for users to design their own pizza and add the user's information to the database after payment.

- The Pizza Ordering System starts with the users choosing the pizza on the menu and the ingredients they want. 
After selecting the ingredient and pizza, user information must be entered for payment.

   ### The Project Task
      Importing Required Libraries

      Using the menu in the "menu.txt" file

      Create superclass “Pizza”
      - Define the Pizza class and the `get_description()` and `get_cost()` methods for encapsulation within that class.
          - This description should be a short description of the pizza being prepared!

      Create pizza subclasses
      - Create subclasses for pizzas on the menu.
          - Each pizza should have its own price and description.

      Create class “Decorator”
      - This class should be the super class of ingredient classes.
      - This class will use the `get_description()` and `get_cost()` methods using the properties of the Pizza class. 
      Complete the decorator class using the following methods.

           ---
          def get_cost(self):
           return self.component.get_cost() + Pizza.get_cost(self)

          def get_description(self):
           return self.component.get_description() + ' ' + Pizza.get_description(self)
           ---

      - Create subclasses for ingredients on the menu.
           - Each ingredient should have its own price and description.
           
      Create a main function. 
      - This function will print the menu first. It will then allow the user to select a pizza and toppings from the menu. 
      After calculating the total price of the selected products, the user should receive:
      the name, surname, TR ID number, credit card number and credit card password information.
      - The collected data and the user's order time should be recorded here in the "Orders_Database.csv" file.

# Requirements
Requirements for this program to work:

    Python 3.9.12
    csv
    datetime
    my_classes

# Setup & Usage
Initially download or copy this repository to your computer

Install requirements: `pip install -r requirements.txt`

Run the program: `PizzaOrderingSystem_OOP.py`

# Project structure
The project has the following structure:

```
program/
|-- __pycache__/
|   |-- module.cpython-39.pyc
|-- module.py
|-- Menu.txt
|-- Orders_Database.csv
|-- program.py
|-- README.md
|-- requirements.txt

 ```

•	`__pycache__/`: Python tarafından otomatik olarak oluşturulmuş derlenmiş dosyaların bulunduğu klasör

•	`module.py`: Programda kullanılan modül dosyası

•	`Menu.txt`: Programın menüsü

•	`Orders_Database.csv`: Sipariş bilgilerinin kaydedildiği dosya

•	`program.py`: Ana program dosyası

•	`README.md`: Bu dosya, program hakkında genel bilgiler içeren kullanım kılavuzu


# Contributing
Contributions are welcome! If you find any issues or want to add a new feature, please open an issue or submit a pull request. 

Thank you in advance for your contributions.
