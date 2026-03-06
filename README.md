# CSV to MySQL using Python

This project demonstrates how to upload data from a CSV file into a MySQL database using Python.

## 📌 Technologies Used
- Python
- Pandas
- SQLAlchemy
- PyMySQL
- MySQL

## 📂 Project Description
The project reads data from a CSV file using the Pandas library and inserts it into a MySQL table using SQLAlchemy. It shows how Python can interact with databases for data storage and management.

## ⚙️ Steps
1. Install required libraries
   pip install pandas sqlalchemy pymysql ipython-sql

2. Create a MySQL database.

3. Connect Python to MySQL using SQLAlchemy.

4. Load the CSV file using Pandas.

5. Insert the data into the MySQL table using `to_sql()`.

## 🚀 Example Code
```python
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("mysql+pymysql://root:password@localhost:3306/project2")

df = pd.read_csv("sample.csv")
df.to_sql("emp", con=engine, if_exists="append", index=False)