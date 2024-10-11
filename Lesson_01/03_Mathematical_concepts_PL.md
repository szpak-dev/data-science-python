### **Koncepcje Matematyczne w Data Science (15-20 min)**

---

#### **1. Wprowadzenie do Modelowania Matematycznego i jego Znaczenia w Data Science**

Modelowanie matematyczne to proces używania struktur i relacji matematycznych do reprezentowania scenariuszy ze świata rzeczywistego. W data science modele pomagają przewidywać wyniki, rozpoznawać wzorce i podejmować decyzje na podstawie danych. Modele te stanowią fundament algorytmów uczenia maszynowego, w których funkcje matematyczne są trenowane na danych w celu uzyskania wglądów lub prognozowania.

**Kluczowe powody, dla których modelowanie matematyczne jest kluczowe w data science:**

- **Modelowanie predykcyjne:** Rozumienie trendów i przewidywanie na podstawie danych z przeszłości.
- **Optymalizacja:** Znajdowanie najlepszego rozwiązania problemów, takich jak maksymalizacja zysków lub minimalizacja kosztów.
- **Symulacja:** Naśladowanie procesów ze świata rzeczywistego w celu analizy i prognozowania.

---

#### **2. Koncepcje Algebry Liniowej: Wektory, Macierze i Operacje na Macierzach**

Algebra liniowa dostarcza narzędzi matematycznych do obsługi danych wielowymiarowych, a wiele algorytmów uczenia maszynowego opiera się na koncepcjach algebry liniowej.

##### **2.1 Wektory**
Wektor to jednowymiarowa tablica liczb. Może reprezentować cechy w zbiorze danych (np. wektor wieku, dochodu i wskaźnika wydatków dla klienta). Wektory są przydatne do wyrażania punktów w przestrzeni lub reprezentowania zbiorów danych w uczeniu maszynowym.

**Przykład: Tworzenie i Manipulacja Wektorami w Pythonie**

```python
import numpy as np

# Tworzenie wektorów
v1 = np.array([2, 3, 5])   # Wektor z trzema elementami
v2 = np.array([1, 0, 4])

# Dodawanie wektorów
v_sum = v1 + v2  # [3, 3, 9]

# Iloczyn skalarny (używany w uczeniu maszynowym do obliczania podobieństwa między wektorami)
dot_product = np.dot(v1, v2)  # 2*1 + 3*0 + 5*4 = 22
```

**Znaczenie w Budowaniu Modeli**
W regresji liniowej stosuje się wektor wag (współczynników) na danych wejściowych (cechach), aby przewidzieć zmienną docelową. Iloczyn skalarny jest często używany w algorytmach klasyfikacji do określenia podobieństwa między wektorami (np. obliczanie odległości w grupowaniu).

##### **2.1.1 Czym jest Iloczyn Skalarny**
Iloczyn skalarny (zwany także iloczynem skalarowym) to operacja matematyczna, która bierze dwie sekwencje liczb o równej długości (zwykle wektory) i zwraca jedną liczbę. Jest to suma iloczynów odpowiadających sobie elementów z dwóch wektorów.

Wyobraź sobie, że masz dwa pociągi zabawkowe, a każdy pociąg ma trzy wagony. Jeden pociąg ma czerwone wagony, a drugi niebieskie. W każdym wagonie znajdują się kulki.

- Czerwony pociąg ma **2, 3 i 5** kulek w swoich wagonach.
- Niebieski pociąg ma **1, 0 i 4** kulki w swoich wagonach.

Teraz, co robimy w iloczynie skalarnym, jest proste:

1. Mnożymy liczbę kulek w pierwszym wagonie czerwonego pociągu (2) przez liczbę kulek w pierwszym wagonie niebieskiego pociągu (1). Więc 2 razy 1 = 2.
2. Następnie mnożymy kulki w drugim wagonie czerwonego pociągu (3) przez kulki w drugim wagonie niebieskiego pociągu (0). Więc 3 razy 0 = 0.
3. Na koniec mnożymy kulki w trzecim wagonie czerwonego pociągu (5) przez kulki w trzecim wagonie niebieskiego pociągu (4). Więc 5 razy 4 = 20.

Następnie dodajemy te wyniki razem: 2 + 0 + 20 = **22**.

To jest iloczyn skalarny! To tylko mnożenie odpowiadających sobie wagonów i dodawanie wyników.

##### **2.1.2 Przykłady Iloczynu Skalarnego w Życiu Codziennym**
1. **Podobieństwo Cosinusowe w NLP:** W przetwarzaniu języka naturalnego (NLP) iloczyn skalarny jest używany do obliczania podobieństwa cosinusowego między dwoma wektorami słów, aby zmierzyć podobieństwo ich znaczeń. Jest to często wykorzystywane w wyszukiwarkach i systemach rekomendacji.

