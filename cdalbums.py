import sqlite3

connenction = sqlite3.connect('cdalbums.db')
cursor = connenction.cursor() # za pomocą kursora można wprowadzać zmiany do bazy danych

global sortBy
sortBy = "artist"

def selectAction():
    print()
    print("Select desired action: ")
    print("a - read all records")
    # print("r - read record ")
    # print("f - find in database")
    print("s - set sorting: sort by " + sortBy)
    print("i - insert new record to database")
    print("d - delete selected record from database")
    # print("e - export to csv")
    print("x - close program")
    print()
    action = input("Input action charter and press enter --> ")
    print()
    if action == "a":
        readAllRecords()
    elif action == "s":
        selectSortMethod()
    elif action == "d":
        deleteRecordID()
    elif action == "i":
        insertRecord()
    elif action == "x":
        closeProgram()
    else:
        print("Wrong command, press enter...")
        input()
        selectAction()

def selectSortMethod():
    global sortBy
    print()
    print("Setup sorting method:")
    print("a - sort by Artist")
    print("t - sort by Title")
    print("y - sort by Year")
    print("i - sort by Album ID")
    print()
    select = input("Set sorting by --> ")
    if select == "a":
        sortBy = "artist"
    elif select == "t":
        sortBy = "title"         
    elif select == "y":
        sortBy = "year"       
    elif select == "i":
        sortBy = "id"
    else:
        sortBy = "artist"
    print()
    print("Sorting is set by " + sortBy + "... ")
    print()
    selectAction()


def readAllRecords():
    def sortByArtist(e):
        return e[1]
    def sortByTitle(e):
        return e[2]
    def sortByYear(e):
        return e[3]
    def sortById(e):
        return e[0]

    cursor.execute('''SELECT * from albums''')
    records = cursor.fetchall()
    # print(records)
    
    if sortBy == "artist":
        records.sort(reverse=False, key=sortByArtist)
    elif sortBy == "title":
        records.sort(reverse=False, key=sortByTitle)    
    elif sortBy == "year":
        records.sort(reverse=False, key=sortByYear)    
    elif sortBy == "id":
        records.sort(reverse=False, key=sortById)    
    
    #wyświetlenie danych za pomocą pętli
    print()
    i = 1
    for row in records:
        print("Item: ", i)
        print("Artist: ", row[1])
        print("Title: ", row[2])
        print("Year: ", row[3])
        print("Album ID: ", row[0])
        print()
        i = i + 1
    print("Total records in database: ", len(records))
    selectAction()


def readRecordID(id):
    readId = id
    print()
    cursor.execute('SELECT * from albums WHERE id = ' + readId)
    record = cursor.fetchall()
    if record == []:
        print("This record don't exist!")
        selectAction()
    for row in record:
        print("Artist: ", row[1])
        print("Title: ", row[2])
        print("Year: ", row[3])
        print("Album ID: ", row[0])
        print()
        

def insertRecord():
    # funkcja wprowadzanie danych - przygotowanxie polecenia SQL z danymi:
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
        # print(f'data to store: {artist}, {title}, {year}')
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


def deleteRecordID():
    while True:
        id = input("Enter Album ID to delete (cancel to stop) --> ")
        try:
            int(id)
            break
        except:
            if id == "cancel":
                selectAction()
            else:
                continue
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
        print("Record deleted...")
        print()
        selectAction()
    else:
        print()
        print("Record are NOT deleted...")
        print()
        selectAction()

def closeProgram():
        connenction.close()
        print("Program closing, press enter...")
        input()
        exit()

selectAction()

connenction.close()









