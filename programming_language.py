class ProgrammingLanguage:
    def __init__(self, language, type, reflection, year):
        self.language = language
        self.type = type
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.type == "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        print(f"{self.language}, {self.type} Typing, Reflection={self.reflection}, First appeared in {self.year}")


def get_dynamic():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.language)


if __name__ == "__main__":
    get_dynamic()
