import sqlite3

connenction = sqlite3.connect('cdalbums.db')
cursor = connenction.cursor() # za pomocą kursora można wprowadzać zmiany do bazy danych

def selectAction():
    print()
    print("Select desired action: ")
    print("a - read all records")
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
        id = input("Enter Album ID to delete --> ")
        deleteRecordID(id)
    elif action == "i":
        insertRecord()
    elif action == "x":
        closeProgram()
    else:
        print("Wrong command, press enter...")
        input()
        selectAction()


def readAllRecords():
    cursor.execute('''SELECT * from albums''')
    records = cursor.fetchall()
    print()
    #wyświetlenie danych za pomocą pętli
    i = 1
    for row in records:
        print("Item: ", i)
        print("Artist: ", row[1])
        print("Title: ", row[2])
        print("Year: ", row[3])
        print("Album ID: ", row[0])
        print()
        i = i + 1
    print("Total rows: ", len(records))
    selectAction()


def readRecordID(id):
    readId = id
    print()
    cursor.execute('SELECT * from albums WHERE id = ' + readId)
    record = cursor.fetchall()
    for row in record:
        print("Artist: ", row[1])
        print("Title: ", row[2])
        print("Year: ", row[3])
        print("Album ID: ", row[0])
        print()
        

def insertRecord():
    # funkcja wprowadzanie danych - przygotowanie polecenia SQL z danymi:
    # uwaga wartość null spowoduje podstawienie automatycznego numeru w kolumnie ID
    
    def getYear():
        # pętla sprawdzająca czy rok to liczba int - jeśli tak zwraca year, jeśli nie to wraca na początek pętli
        while True:
            year = input("Enter album year: ")
            try:
                int(year) # check if year can be int
                year = int(year) #convert year to int
                # print(type(year))
                if year > 1900 and year < 2022: # check if year is more than 1900
                    return year
            except:
                print()
                print("invalid album year value - try again...")
                continue #kontynuacja pętli
    
    def storeData():
        print("!! storing data !!")
        print(f'data to store: {artist}, {title}, {year}')
        query = f'INSERT INTO albums VALUES({dbid}, "{artist}", "{title}", {year})'
        cursor.execute(query)
        # cursor.execute('INSERT INTO albums VALUES(?, ?, ?, ?)',(dbid, artist, title, year))
        connenction.commit()
        print()
        print("Record stored...")
        # print("Press enter...")
        # year = None
        # input()
        selectAction()

    dbid = "null"
    artist = input("Enter Artist: ")
    title = input("Enter Title: ")
    year = getYear()
    storeData()



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
        print()
        selectAction()
    else:
        print()
        print("Record are NOT deleted...")
        print()
        selectAction()

def closeProgram():
        connenction.close()
        print("Program closed. Thank You.")
        exit()


selectAction()


connenction.close()









