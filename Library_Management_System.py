import os
from tkinter import *
from tkinter import messagebox

class Book:
    def __init__(self, title, author,genre, publication_year):
        self.title=title
        self.author=author
        self.genre=genre
        self.publication_year=publication_year
    
    def __str__(self):
        return f"{self.title} by {self.author}, {self.genre}, {self.publication_year}"


class Library:
    def __init__(self):
        self.books = []
    def add_book(self,book):
        try:
            print("please enter the book details: ")
            self.books.append(book)
            print ("book added successfully")
        except Exception as e:
            print("error in adding book",e)
        
    def remove_book(self,title,fileName="/Users/mohamedezzat/Desktop/library_books.txt"):
        try:
            print("please enter the book title: ")
            if not os.path.exists(fileName):
                print("the file is not exist")
                return
            
            with open(fileName,'r') as file:
                lines = file.readlines()
                flag=False
                fileLines=[]
                for line in lines:
                    book_title=line.strip().split(",")
                    if book_title[0]==title:
                        flag=True
                        print("the book removed successfuly!")
                    else:
                        fileLines.append(line)
            if not flag:
                print("the book is not exist in the library")
            with open (fileName,"w") as file:
                file.writelines(fileLines)
            
            self.books=(Book(*line.strip().split(","))for line in fileLines)
        except Exception as e:
            print("error in removing book",e)

        except Exception as e:
            print("error in removing book",e)

    def search_book(self,title,fileName="/Users/mohamedezzat/Desktop/library_books.txt"):
        try:
            if not os.path.exists(fileName):
                print("the file is not exist")
                return
            with open(fileName,"r") as file:
                lines = file.readlines()
                flag=False
                for line in lines:
                    book_title=line.strip().split(",")
                    if book_title[0]==title:
                        flag=True
                if flag==True:
                    print("the book is exist in the library")
                else: print("book doesn't exist")
        except Exception as e:
            print("error in searching book",e)

    def display_book(self,fileName="/Users/mohamedezzat/Desktop/library_books.txt"):
        try:
            if not os.path.exists(fileName):
                print("the file is not exist")
                return
            with open (fileName,"r") as file:
                if os.path.getsize("/Users/mohamedezzat/Desktop/library_books.txt")>0:
                    lines = file.readlines()
                    for line in lines:
                        print(line.strip())
                else: print("file is empty")
        except Exception as e:
            print("error in displaying books",e)

    def save_file(self,fileName="/Users/mohamedezzat/Desktop/library_books.txt"):
        with open(fileName,"w") as file:
            for book in self.books:
                file.write(f"{book.title},{book.author},{book.genre},{book.publication_year}\n")
    
    def load_file(self,fileName="/Users/mohamedezzat/Desktop/library_books.txt"):
        if not os.path.exists(fileName):
            print("it is no file name as you write, let's create one.. ")
            open(fileName,"w").close()
            return
        with open(fileName,"r") as file:
            for line in file:
                title,author,genre,publication_year=line.strip().split(",")
                self.books.append(Book(title,author,genre,publication_year))
                print("file loaded successfully")

class Library_GUI:
    def __init__(self,root):
        self.library=Library()
        self.library.load_file()

        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("800x500")

        self.label=Label(self.root,text="Library Management System",font=("Arial",16))
        self.label.pack(pady=10)

        self.add_button=Button(self.root,text="Add Book",command=self.add_book)
        self.add_button.pack(pady=5)

        self.remove_button=Button(self.root,text="Remove Button",command=self.remove_book)
        self.remove_button.pack(pady=5)

        self.search_button=Button(self.root,text="Search Book",command=self.search_book)
        self.search_button.pack(pady=5)

        self.display_button = Button(root, text="Display Books", command=self.display_books)
        self.display_button.pack(pady=5)

        self.exit_button = Button(root, text="Exit", command=self.exit_app)
        self.exit_button.pack(pady=5)

    def add_book(self):
        self.add_window=Toplevel(self.root)
        self.add_window.title("Add Book")

        Label(self.add_window,text="title: ").grid(row=0,column=0)
        self.title_entry=Entry(self.add_window)
        self.title_entry.grid(row=0,column=1)

        Label(self.add_window,text="author: ").grid(row=1,column=0)
        self.author_entry=Entry(self.add_window)
        self.author_entry.grid(row=1,column=1)
        
        Label(self.add_window,text="genre: ").grid(row=2,column=0)
        self.genre_entry=Entry(self.add_window)
        self.genre_entry.grid(row=2,column=1)
        
        Label(self.add_window,text="publication_year: ").grid(row=3,column=0)
        self.publication_year_entry=Entry(self.add_window)
        self.publication_year_entry.grid(row=3,column=1)

        Button(self.add_window,text="Add",command=self.save_add_book).grid(row=4, column=0, columnspan=2)


    def save_add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        genre = self.genre_entry.get()
        publication_year = self.publication_year_entry.get()
        book = Book(title, author, genre, publication_year)
        self.library.add_book(book)
        self.library.save_file()


    def remove_book(self):
        remove_window = Toplevel(self.root)
        remove_window.title("Remove Book")

        Label(remove_window, text="Title:").grid(row=0, column=0)
        self.remove_title_entry = Entry(remove_window)
        self.remove_title_entry.grid(row=0, column=1)
        Button(remove_window, text="Remove", command=self.save_remove_book).grid(row=1, column=0, columnspan=2)
          
    def save_remove_book(self):
        title = self.remove_title_entry.get()
        self.library.remove_book(title)
        self.library.save_file()
    def search_book(self):
        search_window = Toplevel(self.root)
        search_window.title("Search Book")

        Label(search_window, text="Title:").grid(row=0, column=0)
        self.search_title_entry = Entry(search_window)
        self.search_title_entry.grid(row=0, column=1)

        Button(search_window, text="Search", command=self.save_search_book).grid(row=1, column=0, columnspan=2)

    def save_search_book(self):
        title = self.search_title_entry.get()
        self.library.search_book(title)

    def display_books(self):
        self.library.display_book()

    def exit_app(self):
        self.library.save_file()
        messagebox.showinfo("Info", "File saved successfully!\nThanks for using our system!")
        self.root.quit()        

if __name__ == "__main__":
    root = Tk()
    app = Library_GUI(root)
    root.mainloop()









                





        
    
    
