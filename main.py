# Titel: Telefonregister
# Uppgifts nr: 166
# Författare: Rasmus Thunberg
# Datum: 2023-04-24

#Datastrukturer, sökning, sortering, filhantering

''' Det här är ett program för hantering ett telefonregister
 Programmet lagrar personers namn, adress och telefonnummer i "telefonbok.txt"
 mellan körningarna av programmet. Telefonboken ska för enkelhetens skull inte ta flera personer som har identiskt för- OCH efternamn.
 Detta för att vid byte av telefonnummer är det inte säkert att det finns en primärnyckel, då telefonnummer annars hade kunnat
 funka som det, individer kan inte heller ha samma telefonnummer, i.o.m att det är så i verkligheten.
 Dock kan flera individer ha samma adress'''


class Person:
    '''Person-objekten lagras i en lista personer, som är ett attribut i klassen Telefonbok.

     En klass som beskriver varje person:
     firstname - förnamnet på personen i fråga, av datatypen sträng
     lastname - efternamnet på personen i fråga, av typen sträng
     adress - personens adress, av datatypen sträng
    phoneNum - personens telefonnummer, av datatypen int'''

    '''metod för att skapa ett nytt objekt
    Inparametrar: self, firstname, lastname, adress, phoneNum'''
    def __init__(self, firstname, lastname, adress, phoneNum):
        self.firstname = firstname
        self.lastname = lastname
        self.adress = adress
        self.phoneNum = phoneNum

    def __lt__(self, other):
        '''metod för att möjliggöra sortering av personerna, inparametrarna är self och other
            där other innebär objektet den jämför med'''
        if self.firstname < other.firstname: #sorterar först och främst på förnamn
            return True
        elif self.firstname == other.firstname: #om två objekt har samma förnamn sorteras det på efternamn
            if self.lastname < other.lastname:
                return True
            elif self.lastname == other.lastname: #om två objekt har både samma förnamn och efternamn sorteras det på telefonnummer
                if self.phoneNum < other.phoneNum:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

def readPersons():
    '''öppnar phonebook.txt en gång i meny loopen. Inputen är filen som allt hämtas från.
    Returnerar phoneBook som är en lista över alla personer, där varje person består av en lista med
    fornamn, efternamn, adress, telefonnummer'''
    read = open("phonebook.txt", "r", encoding='utf-8')

    phoneBook = []
    line = read.readlines()
    for i in range(0, len(line), 4): #step parametern har 4, vilket innebär att loopen hoppar 4 steg varje gång
        phoneBook.append(Person(line[i], line[i+1], line[i+2], line[i+3].replace("\n", "")))
    read.close()  # stänger vägen till textfilen
    return phoneBook

