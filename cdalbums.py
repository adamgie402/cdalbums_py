import sqlite3

connenction = sqlite3.connect('cdalbums.db')
cursor = connenction.cursor() # za pomocą kursora można wprowadzać zmiany do bazy danych

def selectAction():
    print()
    print("Select desired action: ")
    print("a - read all database ")
    # print("r - read record ")
    # print("f - find in database")
    print("i - insert new record to database")
    print("d - delete selected record from database")
    # print("e - export to csv")
    print("x - close program")
    print()
    action = input("input action charter and press enter --> ")
    if action == "a":
        readAllRecords()
    # elif action == "r":
    #     id = input("Input record ID --> ")
    #     readRecordID(id)
    elif action == "d":
        id = input("Enter ID to delete --> ")
        deleteRecordID(id)
    elif action == "i":
        insertRecord()
    elif action == "x":
        closeProgram()
    else:
        print("Wrong charter, press enter...")
        input()
        selectAction()


def readAllRecords():
    cursor.execute('''SELECT * from albums''')
    records = cursor.fetchall()
    print()
    #wyświetlenie danych za pomocą pętli
    for row in records:
        print("ID: ", row[0])
        print("Artist: ", row[1])
        print("Title: ", row[2])
        print("Year: ", row[3])
        print()
    print("Total rows: ", len(records))
    selectAction()


def readRecordID(id):
    readId = id
    print()
    cursor.execute('SELECT * from albums WHERE id = ' + readId)
    record = cursor.fetchall()
    for row in record:
        print("ID: ", row[0])
        print("Artist: ", row[1])
        print("Title: ", row[2])
        print("Year: ", row[3])
        print()
        

def insertRecord():
    def saveRecord():
        query = f'INSERT INTO albums VALUES({dbid}, "{artist}", "{title}", {year})'
        cursor.execute(query)
        connenction.commit()
        print()
        print("Record stored...")
        print("Press enter...")
        input()
        selectAction()
    # funkcja wprowadzanie danych - przygotowanie polecenia SQL z danymi:
    # uwaga wartość null spowoduje podstawienie automatycznego numeru w kolumnie ID
    dbid = "null"
    artist = input("Enter Artist: ")
    title = input("Enter Title: ")
    year = input("Enter album year: ")
    try:
        year = int(year)
        saveRecord()
    except:
        print()
        print("invalid album year value...")
        print("press enter...")
        input()
        selectAction()


def deleteRecordID(id):
    delId = id
    readRecordID(delId)
    print()
    print('Are You sure to delete this record?')
    print('y - yes')
    print('n - no')
    print()
    delAction = input('Input action charter and press enter --> ')
    if delAction == 'y':
        cursor.execute('DELETE from albums WHERE id = ' + delId)
        connenction.commit()
        print()
        print("Record deleted, press enter...")
        input()
        print()
        selectAction()
    else:
        selectAction()

def closeProgram():
        connenction.close()
        print("Program closed. Thank You.")
        exit()


selectAction()


connenction.close()









