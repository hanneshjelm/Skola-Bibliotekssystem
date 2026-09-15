from Book import Book
from User import User

books = [
    Book("Pippi Långstrump", "Astrid Lindgren", 1945, "Pippi flyttar in i Villa Villekulla."),
    Book("Bröderna Lejonhjärta", "Astrid Lindgren", 1973, "En berättelse om mod och kärlek."),
    Book("Harry Potter och de vises sten", "J.K. Rowling", 1997, "Harry börjar på Hogwarts."),
    Book("Sagan om ringen", "J.R.R. Tolkien", 1954, "En farlig resa för att förstöra en mäktig ring."),
    Book("Mio, min Mio", "Astrid Lindgren", 1954, "Mio upptäcker sitt kungliga arv.")
]

users = [
    User("admin", "adminpass", "admin"),
    User("testuser", "testpass", "user")
]

def add_book():
    title = input("Ange boktitel: ")
    author = input("Ange författare: ")

    while True:
        try:
            year = int(input("Ange utgivningsår: "))
            break
        except ValueError:
            print("Ogiltigt årtal. Försök igen.")
    
    summary = input("Ange sammanfattning: ")
    book = Book(title, author, year, summary)
    books.append(book)
    print(f"'{title}' tillagd i biblioteket.")

def show_books():
    if not books:
        print("Inga böcker tillgängliga.")
    else:
        for i, book in enumerate(books, start = 1):
            print(f"\n{i}. {book}")

    input("\nTryck Enter för att återvända till menyn.")

def search_books_by_title_or_author():
    search_term = input("Ange titel eller författare att söka efter: ").strip().lower()
    found_books = []

    for book in books:
        if search_term in book.title.lower() or search_term in book.author.lower():
            found_books.append(book)

    if not found_books:
        print(f"Hittade inga böcker med titel eller författare som innehåller '{search_term}'.")
    else:
        for i, book in enumerate(found_books, start = 1):
            print(f"\n{i}. {book}")

    input("\nTryck Enter för att återvända till menyn.")

def get_selection(items):
    while True:
        try:
            selection = int(input("\nSkriv numret du vill välja (0 för att avbryta): "))

            if selection == 0:
                print("Återgår till menyn.")
                return

            if 1 <= selection <= len(items):
                return items[selection - 1]

            print("Ogiltigt val. Försök igen.")

        except ValueError:
            print("Ogiltigt val. Försök igen.")

def borrow_book(current_user):
    available_books = []
    for book in books:
        if book.borrowed_by is None:
            available_books.append(book)

    if not available_books:
        print("Det finns inga tillgängliga böcker att låna.")
        return

    for i, book in enumerate(available_books, start = 1):
        print(f"\n{i}. {book.title} av {book.author} ({book.year})")

    selected_book = get_selection(available_books)
    if selected_book is None:
        return
    
    selected_book.borrowed_by = current_user
    print(f"Du har lånat '{selected_book.title}' av {selected_book.author}.")
    input("\nTryck Enter för att återvända till menyn.")

def return_book(current_user):
    borrowed_books = []
    for book in books:
        if book.borrowed_by == current_user:
            borrowed_books.append(book)

    if not borrowed_books:
        print("Det finns inga böcker att returnera.")
        return

    for i, book in enumerate(borrowed_books, start = 1):
        print(f"\n{i}. {book.title} av {book.author} ({book.year})")

    selected_book = get_selection(borrowed_books)
    if selected_book is None:
        return

    selected_book.borrowed_by = None
    print(f"Du har returnerat '{selected_book.title}' av {selected_book.author}.")
    input("\nTryck Enter för att återvända till menyn.")