2. **Fizyka:** Iloczyn skalarny jest używany do obliczania pracy wykonanej przez siłę. Na przykład, jeśli siła jest przyłożona do obiektu pod pewnym kątem, praca wykonana to iloczyn skalarny wektorów siły i przemieszczenia.

3. **Ekonomia:** Iloczyn skalarny może być używany do obliczania ważonej średniej zwrotów z różnych aktywów, gdzie wagi reprezentują proporcję inwestycji, a wartości reprezentują zwroty z każdego aktywa.

4. **Uczenie Maszynowe:** W modelach klasyfikacyjnych iloczyn skalarny wektora cech wejściowych i wektora wag modelu pomaga określić przewidywaną klasę.

---

##### **2.2 Macierze**
Macierz to dwuwymiarowa tablica liczb, powszechnie używana do reprezentowania zbiorów danych. Wiersze w macierzy zazwyczaj reprezentują punkty danych, podczas gdy kolumny reprezentują cechy.

**Przykład: Tworzenie i Mnożenie Macierzy w Pythonie**

```python
# Tworzenie macierzy
matrix1 = np.array([[1, 2], [3, 4]])  # Macierz 2x2
matrix2 = np.array([[5, 6], [7, 8]])  # Inna macierz 2x2

# Dodawanie macierzy
matrix_sum = matrix1 + matrix2  # Dodawanie elementów

# Mnożenie macierzy (iloczyn skalarny)
matrix_product = np.dot(matrix1, matrix2)
```

**Operacje na Macierzach w Uczeniu Maszynowym**
Mnożenie macierzy: W regresji liniowej macierz cech wejściowych jest mnożona przez wektor współczynników (wag), aby dokonać prognoz. Operacja ta jest wydajna, gdyż skaluje się na wiele punktów danych i cech.

**Przykład:** W postaci macierzy model liniowy można wyrazić jako:

\[
\mathbf{y} = \mathbf{X} \cdot \mathbf{w}
\]

Gdzie:

- \( \mathbf{X} \) to macierz cech (punkty danych jako wiersze, cechy jako kolumny),
- \( \mathbf{w} \) to wektor wag,
- \( \mathbf{y} \) to prognozowany wynik.

---

##### **2.3 Znaczenie Wektorów i Macierzy w Data Science**
- **Reprezentacja Danych:** Wektory reprezentują punkty danych, podczas gdy macierze reprezentują zbiory danych. Modele uczenia maszynowego działają na macierzach, aby wydobywać wzorce z danych.
- **Wydajna Obliczalność:** Operacje na wektorach i macierzach (takie jak dodawanie, mnożenie i iloczyny skalarne) pozwalają na efektywne trenowanie modeli, nawet na dużych zbiorach danych.
- **Transformacje:** Transformacje danych (np. skalowanie, normalizacja) często wymagają operacji na macierzach.
- **Redukcja Wymiarowości:** Algorytmy takie jak analiza głównych składowych (PCA) wykorzystują operacje na macierzach, aby zmniejszyć liczbę cech, zachowując jednocześnie większość zmienności danych.

---

#### **3. Modele Liniowe i Reprezentacja Macierzy**
Najbardziej podstawowym modelem w uczeniu maszynowym jest regresja liniowa, w

 której używamy linii (lub hiperpłaszczyzny w wyższych wymiarach), aby dopasować dane.

**Wzór regresji liniowej:**
\[
y = w_1 x_1 + w_2 x_2 + \dots + w_n x_n + b
\]

Gdzie:

- \( x_1, x_2, \dots, x_n \) to cechy wejściowe,
- \( w_1, w_2, \dots, w_n \) to wagi (współczynniki),
- \( b \) to człon biasu,
- \( y \) to prognozowana wartość.

W postaci macierzy można to zapisać jako:
\[
\mathbf{y} = \mathbf{X} \cdot \mathbf{w} + b
\]

Ta zwarta forma ułatwia obliczenia i czyni je bardziej wydajnymi.

**Przykład: Implementacja Regresji Liniowej w Pythonie**

```python
# Macierz cech (X) i wektor wag (w)
X = np.array([[1, 2], [3, 4], [5, 6]])  # Każdy wiersz to punkt danych
w = np.array([0.4, 0.6])  # Wagi dla każdej cechy

# Prognozowanie wyniku (y) za pomocą mnożenia macierzy
y = np.dot(X, w)
print(y)
```

---

### **Podsumowanie**
Modelowanie matematyczne jest niezbędne w data science do budowania modeli predykcyjnych. Wektory i macierze dostarczają ramy do reprezentowania i manipulowania danymi w sposób wydajny. Operacje algebry liniowej, takie jak mnożenie macierzy, są kluczowe dla wielu algorytmów uczenia maszynowego, szczególnie dla modeli takich jak regresja liniowa i klasyfikacja.