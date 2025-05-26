"""
Aplikacja do analizy i wizualizacji danych z ankiety powitalnej.

Autor: Alan Steinbarth (alan.steinbarth@gmail.com)
GitHub: https://github.com/AlanSteinbarth
Data: 26.05.2025
Wersja: 2.1.0

Aplikacja umożliwia interaktywne przeglądanie i filtrowanie danych z ankiety,
prezentując wyniki w formie różnorodnych wizualizacji przy użyciu Streamlit.
"""

# ============================================================================
# IMPORT BIBLIOTEK
# ============================================================================
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

# ============================================================================
# KONFIGURACJA APLIKACJI I WCZYTANIE DANYCH
# ============================================================================

def load_data():
    """
    Wczytuje dane z pliku CSV z ankiety powitalnej.
    
    Returns:
        pd.DataFrame: Oczyszczone dane ankiety
    """
    return pd.read_csv("35__welcome_survey_cleaned.csv", sep=";")

def setup_page_config():
    """
    Konfiguruje podstawowe ustawienia strony Streamlit.
    """
    st.set_page_config(
        page_title="Ankieta Powitalna - Analiza Danych",
        page_icon="📋",
        layout="wide",
        initial_sidebar_state="expanded"
    )

# Wczytanie danych
df = load_data()

# Nagłówek aplikacji
st.title("📋 Ankieta powitalna 🙋")
st.markdown("### Interaktywna analiza danych z ankiety powitalnej")
st.dataframe(df.head(), hide_index=True)

# ============================================================================
# DEFINICJE STAŁYCH I KATEGORII
# ============================================================================

# Predefiniowane kolejności kategorii dla lepszego sortowania wykresów
age_order = ["<18", "18-24", "25-34", "35-44", "45-54", "55-64", ">=65", "unknown"]
years_of_experience_order = ["0-2", "3-5", "6-10", "11-15", ">=16"]

# Mapowanie hobby na odpowiednie kolumny w DataFrame
hobby_mapping = {
    "sztuka": "hobby_art",
    "książki": "hobby_books", 
    "filmy i seriale": "hobby_movies", 
    "sport": "hobby_sport", 
    "gry video": "hobby_video_games", 
    "inne": "hobby_other",
}

# ============================================================================
# PANEL BOCZNY - FILTRY DANYCH
# ============================================================================

def create_sidebar_filters():
    """
    Tworzy panel boczny z filtrami do interaktywnego filtrowania danych.
    
    Returns:
        dict: Słownik z wybranymi wartościami filtrów
    """
    with st.sidebar:
        st.write("# 🔧 Wybierz filtr dla danych:")
        
        # Filtr płci
        gender = st.radio(
            "👥 Płeć:",
            ["Wszyscy", "Kobiety", "Mężczyźni"],
            help="Wybierz płeć respondentów do analizy"
        )

        # Filtr wieku
        age_categories = st.multiselect(
            "🎂 Przedział wiekowy:",
            age_order,
            default=[],
            placeholder="Wybierz przedziały wiekowe",
            help="Wybierz jeden lub więcej przedziałów wiekowych"     
        )

        # Filtr doświadczenia zawodowego
        years_of_experience_categories = st.multiselect(
            "💼 Ile lat doświadczenia?",
            years_of_experience_order,
            default=[],
            placeholder="Wybierz lata doświadczenia",
            help="Wybierz przedziały lat doświadczenia zawodowego"
        )

        # Filtr specjalizacji
        industry_categories = st.multiselect(
            "🎯 Specjalizacja:",
            sorted(df["industry"].dropna().unique()),
            placeholder="Wybierz specjalizacje",
            help="Wybierz obszary specjalizacji zawodowej"
        )
        
        # Filtr hobby
        hobby_categories = st.multiselect(
            "🎨 Jakie hobby?",
            options=hobby_mapping.keys(),
            placeholder="Wybierz hobby",
            help="Wybierz zainteresowania i hobby"
        )

        # Filtr preferencji przekąsek
        sweet_or_salty = st.radio(
            "🍿 Ulubiona przekąska?",
            ["Jem wszystko", "Słodka", "Słona"],
            help="Wybierz preferencje dotyczące przekąsek"    
        )
        
    return {
        'gender': gender,
        'age_categories': age_categories,
        'years_of_experience_categories': years_of_experience_categories,
        'industry_categories': industry_categories,
        'hobby_categories': hobby_categories,
        'sweet_or_salty': sweet_or_salty
    }

