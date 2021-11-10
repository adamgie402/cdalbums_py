import sqlite3


connenction = sqlite3.connect('cdalbums.db')
cursor = connenction.cursor() # za pomocą kursora można wprowadzać zmiany do bazy danych

# funkcja wprowadzanie danych - przygotowanie polecenia SQL z danymi:
# uwaga wartość null spowoduje podstawienie automatycznego numeru w kolumnie ID

def selectAction():
    print()
    print("Select action: ")
    print("r - read database ")
    print("i - insert new record to database")
    print("d - delete selected record in database")
    print("f - find in database")
    print("c - close program")
    print()
    action = input("?? ")
    if action == "r" or action == "i":
        if action == "i":
            insertRecord()
        else:
            readAllRecords()
    else:
        print()  
        print("Inwalid entry...")
        print()   
        selectAction()


def readAllRecords():
    cursor.execute('''SELECT * from albums''')
    records = cursor.fetchall()
    print()
    print("Total rows: ", len(records))
    print("Printing each row.....")
    print()
    #wyświetlenie danych za pomocą pętli
    for row in records:
        print("ID: ", row[0])
        print("Artist: ", row[1])
        print("Title: ", row[2])
        print("Year: ", row[3])
        print()
    selectAction()

def insertRecord():
    print()
    print("Adding new record to CD database.....")
    id = "null"
    artist = input("Enter Artist: ")
    title = input("Enter Title: ")
    year = input("Enter Year: ")
    query = f'INSERT INTO albums VALUES({id}, "{artist}", "{title}", {year})'
    print(query)
    cursor.execute(query)
    connenction.commit()
    print("record stored sucesfully!")
    print()
    selectAction()

selectAction()

connenction.close()

#tworzenie tabeli 
# cursor.execute('''CREATE TABLE albums(
#     id INTEGER PRIMARY KEY,
#     Artist TEXT, 
#     Title TEXT, 
#     Year INT
#     )''')


# usuwanie całej tabeli
# cursor.execute("DROP TABLE albums")
# connenction.commit()


# wprowadzanie danych - przygotowanie polecenia SQL z danymi:
# uwaga wartość null spowoduje podstawienie automatycznego numeru w kolumnie ID
# cursor.execute('''INSERT INTO albums VALUES(null, 'Coldplay', 'Music Of The Spheres', 2021)''')
# connenction.commit()


# poprawianie danych
# cursor.execute('''UPDATE albums SET Year = 1976 WHERE title = "Taxi Driver"''')
# connenction.commit()

#odczytywanie danych:







