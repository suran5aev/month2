import sqlite3

Connect = sqlite3.connect("Geeks.db")
cursor = Connect.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
               id INT PRIMARY KEY,
               full_name VARCHAR (20) NOT NULL,
               hobby TEXT DEFAULT NUL,
               phone_number INT  NOT NULL +996,
               birth_date DATE,
               mark DOUBLE (7,3) DEFAULT 0.0,
               agreement BOLLEAN FALSE

)                                                                                                                                                                                                                                                                  
               
""")
class Geeks:
    def __init__(self):
        self.full_name = None
        self.hobby = None
        self.phone_number = 0
        self.birth_date = None
        self.mark = 0.0
        self.agreement = False


    def register(self,full_name,hobby,phone_number,birth_date,mark,agreement):
        self.full_name = full_name
        self.hobby = hobby
        self.phone_number = phone_number
        self.birth_date = birth_date

        cursor.execute("""""")
    