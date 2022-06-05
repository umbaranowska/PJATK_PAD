# Zadanie 1 (5 pk)
# Utwórz stronę dash, która:
# a)	Wczyta dane z pliku winequality.csv do tabeli pandas i je wyświetli jako tabelę (10 wierszy).
# b)	Będzie pozwalała na wybór modelu regresji lub klasyfikacji
# (dropdown lista albo radio button albo jeszcze coś innego – wybrać sobie).
# c)	Na podstawie wyboru z pkt. b i funkcji zwrotnej zapewni reakcję łańcuchową.
# W przypadku wyboru regresji ma pokazywać wykres z plotly zależności pH od wybranej przez użytkownika zmiennej,
# a w przypadku wyboru klasyfikacji ma pokazywać zależność target (red/white) od wybranej przez użytkownika innej zmiennej.
# Zastanowić się, który wykres będzie to najlepiej obrazował.

import pandas as pd
import dash