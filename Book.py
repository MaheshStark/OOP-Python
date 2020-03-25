class Book:
    def __init__(self, bookname, author, chapter, isbn, price):  # constructor
        self.bookname = bookname
        self.author = author
        self.chapter = chapter
        self.isbn = isbn
        self.price = price

    def read(self):  # read method
        print("Reading the " + self.bookname + " book")


# create ten objects
b1 = Book("Madol duuwa", "Mr.M.wickramasinghe", "20", "1224554423", "1500.00")
b2 = Book("Baddegama", "Mr.A.P.Gunarathne", "30", "11258784412", "1800.00")
b3 = Book("Headfirst java", "Mr.k.sierra", "45", "44544454889", "2000.00")
b4 = Book("Headfirst PHP", "Mr.d.kevin", "18", "5687424122", "1300.00")
b5 = Book("Headfirst OOP", "Mr.k.sierra", "15", "1212245547", "1200.00")
b6 = Book("Headfirst css", "Mr.M.james", "12", "7894154422", "1400.00")
b7 = Book("Headfirst python", "Mr.M.clinton", "22", "7874547455", "1400.00")
b8 = Book("basic python", "Mr.N.agarwal", "25", "7778444522", "2200.00")
b9 = Book("java to hero", "Mr.M.R.Krishnan", "40", "1444755557", "1800.00")
b10 = Book("C sharp expert", "Mr.M.abhiman", "10", "1444755557", "2500.00")

print(b3.bookname + " Author's name is " + b3.author)
b3.read()
