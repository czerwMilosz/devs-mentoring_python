from datetime import datetime

class Note:
    def __init__(self, author:str, text:str) -> None:
        self.author = author
        self.text = text
        self.time = datetime.now().strftime("%H:%M")

    def __str__(self) -> str:
        return f"{self.author} {self.text} {self.time}"


class Notebook:
    def __init__(self):
        self.notes = []

    def add_note(self, note:Note) -> None:
        self.notes.append(note)

    def add_new_note(self, author:str, text:str) -> None:
        note = Note(author, text)
        self.notes.append(note)

    def count_notes(self) -> int:
        return len(self.notes)

    def show_notes(self) -> None:
        if not self.notes:
            print("No notes in notebook")
            return

        for note in self.notes:
            print(note)

def main():
    note1 = Note("baba", "jaga")
    print(note1)
    nb = Notebook()
    nb.add_new_note("aba", "aga")
    nb.add_note(note1)
    print(f"Number of notes: {nb.count_notes()}")
    nb.show_notes()


if __name__ == "__main__":
    main()