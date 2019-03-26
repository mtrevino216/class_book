class Book():
    def __init__(self,title,author,publisher):
        self.title_name = title
        self.author_name = author
        self.publisher_name = publisher

    def setTitle(self, t):
        self.title_name = t

    def getTitle(self):
        return self.title_name

    def __str__(self):
        return str("Book title: " + self.title_name + "\nAuthor's name: " + self.author_name + "\nPublisher's name: " + self.publisher_name  )

def main():

    user_book=Book("Starting out with Python", "Tony Gaddis", "Pearson")
    print(user_book)

main()