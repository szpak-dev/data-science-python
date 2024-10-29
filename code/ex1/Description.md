## 4. Zadania

1. Zaimplementuj funkcjonalność obliczającą dystans euklidesowy między dwoma punktami 3-wymiarowymi. 
Zastanów się, jak reprezentować punkty.

2. Utwórz plik utility.py i zakoduj w nim funkcję implementującą wyliczanie średniej wszystkich wartości w 
słowniku. Zaimportuj funkcję do notatnika i wykonaj na słowniku data = {'a': 100, 'b': 120, 'c': 130}

3. Utwórz tuplę zawierającą wszystkie litery alfabetu łacińskiego. Utwórz słownik, którego kluczami 
są elementy tupli a wartościami listy n-elementowe, gdzie każdy element to litera w kluczu a n    `zxcvbvcxzsxdcfvcdxszxdcfvgbvfcdxsza``AZSXDCFVBHJ
to numer tej litery w alfabecie (zaczynając od 0). Dla jasności dla tylko pierwszych 3 liter słownik 
wyglądałby tak: {a: [], b: ['b'], c: ['c', 'c']}
★ Spróbuj uzyskać taki sam słownik jedno-linijkowym kodem.

4. Policz, ile słów znajduje się w tekście zawartym w pliku Data_MobyDick.txt.
★ Przygotuj Bag of Words dla tekstu zawartego w pliku Data_MobyDick.txt (Zlicz wystąpienia unikalnych słów bez rozróżniania WIELKICH i małych liter. Wyeliminuj znaki interpunkcyjne itp.) 
* Zadanie może ułatwić Ci pakiet biblioteki standardowej re zawierający zaawansowane operacje na tekście wykorzystujące wyrażenia regularne.

5. Wczytaj plik Dataset_WorldPortIndex.csv. Następnie przygotuj listę obiektów port, które będą instancjami dataclass zawierającymi wybrane informacje na temat odpowiadających portów ze zbioru danych (współrzędne geograficzne, nazwa, kraj, obecność lotniska).
★ Zakładając, że lecę samolotem w punkcie x, w którym najbliższym porcie mogę wylądować?"