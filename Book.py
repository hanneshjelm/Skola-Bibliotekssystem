class Book:
    def __init__(self, title, author, year, summary):
        self.title = title
        self.author = author
        self.year = year
        self.summary = summary
        self.borrowed_by = None

    def __str__(self):
        if self.borrowed_by is not None:
            status = f"Utlånad till {self.borrowed_by.username}"
        else:
            status = "Tillgänglig"

        return f"{self.title} av {self.author}, utgivet år {self.year}, Sammanfattning: {self.summary}, Status: {status}"