# ============================================================================
# FUNKCJE FILTROWANIA DANYCH
# ============================================================================

def apply_filters(df, filters):
    """
    Aplikuje wybrane filtry do DataFrame z danymi ankiety.
    
    Args:
        df (pd.DataFrame): Oryginalne dane ankiety
        filters (dict): Słownik z wartościami filtrów
        
    Returns:
        pd.DataFrame: Przefiltrowane dane
    """
    filtered_df = df.copy()
    
    # Filtrowanie według wieku
    if filters['age_categories']:
        filtered_df = filtered_df[filtered_df["age"].isin(filters['age_categories'])]

    # Filtrowanie według płci
    if filters['gender'] == "Mężczyźni":
        filtered_df = filtered_df[filtered_df["gender"] == 0]
    elif filters['gender'] == "Kobiety":
        filtered_df = filtered_df[filtered_df["gender"] == 1]   

    # Filtrowanie według doświadczenia zawodowego
    if filters['years_of_experience_categories']:
        filtered_df = filtered_df[filtered_df["years_of_experience"].isin(filters['years_of_experience_categories'])]

    # Filtrowanie według preferencji przekąsek
    if filters['sweet_or_salty'] == "Słodka":
        filtered_df = filtered_df[filtered_df["sweet_or_salty"] == "sweet"]
    elif filters['sweet_or_salty'] == "Słona":
        filtered_df = filtered_df[filtered_df["sweet_or_salty"] == "salty"]

    # Filtrowanie według specjalizacji
    if filters['industry_categories']:
        filtered_df = filtered_df[filtered_df["industry"].isin(filters['industry_categories'])]

    # Filtrowanie według hobby
    if filters['hobby_categories']:
        selected_columns = [hobby_mapping[hobby_name] for hobby_name in filters['hobby_categories']]
        filtered_df = filtered_df[filtered_df[selected_columns].sum(axis=1) > 0]
    
    return filtered_df

# ============================================================================
# GŁÓWNA LOGIKA APLIKACJI
# ============================================================================

# Utworzenie filtrów i aplikacja ich do danych
filters = create_sidebar_filters()
df_filtered = apply_filters(df, filters)

# ============================================================================
# SEKCJA METRYK PODSUMOWUJĄCYCH
# ============================================================================

def display_summary_metrics(df):
    """
    Wyświetla metryki podsumowujące liczbę respondentów.
    
    Args:
        df (pd.DataFrame): Przefiltrowane dane ankiety
    """
    st.markdown("## 📊 Podsumowanie")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            "👥 Wszyscy ankietowani", 
            len(df),
            help="Całkowita liczba respondentów po zastosowaniu filtrów"
        )

    with col2:
        women_count = len(df[df["gender"] == 1])
        st.metric(
            "👩 Liczba kobiet", 
            women_count,
            help="Liczba kobiet w przefiltrowanych danych"
        )

    with col3:
        men_count = len(df[df["gender"] == 0])
        st.metric(
            "👨 Liczba mężczyzn", 
            men_count,
            help="Liczba mężczyzn w przefiltrowanych danych"
        )

display_summary_metrics(df_filtered)

# ============================================================================
# SEKCJA PRÓBEK DANYCH
# ============================================================================

def display_random_sample(df, sample_size=10):
    """
    Wyświetla losową próbkę danych z tabeli.
    
    Args:
        df (pd.DataFrame): Dane do próbkowania
        sample_size (int): Rozmiar próbki
    """
    st.markdown("## 🎲 Losowe próbki danych")
    st.markdown("Poniżej przedstawiono losowo wybrane odpowiedzi z ankiety:")
    
    actual_sample_size = min(sample_size, len(df))
    if actual_sample_size > 0:
        sample_df = df.sample(actual_sample_size)
        st.dataframe(
            sample_df,
            use_container_width=True,
            hide_index=True
        )
    else:
        st.warning("Brak danych spełniających wybrane kryteria filtrowania.")

display_random_sample(df_filtered)

# ============================================================================
# SEKCJA WIZUALIZACJI DANYCH
# ============================================================================

def create_age_chart(df):
    """
    Tworzy wykres słupkowy dla rozkładu wieku.
    
    Args:
        df (pd.DataFrame): Dane do wizualizacji
    """
    st.markdown("## 📈 Rozkład wieku")
    if not df.empty:
        age_counts = df.groupby("age").size()
        st.bar_chart(
            age_counts, 
            x_label="Przedziały wiekowe", 
            y_label="Liczba ankietowanych"
        )
    else:
        st.info("Brak danych do wyświetlenia wykresu wieku.")

