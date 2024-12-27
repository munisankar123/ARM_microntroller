from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import json
import pandas as pd
from datetime import datetime


class LibraryManagement:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Library Management System")

        # Main Page Frame
        main_page = Frame(self.root, bg="sky blue")
        main_page.pack(fill=BOTH, expand=True)

        # Title Label
        title = Label(main_page, text="Library Management System", 
                      font=("times new roman", 24, "bold"), bg="blue", fg="white", border=12, relief=GROOVE)
        title.pack(pady=20)
        
        welcome = Label(main_page, text="Welcome to the Library Management System",
                        font=("times new roman", 16, "bold"), bg="sky blue")

        welcome.pack(pady=20)

        # Button Frame
        button_frame = Frame(main_page, bg="sky blue")
        button_frame.pack(expand=True)

        # Buttons
        member_registration = Button(button_frame, text="Member Registration", font=("times new roman", 14, "bold"), 
                                     bg="white", fg="black", width=20, command=self.member_registration)
        enter_library = Button(button_frame, text="To Library", font=("times new roman", 14, "bold"), 
                                bg="white", fg="black", width=20, command=self.enter_library)

        
        member_registration.pack(pady=10)
        enter_library.pack(pady=10)

    def returnhome(self):
        for i in self.root.winfo_children():
            i.pack_forget()
        self.options()
    
    def member_registration(self):
        for widget in self.root.winfo_children():
            widget.pack_forget()
        member_registration=Frame(self.root, bg="sky blue")
        member_registration.pack(fill=BOTH, expand=True)
        title = Label(member_registration, text="Library Management System", 
                      font=("times new roman", 20, "bold"), bg="blue", fg="black",border=12, relief=GROOVE)
        

        namelabel=Label(member_registration,text="Enter your name")
        name=Entry(member_registration, width=30,text="Enter your name")

        contactlabel=Label(member_registration,text="Enter your contact")
        contact=Entry(member_registration, width=30,text="Enter your contact")

        submit=Button(member_registration,text="Submit",command=lambda: self.submituserdetails(name.get(),contact.get()))
        title.pack(side=TOP, fill=X)

        namelabel.pack(pady=10)
        name.pack(pady=10)

        contactlabel.pack(pady=10)
        contact.pack(pady=10)

        submit.pack(pady=10)
    def submituserdetails(self,name,contact):
        if name =="" or contact=="":
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                with open("users.json") as file:
                    data=json.load(file)
            except(FileNotFoundError, json.decoder.JSONDecodeError):
                data=[]
            new_user={
                "id":str(len(data)+1),
                "name":name,
                "contact":contact,
            }
            data.append(new_user)
            with open("users.json","w") as file:
                json.dump(data,file,indent=4)
            messagebox.showinfo("Success","User registered successfully completed and your id is "+str(len(data)+1))
            self.options()
    def enter_library(self):

        for widget in self.root.winfo_children():
            widget.pack_forget()
        
        
        library=Frame(self.root, bg="sky blue")
        library.pack(fill=BOTH, expand=True)

        title = Label(library, text="Library Management System", 
                      font=("times new roman", 20, "bold"), bg="blue", fg="black",border=12, relief=GROOVE)
        title.pack(side=TOP, fill=X)

        idlabel=Label(library,text="Enter your member id")
        id=Entry(library, width=30,text="Enter your member id")
        signlabel=Label(library,text="Enter your details to enter the library")
        signlabel.pack(pady=10)

        namelabel=Label(library,text="Enter your name")
        name=Entry(library, width=30,text="Enter your name")

        submit=Button(library,text="Submit",command=lambda: self.checkuser(id.get(),name.get()))

        idlabel.pack(pady=10)
        id.pack(pady=10)
        namelabel.pack(pady=10)
        name.pack(pady=10)
        submit.pack(pady=10)

    def checkuser(self,memberid,name):
        try:
            with open("users.json", "r") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []
        for user in data:
            if user.get("id") == memberid:
                global id
                id = memberid
                if user.get("name") == name:
                    self.options()
                    return
                else:
                    messagebox.showinfo("Error", "User not found. Please register.")
        self.member_registration()

    def options(self):
        for i in self.root.winfo_children():
            i.pack_forget()
        options=Frame(self.root, bg="sky blue")
        options.pack(fill=BOTH, expand=True)
        title = Label(options, text="Library Management System", 
                      font=("times new roman", 20, "bold"), bg="blue", fg="black",border=12, relief=GROOVE)
        title.pack(side=TOP, fill=X)

        oplabel=Label(options,text="Select an option")
        oplabel.pack(pady=10)

        addbook=Button(options,text="Add Book",command=self.addbook)
        borrow_book=Button(options,text="Borrow Book",command=self.borrowbook)
        return_book=Button(options,text="Return Book",command=self.retrunbook)
        exit=Button(options,text="Exit",command=self.root.quit)


        details=Button(options,text="Details of books",command=self.details)
        searchlabel=Label(options,text="Search for a book")
        search=Entry(options, width=30,text="Search for a book")
        searchbutton=Button(options,text="Search",command=lambda: self.searchbook(search.get()))
        searchlabel.pack(pady=10)
        search.pack(pady=10)
        searchbutton.pack(pady=10)
        


        addbook.pack(pady=10)
        borrow_book.pack(pady=10)
        return_book.pack(pady=10)
        details.pack(pady=10)
        exit.pack(pady=10)
    
    def searchbook(self, title):

        # Load book data
        try:
            with open("books.json", "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        if not data:
            messagebox.showinfo("Error", "No books available")
            return
        
        for book in data:
            if title.lower() in book["title"].lower():
                messagebox.showinfo("Book Found", f"Book found with ID {book['id']}\nTitle: {book['title']}\nAuthor: {book['author']}\nQuantity: {book['quantity']}\nAvailable: {book['available']}")
                return
        messagebox.showinfo("Book Not Found", "Book not found")

    def details(self):
        # Clear existing widgets
        for i in self.root.winfo_children():
            i.pack_forget()

        # Create a frame for the details
        details = Frame(self.root, bg="sky blue")
        details.pack(fill=BOTH, expand=True)

        # Title Label
        title = Label(details, text="Library Management System",
                    font=("times new roman", 20, "bold"), bg="blue", fg="black", border=12, relief=GROOVE)
        title.pack(side=TOP, fill=X)

        # Load book data
        try:
            with open("books.json", "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        if not data:
            messagebox.showinfo("Error", "No books available")
            return

        # Create a Treeview to display books
        tree_frame = Frame(details, bg="sky blue")
        tree_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Scrollbars
        x_scroll = Scrollbar(tree_frame, orient=HORIZONTAL)
        y_scroll = Scrollbar(tree_frame, orient=VERTICAL)

        # Treeview widget
        tree = ttk.Treeview(tree_frame, columns=("id", "title", "author", "quantity", "available"),
                            xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)

        x_scroll.config(command=tree.xview)
        y_scroll.config(command=tree.yview)
        x_scroll.pack(side=BOTTOM, fill=X)
        y_scroll.pack(side=RIGHT, fill=Y)

        tree.heading("id", text="ID")
        tree.heading("title", text="Title")
        tree.heading("author", text="Author")
        tree.heading("quantity", text="Quantity")
        tree.heading("available", text="Available")
        tree["show"] = "headings"

        tree.column("id", anchor=CENTER, width=50)
        tree.column("title", anchor=W, width=200)
        tree.column("author", anchor=W, width=150)
        tree.column("quantity", anchor=CENTER, width=100)
        tree.column("available", anchor=CENTER, width=100)

        # Insert data into Treeview
        for book in data:
            tree.insert("", "end", values=(book["id"], book["title"], book["author"], book["quantity"], book["available"]))

        tree.pack(fill=BOTH, expand=True)

        # Home Button
        home = Button(details, text="Home", command=self.returnhome, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        home.pack(pady=10)
    def addbook(self):
        for i in self.root.winfo_children():
            i.pack_forget()
        addbook=Frame(self.root, bg="sky blue")
        addbook.pack(fill=BOTH, expand=True)
        title = Label(addbook, text="Library Management System", 
                      font=("times new roman", 20, "bold"), bg="blue", fg="black",border=12, relief=GROOVE)
        title.pack(side=TOP, fill=X)


        titlelabel=Label(addbook,text="Enter book name")
        title=Entry(addbook, width=30,text="Enter book name")

        authorlabel=Label(addbook,text="Enter author name")
        author=Entry(addbook, width=30,text="Enter author name")

        quantitylabel=Label(addbook,text="Enter quantity")
        quantity=Entry(addbook, width=30,text="Enter quantity")

        submit=Button(addbook,text="Submit",
                      command=lambda: self.submitbookdetails(title.get(),author.get(),quantity.get()))
        
        titlelabel.pack(pady=10)
        title.pack(pady=10)
        authorlabel.pack(pady=10)
        author.pack(pady=10)
        quantitylabel.pack(pady=10)
        quantity.pack(pady=10)
        submit.pack(pady=10)
        home=Button(addbook,text="Home",command=self.returnhome)
        home.pack(pady=10)
    
    def submitbookdetails(self, title, author, quantity):
        if not title or not author or not quantity:
            messagebox.showerror("Error", "All fields are required")
            return 
        try:
            with open("books.json", "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        book_exists = False
        for book in data:
            if book.get("title") == title and book.get("author") == author:
                book["quantity"] = str(int(book["quantity"]) + int(quantity))
                book["available"] = str(int(book["available"]) + int(quantity))
                book_exists = True
                break
        if not book_exists:
            new_book = {
                "id": str(len(data) + 1),
                "title": title,
                "author": author,
                "quantity": str(quantity),
                "available": str(quantity)
            }
            data.append(new_book)

        with open("books.json", "w") as file:
            json.dump(data, file, indent=4)
        messagebox.showinfo("Success", "Book added successfully with book id " + str(len(data)))
        self.options()

    def borrowbook(self):
        for i in self.root.winfo_children():
            i.pack_forget()
        borrowbook=Frame(self.root, bg="sky blue")
        borrowbook.pack(fill=BOTH, expand=True)
        title = Label(borrowbook, text="Library Management System", 
                      font=("times new roman", 20, "bold"), bg="blue", fg="black",border=12, relief=GROOVE)
        title.pack(side=TOP, fill=X)

        titlelabel=Label(borrowbook,text="Enter book name")
        title=Entry(borrowbook, width=30,text="Enter book name")

        authorlabel=Label(borrowbook,text="Enter author name")
        author=Entry(borrowbook, width=30,text="Enter author name")

        submit=Button(borrowbook,text="Submit",
                      command=lambda: self.borrowbookdetails(title.get(),author.get()))
        
        titlelabel.pack(pady=10)
        title.pack(pady=10)
        authorlabel.pack(pady=10)
        author.pack(pady=10)
        submit.pack(pady=10)
        home=Button(borrowbook,text="Home",command=self.returnhome)
        home.pack(pady=10)

    def borrowbookdetails(self, title, author):
        if not title or not author:
            messagebox.showerror("Error", "All fields are required")
            return
        try:
            with open("books.json", "r") as file:
                books_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            books_data = []
        book_exists = False
        for book in books_data:
            if book.get("title") == title and book.get("author") == author:
                if int(book.get("available")) > 0:
                    book["available"] = str(int(book["available"]) - 1)  
                    book_exists = True
                    book_id = book["id"]
                    break
                else:
                    messagebox.showerror("Error", "Book not available")
                    return
        
        if not book_exists:
            messagebox.showerror("Error", "Book not found")
            return
        try:
            with open("user.json", "r") as file:
                users_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            users_data = []

        memberid = id  
        if not memberid:
            messagebox.showerror("Error", "Member not logged in or not found")
            return
        try:
            with open("borrow.json", "r") as file:
                borrow_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            borrow_data = []
        new_borrow = {
            "bookid": book_id,
            "memberid": memberid,
            "borrowed_at": str(datetime.now().strftime("%Y-%m-%d"))
        }
        borrow_data.append(new_borrow)

        # Save updated borrow.json
        with open("borrow.json", "w") as file:
            json.dump(borrow_data, file, indent=4)
        with open("books.json", "w") as file:
            json.dump(books_data, file, indent=4)
        messagebox.showinfo("Success", "Book borrowed successfully")
        self.options()

    def retrunbook(self):
        for i in self.root.winfo_children():
            i.pack_forget()
        returnbook=Frame(self.root, bg="sky blue")
        returnbook.pack(fill=BOTH, expand=True)
        title = Label(returnbook, text="Library Management System", 
                      font=("times new roman", 20, "bold"), bg="blue", fg="black",border=12, relief=GROOVE)
        title.pack(side=TOP, fill=X)

        titlelabel=Label(returnbook,text="Enter book name")
        title=Entry(returnbook, width=30,text="Enter book name")

        authorlabel=Label(returnbook,text="Enter author name")
        author=Entry(returnbook, width=30,text="Enter author name")

        submit=Button(returnbook,text="Submit",
                      command=lambda: self.returnbookdetails(title.get(),author.get()))
        
        titlelabel.pack(pady=10)
        title.pack(pady=10)
        authorlabel.pack(pady=10)
        author.pack(pady=10)
        submit.pack(pady=10)
        home=Button(returnbook,text="Home",command=self.returnhome)
        home.pack(pady=10)

    def returnbookdetails(self, title, author):
        if not title or not author:
            messagebox.showerror("Error", "All fields are required")
            return
        try:
            with open("books.json", "r") as file:
                books_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            books_data = []
        book_exists = False
        for book in books_data:
            if book.get("title") == title and book.get("author") == author:
                book["available"] = str(int(book["available"]) + 1)
                book_exists = True
                book_id = book["id"]
                break
        if not book_exists:
            messagebox.showerror("Error", "Book not found")
            return
        try:
            with open("borrow.json", "r") as file:
                borrow_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            borrow_data = []
        memberid = id
        if not memberid:
            messagebox.showerror("Error", "Member not logged in or not found")
            return
        book_exists = False
        for borrow in borrow_data:
            if borrow.get("bookid") == book_id and borrow.get("memberid") == memberid:
                borrow_data.remove(borrow)
                book_exists = True
                break
        if not book_exists:
            messagebox.showerror("Error", "Book not borrowed")
            return
        with open("borrow.json", "w") as file:
            json.dump(borrow_data, file, indent=4)
        with open("books.json", "w") as file:
            json.dump(books_data, file, indent=4)
        messagebox.showinfo("Success", "Book returned successfully")
        self.options()

if __name__ == "__main__":
    root = Tk()
    app = LibraryManagement(root)
    root.mainloop()