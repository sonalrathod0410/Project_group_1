import sqlite3
import csv

def create_database(database_name):
    conn = sqlite3.connect(database_name)
    conn.close

def create_table():
   
    conn = sqlite3.connect('Health_database.db')    
    cur = conn.cursor()   
    cur.execute('''CREATE TABLE IF NOT EXISTS sleep_cycle
                (Person_ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                Gender TEXT ,
                Age INTEGER,
                Occupation TEXT, 
                Sleep_Duration DECIMAL,
                 Quality_of_Sleep INTEGER, 
                Physical_Activity_level INTEGER,
                 Stress_Level INTEGER, 
                BMI_Category TEXT,Blood_Pressure INTEGER,
                 Heart_Rate INTEGER, Daily_Steps INTEGER, 
                Sleep_Disorder TEXT)
                ''') 
    conn.commit() 
    conn.close()

def data_from_csv(table_name,filename): 
    conn = sqlite3.connect('Health_database.db')
    cur = conn.cursor()
        
    with open(filename, 'r') as file:
        data = csv.reader(file)
        next(data)
        for row in data:
            cur.execute(f"REPLACE INTO {table_name} VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)", row)


        conn.commit()
        print("Data loaded successfully.")
        conn.close()

