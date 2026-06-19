class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __len__(self):
        return len(self.title)
    
a1 = Book("Harry Potter", "J.K. Rowling")
a2 = Book("Carrie", "Stephen King")
print(str(a1))
print(len(a1))
print(str(a2))
print(len(a2))