def delete_book():
    if not books:
        print("Det finns inga böcker att ta bort.")
        return

    for i, book in enumerate(books, start = 1):
        print(f"\n{i}. {book.title} av {book.author} ({book.year})")

    selected_book = get_selection(books)
    if selected_book is None:
        return

    if selected_book.borrowed_by is not None:
        print(f"Kan inte ta bort '{selected_book.title}' eftersom den är utlånad.")
        input("\nTryck Enter för att återvända till menyn.")
        return

    books.remove(selected_book)
    print(f"'{selected_book.title}' av {selected_book.author} har tagits bort från biblioteket.")
    input("\nTryck Enter för att återvända till menyn.")

def login():
    username = input("Ange användarnamn: ").strip()
    password = input("Ange lösenord: ")

    for user in users:
        if user.username.lower() == username.lower() and user.password == password:
            print(f"Välkommen {user.username}!")
            return user

    print("Ogiltigt användarnamn eller lösenord.")
    return

def add_user():
    while True:
        username = input("Ange nytt användarnamn: ").strip()
        if not username:
            print("Användarnamnet får inte vara tomt.")
            continue

        if any(user.username.lower() == username.lower() for user in users):
            print("Användarnamnet finns redan. Välj ett annat.")
            continue
        break

    while True:
        password = input("Ange lösenord: ")
        if not password:
            print("Lösenordet får inte vara tomt.")
            continue
        
        if len(password) < 6:
            print("Lösenordet måste vara minst 6 tecken långt.")
            continue
        break

    while True:
        role = input("Ange roll (admin/user): ").lower()
        if role not in ["admin", "user"]:
            print("Ogiltig roll. Använd 'admin' eller 'user'.")
            continue
        break

    new_user = User(username, password, role)
    users.append(new_user)
    print(f"Användare '{username}' med rollen '{role}' har lagts till.")
    input("\nTryck Enter för att återvända till menyn.")

def delete_user(current_user):
    if not users:
        print("Det finns inga användare att ta bort.")
        return

    for i, user in enumerate(users, start = 1):
        print(f"\n{i}. {user.username} ({user.role})")

    selected_user = get_selection(users)
    if selected_user is None:
        return

    if selected_user == current_user:
        print("Du kan inte ta bort den användare som är inloggad.")
        input("\nTryck Enter för att återvända till menyn.")
        return

    for book in books:
        if book.borrowed_by == selected_user:
            book.borrowed_by = None

    users.remove(selected_user)
    print(f"Användare '{selected_user.username}' har tagits bort.")
    input("\nTryck Enter för att återvända till menyn.")

def show_all_borrowed_books():
    borrowed_books = []
    for book in books:
        if book.borrowed_by is not None:
            borrowed_books.append(book)

    if not borrowed_books:
        print("Det finns inga utlånade böcker.")
    else:
        for i, book in enumerate(borrowed_books, start = 1):
            print(f"\n{i}. {book}")

    input("\nTryck Enter för att återvända till menyn.")

def menu(current_user):
    while True:
        print("\nHuvudmeny")
        print("---------")
        print("1. Visa alla böcker")
        print("2. Sök efter bok (titel eller författare)")
        print("3. Låna bok")
        print("4. Returnera bok")

        if current_user.role == "admin":
            print("5. Lägg till bok")
            print("6. Ta bort bok")
            print("7. Visa alla utlånade böcker")
            print("8. Lägg till användare")
            print("9. Ta bort användare")

        print("0. Logga ut")

        choice = input("Välj ett alternativ: ")

        if choice == "1":
            show_books()
        elif choice == "2":
            search_books_by_title_or_author()
        elif choice == "3":
            borrow_book(current_user)
        elif choice == "4":
            return_book(current_user)
        elif choice == "5" and current_user.role == "admin":
            add_book()
        elif choice == "6" and current_user.role == "admin":
            delete_book()
        elif choice == "7" and current_user.role == "admin":
            show_all_borrowed_books()
        elif choice == "8" and current_user.role == "admin":
            add_user()
        elif choice == "9" and current_user.role == "admin":
            delete_user(current_user)
        elif choice == "0":
            print("Loggar ut.")
            return
        else:
            print("Ogiltigt val. Försök igen.")

while True:
    current_user = login()
    if current_user:
        menu(current_user)