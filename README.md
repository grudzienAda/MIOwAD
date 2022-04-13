# MIOwAD
Metody inteligencji obliczeniowej w analizie danych (sem. VI)


1.2.1. NN1: Bazowa implementacja (1 tydzień, 2 punkty)

Na tych zajęciach należy zaimplementować sieć neuronową typu MLP, w której można ustawić: liczbę warstw, liczbę neuronów w każdej z warstw i wagi poszczególnych połączeń, w tym biasów. Sieć ma używać sigmoidalnej funkcji aktywacji. Na wyjściu dopuszczana jest funkcja liniowa.

Implementacja sieci musi być przygotowana w taki sposób, żeby łatwo zmieniać:

    - Architekturę, to znaczy liczbę wejść, wyjść, neuronów w warstwach ukrytych.
    - Funkcję aktywacji.

Tak przygotowaną implementację należy następnie wykorzystać do rozwiązania zadania regresji na dostarczonych danych. Parametry sieci należy dobrać ręcznie, tak aby uzyskać możliwie dobrze wyniki na zbiorach danych (zbudować po jednej sieci dla każdego zbioru):

    - square-simple
    - steps-large

Rozważyć architektury sieci:

    - jedna warstwa ukryta, 5 neuronów,
    - jedna warstwa ukryta, 10 neuronów,
    - dwie warstwy ukryte, po 5 neuronów każda.

Aby otrzymać 2 punkty MSE na [nieznormalizowanym] zbiorze testowym nie może przekraczać wartości 9.
1.2.2. NN2: Implementacja propagacji wstecznej błędu (2 tygodnie, 4 punkty)

W ramach tego laboratorium trzeba zaimplementować uczenie sieci neuronowej propagacją wsteczną błędu. Aby sprawdzić implementację, należy wykonać uczenie na prostych danych do uczenia dostarczonych na zajęciach. Następnie należy zaimplementować metodę wizualizacji wartości wag sieci w kolejnych iteracjach i, w przypadku gdy nie udaje się nauczyć sieci, spróbować wykorzystać te wizualizacje do ustalenia przyczyny problemu. Zaimplementować wersję z aktualizacją wag po prezentacji wszystkich wzorców i wersję z aktualizacją po prezentacji kolejnych porcji (batch). Porównać szybkość uczenia dla każdego z wariantów.

Inicjować wagi z rozkładu jednostajnego na przedziale [0,1]. Opcjonalnie zaimplementować inną metodą inicjowania wag. Albo metodę He albo Xavier.

Przetestować uczenie sieci na następujących zbiorach (w nawiasach wartość MSE, aby otrzymać 4 punkty):

    - square-simple (jeśli sieć nie jest w stanie się nauczyć tej funkcji to coś jest bardzo źle zrobione, MSE: 4),
    - steps-small (MSE: 4),
    - multimodal-large (MSE: 40).

(Wartości MSE liczone na nieznormalizowanych danych)
1.2.3. NN3: Implementacja momentu i normalizacji gradientu (1 tydzień, 2 punkty)

Zaimplementować dwa usprawnienia uczenia gradientowego sieci neuronowej:

    - moment,
    - normalizację gradientu RMSProp.

Porównać szybkość zbieżności procesu uczenia dla obu wariantów.

Przeprowadzić eksperymenty na zbiorach(w nawiasach wartość MSE, aby otrzymać 2 punkty):

    - square-large (MSE: 1),
    - steps-large (MSE: 3),
    - multimodal-large (MSE: 9).

Literatura:

    - Uczenie gradientowe z momentem: rozdział 3.2.2 Computational Intelligence, A. P. Engelbrecht
    - Normalizacja gradientu: Wykład 6e: http://www.cs.toronto.edu/~tijmen/csc321/slides/lecture_slides_lec6.pdf

1.2.4. NN4: Rozwiązywanie zadania klasyfikacji (1 tydzień, 2 punkty)

Zaimplementować funkcję softmax dla warstwy wyjściowej sieci neuronowej. Sprawdzić szybkość i skuteczność w wariancie, gdy sieć używa funkcji softmax na ostatniej warstwie i gdy jest użyta zwykła funkcja aktywacji. Softmax wymaga też odpowiednich zmian w algorytmie uczenia, uwzględniających pochodną fukcji.

Przeprowadzić eksperymenty na zbiorach (w nawiasach wymagana wartość F-measure na 2 punkty):

    - rings3-regular (F-measure: 0.75),
    - easy (F-measure: 0.99),
    - xor3 (F-measure: 0.97).

1.2.5. NN5: Testowanie różnych funkcji aktywacji (1 tydzień, 2 punkty)

Należy rozszerzyć istniejącą implementację sieci i metody uczącej o możliwość wyboru funkcji aktywacji:

    - sigmoid,
    - liniowa,
    - tanh,
    - ReLU.

Pytanie dodatkowe – czy wszyscy implementują dokładnie gradient dla funkcji ReLU?

Porównać szybkość uczenia i skuteczność sieci w zależności od liczby neuronów w poszczególnych warstwach i rodzaju funkcji aktywacji. Należy wziąć pod uwagę fakt, że różne funkcje aktywacji mogą dawać różną skuteczność w zależności od liczby neuronów i liczby warstw. Sprawdzić sieci z jedną, dwiema i trzema warstwami ukrytymi. Podobnie jak w poprzednim tygodniu, trzeba dostosować proces uczenia do pochodnych nowych funkcji aktywacji.

Przeprowadzić testy wstępne dla zbioru multimodal-large (regresja), dla wszystkich trzech architektur i wszystkich czterech funkcji aktywacji.

Dla pozostałych zbiorów wybrać dwa najlepsze zestawy i zbadać ich skuteczność:

    - regresja
        - steps-large,
    - klasyfikacja
        - rings5-regular
        - rings3-regular

1.2.6. NN6: Zjawisko przeuczenia + regularyzacja (brak punktów za zadanie, sprawozdanie po tym tygodniu)

Zaimplementować mechanizm regularyzacji wag w sieci oraz mechanizm zatrzymywania uczenia przy wzroście błędu na zbiorze walidacyjnym.

Przeprowadzić eksperymenty na zbiorach i porównać skuteczność na zbiorze testowym dla różnych wariantów przeciwdziałania przeuczeniu sieci:

    - multimodal-sparse,
    - rings5-sparse,
    - rings3-balance,
    - xor3-balance.

Author: Jan Karwowski
