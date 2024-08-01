class Titles:
    def __init__(self, titles:list) -> None:
        self._titles = titles


    def getTitles(self) -> list:
        return self._titles


class KWICGenerator:
    def __init__(self, titles:Titles) -> None:
        self._titles = titles.getTitles()

    def generateKWIC(self) -> list:
        phrasesKWIC = []
        for title in self._titles:
            titleWords = title.split()
            phrase = ""
            for word in titleWords:
                if(word.istitle() or word.isupper()):
                    phrase += "     " + word
                    phrasesKWIC.append(phrase)
                else:
                    phrase += " " + word
        return phrasesKWIC


class KWICDisplay:
    def __init__(self, phrasesKWIC:list) -> None:
        self._phrases = phrasesKWIC

    def display(self) -> None:
        for phrase in self._phrases:
            print(phrase)


titles = Titles(
    [
    "The quick brown fox jumps over Jhonny",
    "she sells sea shells in California",
    "KWIC is an Acronym for keyword in Context",
    "Juan is more handsome than Carlos",
    "he wants to be President of the United States in a nearly future",
    "Anna lives in Arizona and her father's name is Pedro"
    ]
)

generador = KWICGenerator(titles).generateKWIC()
imprimir = KWICDisplay(generador).display()