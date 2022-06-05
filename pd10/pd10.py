# Zadanie 1 (5 pk)
# Utwórz stronę streamlit, która:
# a. Będzie miała dwie zakładki (dwie wersje wyświetlania): Ankieta i Staty (1 pkt)
# b. Na stronie Ankieta: (1 pkt)
# • Ma być pole do wpisania imienia, pole do wpisania nazwiska.
# • Po zapisaniu pola mają wyświetlać na zielono komunikat o poprawnym zapisaniu kwestionariusza.
# c. Na stronie Staty: (3 pkt) •
# Ma być możliwość wczytania danych csv do dataframe;
# • W trakcie wczytania ma być symulacja oczekiwania, np. pasek postępu albo kółeczko.
# • Po wczytaniu danych, ma być możliwość wybrania wykresu o wizualizacji danych (2 wykresy do wyboru).
# Dane do wczytania to np. dane utworzone w 5 pracy domowej (customers.csv)

import streamlit as st
import pandas as pd
import time
import plotly.express as px

st.title('praca domowa 10')
page = st.sidebar.selectbox('Wybierz stronę:', ['ankieta', 'staty'])

# ankieta

if page == 'ankieta':

    imie = st.text_input('Wpisz imię: ')
    nazwisko = st.text_input('Wpisz nazwisko: ')

    if st.button('OK') and imie.isalpha() and nazwisko.isalpha():
        st.success('Formularz wypełniony poprawnie')
        with open('ankieta.txt', 'a') as file:
            file.write('\n')
            file.write(','.join([imie, nazwisko]))
    else:
        st.error('Wpisz poprawne dane')

#staty

if page == 'staty':

    data = st.file_uploader('Wczytaj dane', type = ['csv'])

    if data is not None:
        with st.spinner('Ładowanie...'):
            time.sleep(3)
        df = pd.read_csv(data)
        st.dataframe(df.head(5))

        graph_type = st.selectbox('Wybierz typ wykresu', ('scatterplot', 'barplot'))
        variables_num = tuple(x for x in df.columns if df[x].dtype in ['float', 'int', 'float64', 'int64']) # bardzo uproszczony wybór typów kolumn
        variables_str = tuple(x for x in df.columns if df[x].dtype in ['str', 'object'])

        if graph_type == 'scatterplot':
            x_var = st.selectbox('Wybierz zmienną na osi X', variables_num)
            y_var = st.selectbox('Wybierz zmienną na osi Y', variables_num)
            scatterplot = px.scatter(df, x = x_var, y = y_var)
            st.plotly_chart(scatterplot)

        if graph_type == 'barplot':
            var = st.selectbox('Wybierz zmienną', variables_str)
            df_counts = df[var].value_counts().reset_index()
            barplot = px.bar(df_counts, x = 'index', y = var)
            st.plotly_chart(barplot)