def create_gender_pie_chart(df):
    """
    Tworzy wykres kołowy dla rozkładu płci.
    
    Args:
        df (pd.DataFrame): Dane do wizualizacji
    """
    st.markdown("## ⚧ Rozkład płci")
    if not df.empty and df["gender"].notna().any():
        gender_counts = df["gender"].value_counts()
        gender_counts = gender_counts.rename({0: "Mężczyźni", 1: "Kobiety"})
        
        fig = px.pie(
            values=gender_counts.values, 
            names=gender_counts.index, 
            title="Wykres kołowy dla rozkładu płci"
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Brak danych do wyświetlenia wykresu płci.")

def create_education_chart(df):
    """
    Tworzy wykres słupkowy dla poziomu wykształcenia.
    
    Args:
        df (pd.DataFrame): Dane do wizualizacji
    """
    st.markdown("## 🎓 Poziom wykształcenia")
    if not df.empty:
        edu_counts = df.groupby("edu_level").size()
        st.bar_chart(
            edu_counts, 
            x_label="Wykształcenie", 
            y_label="Liczba ankietowanych"
        )
    else:
        st.info("Brak danych do wyświetlenia wykresu wykształcenia.")

def create_animals_chart(df):
    """
    Tworzy wykres słupkowy dla ulubionych zwierząt.
    
    Args:
        df (pd.DataFrame): Dane do wizualizacji
    """
    st.markdown("## 🐕 Ulubione zwierzęta")
    if not df.empty:
        animals_counts = df.groupby("fav_animals").size()
        st.bar_chart(
            animals_counts, 
            y_label="Liczba ankietowanych"
        )
    else:
        st.info("Brak danych do wyświetlenia wykresu zwierząt.")

def create_places_pie_chart(df):
    """
    Tworzy wykres kołowy dla ulubionych miejsc.
    
    Args:
        df (pd.DataFrame): Dane do wizualizacji
    """
    st.markdown("## 🏖️ Ulubione miejsca do spędzania wolnego czasu")
    if not df.empty and df["fav_place"].notna().any():
        fav_place_counts = df["fav_place"].value_counts()
        fig = px.pie(
            values=fav_place_counts.values, 
            names=fav_place_counts.index
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Brak danych do wyświetlenia wykresu miejsc.")

def create_industry_chart(df):
    """
    Tworzy wykres słupkowy dla specjalizacji zawodowej.
    
    Args:
        df (pd.DataFrame): Dane do wizualizacji
    """
    st.markdown("## 💼 Aktualna specjalizacja zawodowa")
    if not df.empty:
        industry_counts = df.groupby("industry").size()
        st.bar_chart(
            industry_counts, 
            y_label="Liczba ankietowanych"
        )
    else:
        st.info("Brak danych do wyświetlenia wykresu specjalizacji.")

def create_interactive_charts(df):
    """
    Tworzy interaktywne wykresy dla hobby, preferencji nauki i motywacji.
    
    Args:
        df (pd.DataFrame): Dane do wizualizacji
    """
    st.markdown("## 🎮 Szczegółowa analiza preferencji")
    
    if df.empty:
        st.info("Brak danych do wyświetlenia szczegółowych analiz.")
        return
    
    # Definicje kolumn dla różnych kategorii
    hobby_columns = [
        "hobby_art", "hobby_books", "hobby_movies", 
        "hobby_sport", "hobby_video_games", "hobby_other"
    ]
    
    learning_pref_columns = [
        "learning_pref_books", "learning_pref_chatgpt", "learning_pref_offline_courses", 
        "learning_pref_online_courses", "learning_pref_personal_projects", 
        "learning_pref_teaching", "learning_pref_teamwork", "learning_pref_workshops"
    ]
    
    motivation_columns = [
        "motivation_career", "motivation_challenges", "motivation_creativity_and_innovation", 
        "motivation_money_and_job", "motivation_personal_growth", "motivation_remote"
    ]
    
    # Liczenie wystąpień dla hobby
    hobby_counts = (df[hobby_columns] == 1).sum()
    hobby_counts = hobby_counts.rename({
        "hobby_art": "Sztuka",
        "hobby_books": "Książki", 
        "hobby_movies": "Filmy i seriale", 
        "hobby_sport": "Sport", 
        "hobby_video_games": "Gry video", 
        "hobby_other": "Inne"
    })
    
    # Liczenie wystąpień dla preferencji nauki
    learning_pref_counts = (df[learning_pref_columns] == 1).sum()
    learning_pref_counts = learning_pref_counts.rename({
        "learning_pref_books": "Książki", 
        "learning_pref_chatgpt": "ChatGPT", 
        "learning_pref_offline_courses": "Kursy Offline", 
        "learning_pref_online_courses": "Kursy Online", 
        "learning_pref_personal_projects": "Osobiste projekty", 
        "learning_pref_teaching": "Nauczanie", 
        "learning_pref_teamwork": "Współpraca", 
        "learning_pref_workshops": "Warsztaty"
    })
    
    # Liczenie wystąpień dla motywacji
    motivation_counts = (df[motivation_columns] == 1).sum()
    motivation_counts = motivation_counts.rename({
        "motivation_career": "Kariera", 
        "motivation_challenges": "Wyzwania", 
        "motivation_creativity_and_innovation": "Kreatywność i innowacje", 
        "motivation_money_and_job": "Pieniądze i praca", 
        "motivation_personal_growth": "Rozwój osobisty", 
        "motivation_remote": "Praca zdalna"
    })
    
    # Selectbox do wyboru kategorii
    category_options = ['Hobby', 'Preferencje dotyczące nauki', 'Motywacja']
    selected_category = st.selectbox(
        '🔍 Co Cię jeszcze interesuje?', 
        category_options,
        help="Wybierz kategorię do szczegółowej analizy"
    )
    
    # Wyświetlanie odpowiedniego wykresu
    if selected_category == "Hobby":
        st.markdown("### 🎨 Analiza hobby i zainteresowań")
        st.bar_chart(hobby_counts.sort_values(ascending=False))
        
    elif selected_category == "Preferencje dotyczące nauki":
        st.markdown("### 📚 Preferencje dotyczące sposobów nauki")
        st.bar_chart(learning_pref_counts.sort_values(ascending=False))
        
    elif selected_category == "Motywacja":
        st.markdown("### 🎯 Analiza motywacji do rozwoju")
        st.bar_chart(motivation_counts.sort_values(ascending=False))

def create_gender_industry_comparison(df):
    """
    Tworzy wykres porównawczy specjalizacji według płci.
    
    Args:
        df (pd.DataFrame): Dane do wizualizacji
    """
    st.markdown("## ⚖️ Rozkład specjalizacji według płci")
    
    if df.empty:
        st.info("Brak danych do wyświetlenia porównania.")
        return
        
    # Grupowanie danych według płci i specjalizacji
    grouped_data = df.groupby(["gender", "industry"]).size().reset_index(name="count")
    
    if not grouped_data.empty:
        # Tworzenie tabeli przestawnej
        pivot_df = grouped_data.pivot(
            index="industry", 
            columns="gender", 
            values="count"
        ).fillna(0)
        
        # Zmiana nazw kolumn na bardziej czytelne
        pivot_df.columns = pivot_df.columns.map({0: "Mężczyźni", 1: "Kobiety"})
        
        st.bar_chart(pivot_df)
    else:
        st.info("Brak danych do porównania specjalizacji według płci.")

# ============================================================================
# WYŚWIETLANIE WSZYSTKICH WIZUALIZACJI
# ============================================================================

# Wyświetlanie podstawowych wykresów demograficznych
create_age_chart(df_filtered)
create_gender_pie_chart(df_filtered)
create_education_chart(df_filtered)
create_animals_chart(df_filtered)
create_places_pie_chart(df_filtered)
create_industry_chart(df_filtered)

# Wyświetlanie interaktywnych analiz
create_interactive_charts(df_filtered)

# Wyświetlanie porównań zaawansowanych
create_gender_industry_comparison(df_filtered)

# ============================================================================
# STOPKA APLIKACJI
# ============================================================================

st.markdown("---")
st.markdown("""
### 👨‍💻 Informacje o aplikacji

**Autor**: Alan Steinbarth  
**Email**: alan.steinbarth@gmail.com  
**GitHub**: [AlanSteinbarth](https://github.com/AlanSteinbarth)  
**Repozytorium**: [Filtrowanie-danych-z-ankiety](https://github.com/AlanSteinbarth/Filtrowanie-danych-z-ankiety)

Aplikacja została stworzona przy użyciu **Streamlit** do interaktywnej analizy danych z ankiety powitalnej.
""")