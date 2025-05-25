# Changelog

Wszystkie znaczące zmiany w tym projekcie będą dokumentowane w tym pliku.

Format oparty na [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
a projekt stosuje [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-05-25

### Dodane
- Interaktywna aplikacja Streamlit do analizy danych z ankiety
- Panel boczny z filtrami dla:
  - Płci (wszyscy/kobiety/mężczyźni)
  - Przedziałów wiekowych
  - Lat doświadczenia zawodowego
  - Specjalizacji zawodowej
  - Hobby i zainteresowań
  - Preferencji przekąsek (słodkie/słone)
- Metryki podsumowujące liczbę respondentów
- Wyświetlanie losowych próbek danych
- Wizualizacje danych:
  - Wykres słupkowy dla wieku
  - Wykres kołowy dla płci
  - Wykres słupkowy dla poziomu wykształcenia
  - Wykres słupkowy dla ulubionych zwierząt
  - Wykres kołowy dla ulubionych miejsc
  - Wykres słupkowy dla specjalizacji
  - Interaktywne wykresy dla hobby, preferencji nauki i motywacji
  - Wykres porównawczy specjalizacji według płci
- Kompletna dokumentacja projektu
- Licencja MIT
- Requirements.txt z wszystkimi zależnościami

### Struktura projektu
- `app.py` - główna aplikacja Streamlit
- `35__welcome_survey_cleaned.csv` - dane ankiety
- `README.md` - dokumentacja projektu
- `requirements.txt` - zależności Python
- `LICENSE` - licencja MIT
- `CHANGELOG.md` - historia zmian
- `CONTRIBUTING.md` - przewodnik dla współtwórców

## [Unreleased]

### Planowane
- Dodanie testów jednostkowych
- Optymalizacja wydajności dla większych zbiorów danych
- Dodanie możliwości eksportu wyników
- Rozszerzenie opcji wizualizacji
- Dodanie walidacji danych wejściowych