class PhoneBook():
    '''Klass som innehåller alla personer och deras information:
    readPersons - en lista över alla personer'''

    def __init__(self, persons = None):
        '''metod för att skapa en katalog med alla personer
        Inparametrar: self, persons=None
        Om det finns en inparameter för persons.
        så sätter den self.persons till inparametern'''
        if persons:
            self.persons = persons
        else:
            self.persons = readPersons()

    def cleanPerson(self, obj):
        '''Metod för att ta bort radbrytningen mellan objekten, returnerar objekten utan radbrytning
        som sedan används i de andra metoderna.
        Inputen är objektet person som är en loopning igenom personerna i listan self.persons.
        Gör att det slipper upprepas i varje metod som använder objekten utan radbrytning'''
        obj.firstname = str(obj.firstname).replace("\n", "")
        obj.lastname = str(obj.lastname).replace("\n", "")
        obj.fullname = str(obj.firstname + " " + obj.lastname)
        obj.adress = str(obj.adress).replace("\n", "")
        obj.phoneNum = str(obj.phoneNum)
        return obj.firstname, obj.lastname, obj.adress, obj.phoneNum, obj.lastname

    def addPersonNames(self, firstname, lastname):
        '''metod för att lägga till namnet på en person. Inparametrar är firstname & lastname.
        returnerar True om allt funkar som det ska, returnerar False om kombinationen av för- och efternamn
        redan är upptaget eller tomt'''
        while True:
            nameExistCheck = 0
            for person in self.persons: #loopar igenom alla personer
                person.firstname, person.lastname, person.adress, person.phoneNum, person.lastname = self.cleanPerson(person)
                if firstname == person.firstname and lastname == person.lastname: #kollar om komb. av för- och efternamn finns
                    print("Kombinationen av för- och efternamn är upptaget!")
                    return False
                if firstname == "" or lastname == "":
                    print("Personen måste ha både för- och efternamn")
                    return False
                elif nameExistCheck == len(self.persons)-1:
                    return True
                else:
                    nameExistCheck += 1

    def addPersonNum(self, phoneNum):
        '''metod för att lägga till telefonnumret på en person. Inparametrar är phoneNum
        returnerar True om allt funkar som det ska, returnerar False om någon felinmatning görs'''
        while True:
            for person in self.persons:
                if phoneNum == person.phoneNum:  # Kollar om numret redan används av någon
                    print("Numret är upptaget!")  # isåfall returneras False
                    return False
            try:
                phoneNum = int(phoneNum)
                if len(str(phoneNum)) < 6:
                    print("För kort telefonnummer!")
                    return False
                elif len(str(phoneNum)) > 12:
                    print("För långt telefonnummer!")
                    return False
                else:
                    return True
            except ValueError:
                print("Mata enbart in telefonnummer med siffror!")
                return False
            except:
                print("Felaktigt format!")
                return False

    def addPerson(self, first, last, adress, num):
        '''Metod för att sammanställa förnamn, efternamn, adress och telefonnummer som tidigare matats in
        och skapa ett objekt i Person som läggs till i persons.
        Inparametrar är förnamn, efternamn, adress och telefonnummer'''
        self.persons.append(Person(first, last, adress, num))

    def searchName(self, first, last):
        '''metod för att söka upp en person. Tar in firstname och lastname som är för- och efternamn.
        Ifall count == 0 betyder det att ingen med det eftersökta för- och efternamnet hittades, Returnerar True
        om någon med det aktuella namnet hittas'''
        self.firstname = first
        self.lastname = last
        count = 0
        for person in self.persons:
            person.firstname, person.lastname, person.adress, person.phoneNum, person.lastname = self.cleanPerson(person)
            if self.firstname == person.firstname and self.lastname == person.lastname:
                count += 1
        i = 0
        for person in self.persons:
            person.firstname, person.lastname, person.adress, person.phoneNum, person.lastname = self.cleanPerson(person)
            if self.firstname == person.firstname and self.lastname == person.lastname:
                if i == 0:
                    print(" " * 4, "Namn", " " * 28, "Adress", " " * 27, "Telefonnummer")
                    print("{:30s} {:43s} {}".format(person.fullname, person.adress, person.phoneNum))
                    return True
                i += 1
            elif count == 0:
                print("Namnet finns inte, skriv in ett namn som finns!")
                break

    def searchNum(self, num):
        '''Metod för att söka efter ett telefonnummer.
        Tar in numret och returnerar True om telefonnumret finns'''
        phoneNum = num
        booleanCheck = False
        for person in self.persons:
            person.firstname, person.lastname, person.adress, person.phoneNum, person.lastname = self.cleanPerson(person)
            if phoneNum == person.phoneNum:
                print(" "*4, "Namn", " "*28, "Adress", " "*27, "Telefonnummer")
                print("{:30s} {:43s} {}".format(person.fullname, person.adress, person.phoneNum))
                return True
            else:
                pass
        if booleanCheck == False:
            print("Telefonnumret finns inte, testa ett annat nummer!")

    def removePerson(self, first, last):
        '''Metod för att ta bort en person.
        Tar inparametrar firstname och lastname. Returnerar True om namnet finns'''
        self.firstname = first
        self.lastname = last
        booleanCheck = False
        for person in self.persons:
            person.firstname, person.lastname, person.adress, person.phoneNum, person.lastname = self.cleanPerson(person)
            if self.firstname == person.firstname and self.lastname == person.lastname:
                self.persons.remove(self.persons[self.persons.index(person)])
                print(f"Tagit bort {self.firstname} {self.lastname}!")
                return True
            else:
                pass
        if booleanCheck == False:
            print("Namnet finns inte, skriv in ett namn som finns!")

    def checkExists(self, first, last):
        '''Metod för att kolla om en person existerar.
        inparametrar är firstname och lastname. Returnerar True om namnet finns'''
        self.firstname = first
        self.lastname = last
        booleanCheck = False
        for person in self.persons:
            person.firstname, person.lastname, person.adress, person.phoneNum, person.lastname = self.cleanPerson(person)
            if self.firstname == person.firstname and self.lastname == person.lastname:
                return True
            else:
                continue
        if booleanCheck == False:
            print("Namnet finns inte, skriv in ett namn som finns!")

    def newAdress(self, first, last, adressNew):
        '''Metod för att uppdatera adressen till personen.
        Returnerar True om personen som ska ha den nya adressen finns och det matats in en adress,
        annars returneras False'''

        self.firstname = first
        self.lastname = last
        booleanCheck = False
        for person in self.persons:
            person.firstname, person.lastname, person.adress, person.phoneNum, person.lastname = self.cleanPerson(person)
            if self.firstname == person.firstname and self.lastname == person.lastname:
                if adressNew == "":
                    print("Mata in en adress!")
                    return False
                else:
                    person.adress = adressNew
                    print(f"Uppdaterat adressen för {self.firstname} {self.lastname} till {person.adress}!")
                    return True
            else:
                pass
        if booleanCheck == False:
            print("Namnet finns inte, skriv in ett namn som finns!")

    def newPhoneNum(self, first, last, newNum):
        '''Metod för att uppdatera telefonnumret. Inparametrar är förnamn, efternamn och det nya numret.
        Metoden returnerar True om telefonnumret uppdateras.'''

        self.firstname = first
        self.lastname = last
        for person in self.persons:
            person.firstname, person.lastname, person.adress, person.phoneNum, person.lastname = self.cleanPerson(person)
            if self.firstname == person.firstname and self.lastname == person.lastname:
                if person.phoneNum == newNum:
                    print("Numret är redan upptaget!")
                    pass
                elif len(str(newNum)) < 6:
                    print("För kort telefonnummer!")
                    pass
                elif len(str(newNum)) > 12:
                    print("För långt telefonnummer!")
                    pass
                else:
                    person.phoneNum = newNum
                    print(f"Uppdaterat telefonnumret för {self.firstname} {self.lastname} till {person.phoneNum}!")
                    return True
            else:
                pass

    def printingPerson(self):
        '''Metod för att skriva ut en sorterad lista
        med alla personer.'''
        print(" "*4, "Namn", " "*28, "Adress", " "*27, "Telefonnummer")
        self.persons.sort()
        for person in self.persons:
            person.firstname, person.lastname, person.adress, person.phoneNum, person.lastname = self.cleanPerson(person)
            print("{:30s} {:43s} {}".format(person.fullname, person.adress, person.phoneNum))#:Xs ser till att ta upp utrymme som motsvarar X tecken

    def writePhoneBook(self, file = "phonebook.txt"):
        '''Metod för att lägga till den uppdaterade telefonboken till
        "phonebook.txt" inparameter är filnamnet, den returnerar inget'''
        clean = open(file, "w", encoding='utf-8')
        clean.write("") #rensar phonebook.txt från allt som stod där tidigare
        clean.close()
        writing = open(file, "a", encoding='utf-8')
        phoneBook = []
        for person in self.persons: #Lägger till varje objekt från varje person rad för rad i varsin lista inut i listan phoneBook
            person.firstname, person.lastname, person.adress, person.phoneNum, person.lastname = self.cleanPerson(person)
            phoneBook.append(f"{person.firstname}\n{person.lastname}\n{person.adress}\n{person.phoneNum}\n")
        for i in range(len(phoneBook)): #lägger till de nya och uppdaterade personerna till phonebook.txt
            writing.write(phoneBook[i])
        writing.close()  # stänger vägen till textfilen
            # Returnerar phoneBook som är en lista över alla personer, där varje person består av en lista med
            # fornamn, efternamn, adress, telefonnummer

