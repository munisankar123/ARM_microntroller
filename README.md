# Library management system 


The Library Management with GUI Interface is an intuitive and user-friendly application designed to streamline library management processes. Built using Python's Tkinter library, this system offers a comprehensive set of functionalities for efficiently managing library resources. The core features include the ability to add and update books, register new library members, and track book borrow and return transactions. Through a graphical user interface (GUI), users can easily search for books by title or author, as well as generate detailed reports on borrowed books or available inventory. The system also ensures persistence by saving data to a file (in formats such as JSON) and automatically reloading it upon program restart, ensuring that the library's information is consistently up-to-date. By providing a seamless, interactive experience, the Library Management with GUI Interface enhances library operations, enabling administrators to manage books, members, and transactions efficiently and effortlessly.


User Registration

•	Upon entering the library, the application checks if the user is already registered.

•	If not, the user is directed to the registration desk.

•	At the desk, they provide their name and contact number.

•	The system then registers the user, assigns them a unique ID, and grants them access to the library.

•	User details are stored in JSON format for enhanced readability and efficient data access.

Library Services

After entering the library, the user is provided with various services, including the ability to:
Add Books:

•	The user can add new books to the library by specifying the book name, author name, and quantity.

•	If additional copies of an existing book are being added, the system updates the existing record instead of creating a new one.

•	All added books are saved in the books.json file with fields for book ID, book name, author name, total quantity, and available quantity.

Borrow Books:

•	The user can borrow books from the library by providing the title and author of the desired book.

•	When a book is borrowed, the available quantity is decreased by one, and a record of the borrowed book ID, user ID, and borrowing date is stored.

•	If the user attempts to borrow an unavailable book, a warning is raised.

Return Books:

•	The user can return borrowed books to the library after finishing reading them.

•	When a book is returned, the available quantity is increased, and the updated information is stored in the books.json file.

Search Books:

•	The user can view a list of all books by clicking on a "details" button.

•	Alternatively, they can search for a specific book to determine its availability in the library.



![Screenshot 2024-12-27 002836](https://github.com/user-attachments/assets/9bd76779-5cf5-4a6c-84f5-96947d0ab2a0)
![Screenshot 2024-12-27 002859](https://github.com/user-attachments/assets/7e3afd82-8c07-466b-8572-6d944b2c9db4)
![Screenshot 2024-12-27 002734](https://github.com/user-attachments/assets/e8ba505f-165f-412f-8cad-8f18a189ca4a)

