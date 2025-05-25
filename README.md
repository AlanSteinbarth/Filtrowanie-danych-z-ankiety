# 📋 Filtrowanie Danych z Ankiety

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI/CD](https://github.com/AlanSteinbarth/Filtrowanie-danych-z-ankiety/actions/workflows/ci.yml/badge.svg)](https://github.com/AlanSteinbarth/Filtrowanie-danych-z-ankiety/actions)
[![Code Quality](https://github.com/AlanSteinbarth/Filtrowanie-danych-z-ankiety/actions/workflows/quality.yml/badge.svg)](https://github.com/AlanSteinbarth/Filtrowanie-danych-z-ankiety/actions)
[![Security](https://github.com/AlanSteinbarth/Filtrowanie-danych-z-ankiety/actions/workflows/security.yml/badge.svg)](https://github.com/AlanSteinbarth/Filtrowanie-danych-z-ankiety/actions)
[![Version](https://img.shields.io/github/v/release/AlanSteinbarth/Filtrowanie-danych-z-ankiety)](https://github.com/AlanSteinbarth/Filtrowanie-danych-z-ankiety/releases)

> **Wersja 2.0** - Ulepszona, enterprise-level aplikacja do analizy danych ankiety

## 📋 Spis Treści

- [🚀 Funkcjonalności](#-funkcjonalności)
- [🛠️ Technologie](#️-technologie)
- [📦 Instalacja](#-instalacja)
- [🎯 Użytkowanie](#-użytkowanie)
- [📊 Dane](#-dane)
- [📈 Wizualizacje](#-wizualizacje)
- [🧪 Testowanie](#-testowanie)
- [🔧 Rozwój](#-rozwój)
- [📚 Dokumentacja](#-dokumentacja)
- [🤝 Wkład w projekt](#-wkład-w-projekt)
- [🔒 Bezpieczeństwo](#-bezpieczeństwo)
- [📋 Changelog](#-changelog)
- [📄 Licencja](#-licencja)
- [👨‍💻 Autor](#-autor)
- [❓ FAQ](#-faq)

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

## 🧪 Testowanie

### Uruchamianie testów lokalnie

```bash
# Instalacja zależności deweloperskich
pip install -r requirements-dev.txt

# Uruchomienie wszystkich testów
pytest

# Testy z pokryciem kodu
pytest --cov=app --cov-report=html

# Sprawdzenie jakości kodu
flake8 app.py
bandit -r . -f json
safety check
```

### CI/CD Pipeline

Projekt używa GitHub Actions do automatycznego:
- ✅ Testowania na Python 3.8, 3.9, 3.10, 3.11
- ✅ Sprawdzania jakości kodu (flake8, bandit)
- ✅ Skanowania bezpieczeństwa (safety, bandit)
- ✅ Automatycznego tworzenia releases

## 🔧 Rozwój

### Środowisko deweloperskie

```bash
# Klonowanie repozytorium
git clone https://github.com/AlanSteinbarth/Filtrowanie-danych-z-ankiety.git
cd Filtrowanie-danych-z-ankiety

# Tworzenie środowiska wirtualnego
python -m venv venv
source venv/bin/activate  # Linux/Mac
# lub
venv\Scripts\activate     # Windows

# Instalacja zależności deweloperskich
pip install -r requirements-dev.txt

# Uruchomienie w trybie development
streamlit run app.py --server.runOnSave true
```

### Struktura projektu

```
Filtrowanie-danych-z-ankiety/
├── .github/
│   ├── workflows/           # GitHub Actions CI/CD
│   ├── ISSUE_TEMPLATE/      # Szablony issues
│   └── PULL_REQUEST_TEMPLATE.md
├── db/                      # Struktura bazy danych
├── tests/                   # Testy jednostkowe
├── app.py                   # Główna aplikacja
├── requirements.txt         # Zależności produkcyjne
├── requirements-dev.txt     # Zależności deweloperskie
├── .env.example            # Przykład konfiguracji
├── .gitignore              # Ignorowane pliki
└── docs/                   # Dokumentacja
```

## 📚 Dokumentacja

- [CONTRIBUTING.md](CONTRIBUTING.md) - Przewodnik dla deweloperów
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) - Kodeks postępowania
- [SECURITY.md](SECURITY.md) - Polityka bezpieczeństwa
- [CHANGELOG.md](CHANGELOG.md) - Historia zmian

## 📋 Changelog

Historia zmian dostępna w [CHANGELOG.md](CHANGELOG.md).

## 📄 Licencja

Ten projekt jest licencjonowany na podstawie licencji MIT - szczegóły w pliku [LICENSE](LICENSE).

## 👨‍💻 Autor

**Alan Steinbarth**
- Email: alan.steinbarth@gmail.com
- GitHub: [@AlanSteinbarth](https://github.com/AlanSteinbarth)

## 🤝 Wkład w projekt

Zachęcamy do współpracy! Sprawdź [CONTRIBUTING.md](CONTRIBUTING.md) aby dowiedzieć się więcej.

### Szybki start dla deweloperów

1. **Fork** repozytorium
2. **Utwórz** branch dla nowej funkcji (`git checkout -b feature/AmazingFeature`)
3. **Commit** swoje zmiany (`git commit -m 'feat: Add some AmazingFeature'`)
4. **Push** do brancha (`git push origin feature/AmazingFeature`)
5. **Otwórz** Pull Request

## 🔒 Bezpieczeństwo

Bezpieczeństwo jest naszym priorytetem. Sprawdź [SECURITY.md](SECURITY.md) dla:
- Zgłaszania vulnerabilities
- Supported versions
- Security best practices

## ❓ FAQ

### Jak uruchomić aplikację lokalnie?
```bash
pip install -r requirements.txt
streamlit run app.py
```

### Czy mogę używać własnych danych?
Tak! Zastąp plik `35__welcome_survey_cleaned.csv` swoimi danymi w tym samym formacie.

### Jak zgłosić błąd?
Użyj [GitHub Issues](https://github.com/AlanSteinbarth/Filtrowanie-danych-z-ankiety/issues) z odpowiednim szablonem.

### Czy aplikacja jest gotowa do produkcji?
Tak! Aplikacja przeszła przez pełny pipeline CI/CD i testy bezpieczeństwa.

### Jak dodać nowe filtry?
Sprawdź [CONTRIBUTING.md](CONTRIBUTING.md) sekcję "Dodawanie nowych funkcji".

---

## 🏆 Wyróżnienia

- ✅ **Enterprise Level** - Pełny pipeline CI/CD
- ✅ **Security First** - Automatyczne skanowanie bezpieczeństwa
- ✅ **Code Quality** - Automatyczne sprawdzanie jakości kodu
- ✅ **Multi-Platform** - Testowane na Python 3.8-3.11
- ✅ **Community Ready** - Pełna dokumentacja i szablony

---

⭐ **Jeśli projekt Ci się podoba, zostaw gwiazdkę!**