def validNumber(startNum, endNum):
    '''Funktion för att skriva ut att det inte är en giltlig siffra som matats in- Inparametrar är
    start och slutsiffran'''
    print(f"Skriv in en giltlig siffra mellan {startNum}-{endNum}!")

def getInfo(phoneBook):
    '''Funktion för att söka upp ett nummer eller namn, input är phoneBook'''
    searchNameNum = input("Vill du:\n1. Leta efter en person\n2. Få information om ett telefonnummer\n")
    if searchNameNum == "1":
        while True:
            firstname = input("Förnamn: ").capitalize()
            lastname = input("Efternamn: ").capitalize()
            if phoneBook.searchName(firstname, lastname) == True:
                break
    elif searchNameNum == "2":
        while True:
            replaceChar = ["-", " "]
            phoneNum = input("Telefonnumret: ")
            for i in replaceChar: # Tar bort "-" och " " från det inmatade numret
                phoneNum = phoneNum.replace(i, "")
            if phoneBook.searchNum(phoneNum) == True:
                break
    else:
        validNumber(1, 2)


def addPerson(phoneBook):
    """Funktion för att lägga till en ny person, input är phoneBook"""
    print("Lägger till ny person")
    while True:
        first = input("Förnamn: ").strip().capitalize()
        last = input("Efternamn: ").strip().capitalize()
        checkNames = phoneBook.addPersonNames(first, last)
        if checkNames == True:
            break
        else:
            continue

    while True:
        adress = input("Adress: ").title()
        if adress == "":
            print("Skriv in en adress!")
            continue
        else:
            break

    while True:
        phoneNum = input("Telefonnummer: ")
        checkNum = phoneBook.addPersonNum(phoneNum)
        if checkNum == True:
            break
        else:
            continue

    if checkNames == True and checkNum == True:
        phoneBook.addPerson(first, last, adress, phoneNum)
        print(f"Lagt till {first} {last}!")

