# PizzaOrderingSystem
 Object Oriented Programming exercise

# Genel Bakış
Bu program, [programın amacını buraya yazın örn: This is a sample project demonstrating how to deploy machine learning models using FastAPI and Streamlit. The project contains a web interface built using Streamlit where users can input data and get predictions from different machine learning models. The predictions are made by a FastAPI app which serves the machine learning models as APIs.].

# Gereksinimler
Bu programın çalışması için gerekenler:

Python [sürüm numarası]
[Diğer gereksinimler, modüller vs.]

# Kurulum
Bu depoyu bilgisayarınıza indirin veya kopyalayın
Gereksinimleri yükleyin: pip install -r requirements.txt
Programı çalıştırın: python program.py

# Kullanım
[Programın kullanımı hakkında bilgi verin. Örnek olarak programın nasıl çalıştırılacağı, hangi parametrelerin verilmesi gerektiği, nasıl kullanılacağı vs. gibi konularda açıklama yapabilirsiniz.]

# Project structure
The project has the following structure:

```program/
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



# Usage

To run the project, first install the dependencies:

```pip install -r requirements.txt```
Then, start the FastAPI app:
```cd app
uvicorn main:app --reload
```

The API documentation can be accessed at http://localhost:8000/docs.

Finally, start the Streamlit app:

```streamlit run streamlit_app/main.py```
The web interface can be accessed at http://localhost:8501.
Contributing
Contributions are welcome! If you find any issues or want to add a new feature, please open an issue or submit a pull request.
License
This project is licensed under the MIT License - see the LICENSE.md file for details.
