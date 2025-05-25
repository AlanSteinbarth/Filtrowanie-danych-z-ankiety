# 📋 Filtrowanie Danych z Ankiety

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Interaktywna aplikacja webowa do analizy i wizualizacji danych z ankiety powitalnej. Umożliwia przeglądanie, filtrowanie i analizę odpowiedzi z ankiety przy użyciu intuicyjnego interfejsu użytkownika.

## 🚀 Funkcjonalności

- **Interaktywne filtrowanie danych** - według płci, wieku, doświadczenia, specjalizacji i hobby
- **Wizualizacje danych** - wykresy słupkowe, kołowe i metryki
- **Analiza demograficzna** - rozkład respondentów według różnych kryteriów
- **Losowe próbkowanie** - przeglądanie przykładowych odpowiedzi
- **Responsywny interfejs** - optymalizowany dla różnych urządzeń

## 🛠️ Technologie

- **Python 3.8+**
- **Streamlit** - framework do tworzenia aplikacji webowych
- **Pandas** - manipulacja i analiza danych
- **Plotly** - interaktywne wizualizacje
- **Altair** - deklaratywne wizualizacje statystyczne

## 📦 Instalacja

1. **Sklonuj repozytorium:**
```bash
git clone https://github.com/AlanSteinbarth/Filtrowanie-danych-z-ankiety.git
cd Filtrowanie-danych-z-ankiety
```

2. **Utwórz środowisko wirtualne:**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# lub
source venv/bin/activate  # Linux/Mac
```

3. **Zainstaluj zależności:**
```bash
pip install -r requirements.txt
```

4. **Uruchom aplikację:**
```bash
streamlit run app.py
```

5. **Otwórz w przeglądarce:**
Aplikacja będzie dostępna pod adresem: `http://localhost:8501`

## 📊 Dane

Aplikacja wykorzystuje plik `35__welcome_survey_cleaned.csv` zawierający oczyszczone dane z ankiety powitalnej. Dane obejmują:

- Informacje demograficzne (wiek, płeć)
- Poziom wykształcenia
- Doświadczenie zawodowe
- Specjalizację zawodową
- Hobby i zainteresowania
- Preferencje dotyczące nauki
- Motywację do rozwoju

## 🎯 Użytkowanie

1. **Uruchom aplikację** zgodnie z instrukcjami instalacji
2. **Użyj panelu bocznego** do ustawienia filtrów:
   - Wybierz płeć respondentów
   - Określ przedziały wiekowe
   - Wybierz lata doświadczenia
   - Filtruj według specjalizacji
   - Wybierz hobby
   - Określ preferencje przekąsek
3. **Przeglądaj wyniki** w głównym panelu:
   - Metryki podsumowujące
   - Losowe próbki danych
   - Różnorodne wizualizacje
4. **Analizuj dane** używając interaktywnych wykresów

## 📈 Wizualizacje

Aplikacja oferuje następujące typy wizualizacji:

- **Wykresy słupkowe** - dla wieku, wykształcenia, hobby, motywacji
- **Wykresy kołowe** - dla płci i ulubionych miejsc
- **Wykresy porównawcze** - specjalizacja według płci
- **Metryki** - liczba respondentów według kategorii

## 🤝 Wkład w projekt

Chcesz przyczynić się do rozwoju projektu? Sprawdź [CONTRIBUTING.md](CONTRIBUTING.md) aby dowiedzieć się więcej.

## 📋 Changelog

Historia zmian dostępna w [CHANGELOG.md](CHANGELOG.md).

## 📄 Licencja

Ten projekt jest licencjonowany na podstawie licencji MIT - szczegóły w pliku [LICENSE](LICENSE).

## 👨‍💻 Autor

**Alan Steinbarth**
- Email: alan.steinbarth@gmail.com
- GitHub: [@AlanSteinbarth](https://github.com/AlanSteinbarth)

## 🐛 Zgłaszanie błędów

Jeśli znalazłeś błąd lub masz sugestię, proszę [utwórz issue](https://github.com/AlanSteinbarth/Filtrowanie-danych-z-ankiety/issues).

---

⭐ **Jeśli projekt Ci się podoba, zostaw gwiazdkę!**