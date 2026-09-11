class book:
    def __init__(self,title, author):
        self.title = title
        self.author = author
    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)   
class ebook(book):
    def __init__(self, file_size, title, author):
        super().__init__(title, author)
        self.file_size = file_size
    def display(self):
        super().display()
        print("File Size:", self.file_size, "MB")   
e = ebook(5, "Python Programming", "John Doe")
e.display()