def removePerson(phoneBook):
    '''Funktion för att ta bort en person, input phoneBook'''
    print("Tar bort person")
    while True:
        first = input("Förnamn: ").strip().capitalize()
        last = input("Efternamn: ").strip().capitalize()
        if phoneBook.removePerson(first, last) == True:
            break

def changeInfo(phoneBook):
    '''Funktion för att ändra telefonnumret eller adress för någon.
    Returnerar False om allt är korrekt, tar phoneBook som input'''
    print("Vem vill du ändra uppgifter för?")
    while True:
        first = input("Förnamn: ").strip().capitalize()
        last = input("Efternamn: ").strip().capitalize()
        if phoneBook.checkExists(first, last) == True:
            changeInfo = input("Vill du:\n1. Ändra telefonnummer\n2. Ändra Adress\n")
            if changeInfo == "1":
                while True:
                    newNum = input("Vad ska det nya telefonnumret vara?: ")
                    try:
                        replaceChar = ["-", " "]
                        for i in replaceChar:
                            newNum = newNum.replace(i, "")
                        int(newNum)
                        if phoneBook.newPhoneNum(first, last, newNum) == True:
                            return False
                    except:
                        print("Skriv enbart in siffror, bindestreck och mellanslag!")
            elif changeInfo == "2":
                while True:
                    newAdress = input("Vad ska den nya adressen vara: ").capitalize()
                    if phoneBook.newAdress(first, last, newAdress) == True:
                        return False
            else:
                validNumber(1, 2)
        else:
            pass

def main():
    '''Metod för att starta allt och skriver ut valen
    har varken några inparametrar eller något den returnerar'''

    phoneBook = PhoneBook()


    while True:
        val = input("Vill du:\n1. Leta efter ett telefonnummer eller ett namn\n2. Lägga till nya uppgifter\n"
                    "3. Ta bort uppgifter\n4. Ändra uppgifter (telefonnummer och adress)\n5. Ha en utskrift av registret\n"
                    "6. Avsluta\n")

        if val == "1":
            getInfo(phoneBook)

        elif val == "2":
            addPerson(phoneBook)

        elif val == "3":
            removePerson(phoneBook)

        elif val == "4":
            changeInfo(phoneBook)

        elif val == "5":
            phoneBook.printingPerson()

        elif val == "6":
            phoneBook.writePhoneBook()
            print("Avslutar telefonboken, tack för att du använt oss!")
            break
        else:
            validNumber(1, 5)

def fileExistCheck():
    '''Kör funktionen main och kollar då om txt-filen som är tänkt att läsa från finns, vid FileNotFoundError skriver
    den ut att filen inte finns och avslutas'''
    try:
        main()

    except FileNotFoundError:
        print("Filen finns inte")

fileExistCheck()