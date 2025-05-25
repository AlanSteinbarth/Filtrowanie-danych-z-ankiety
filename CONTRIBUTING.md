# Przewodnik dla Współtwórców

Dziękujemy za zainteresowanie wkładem w projekt **Filtrowanie Danych z Ankiety**! 🎉

## 🤝 Sposoby Współpracy

### Zgłaszanie Błędów
1. Sprawdź czy błąd nie został już zgłoszony w [Issues](https://github.com/AlanSteinbarth/Filtrowanie-danych-z-ankiety/issues)
2. Utwórz nowy issue z szablonem:
   - **Tytuł**: Krótki opis problemu
   - **Opis**: Szczegółowy opis błędu
   - **Kroki reprodukcji**: Jak odtworzyć błąd
   - **Oczekiwane zachowanie**: Co powinno się stać
   - **Rzeczywiste zachowanie**: Co się dzieje
   - **Środowisko**: System operacyjny, wersja Python, wersja przeglądarki

### Sugerowanie Ulepszeń
1. Sprawdź czy sugestia nie została już zgłoszona
2. Utwórz issue z etykietą "enhancement"
3. Opisz szczegółowo proponowaną funkcjonalność
4. Wyjaśnij dlaczego byłaby przydatna

### Zgłaszanie Pull Requestów

#### Przygotowanie środowiska
```bash
# 1. Forkuj repozytorium na GitHub
# 2. Sklonuj swój fork
git clone https://github.com/TWOJA-NAZWA/Filtrowanie-danych-z-ankiety.git
cd Filtrowanie-danych-z-ankiety

# 3. Utwórz środowisko wirtualne
python -m venv venv
venv\Scripts\activate  # Windows
# lub
source venv/bin/activate  # Linux/Mac

# 4. Zainstaluj zależności
pip install -r requirements.txt

# 5. Utwórz branch dla swojej zmiany
git checkout -b nazwa-twojej-funkcji
```

#### Standardy Kodowania
- **Format kodu**: Używaj PEP 8 dla Python
- **Komentarze**: Pisz komentarze w języku polskim dla lepszej czytelności
- **Nazwy zmiennych**: Używaj polskich nazw tam gdzie to możliwe
- **Dokumentacja**: Dodawaj docstring do funkcji

#### Przykład dobrego kodu:
```python
def filtruj_dane_podle_wieku(df: pd.DataFrame, przedzialy_wiekowe: list) -> pd.DataFrame:
    """
    Filtruje DataFrame według wybranych przedziałów wiekowych.
    
    Args:
        df (pd.DataFrame): Dane ankiety do filtrowania
        przedzialy_wiekowe (list): Lista wybranych przedziałów wiekowych
        
    Returns:
        pd.DataFrame: Przefiltrowane dane
    """
    if przedzialy_wiekowe:
        return df[df["age"].isin(przedzialy_wiekowe)]
    return df
```

#### Proces PR
1. **Testuj lokalnie**: Upewnij się że aplikacja działa poprawnie
```bash
streamlit run app.py
```

2. **Commituj zmiany**:
```bash
git add .
git commit -m "feat: dodaj funkcję filtrowania według nowego kryterium"
```

3. **Wypchnij zmiany**:
```bash
git push origin nazwa-twojej-funkcji
```

4. **Utwórz Pull Request** na GitHub z opisem:
   - Co zmienia PR
   - Dlaczego ta zmiana jest potrzebna
   - Jak testować zmiany
   - Screenshoty (jeśli dotyczy UI)

#### Konwencje Commitów
Używamy [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` - nowa funkcjonalność
- `fix:` - naprawa błędu
- `docs:` - zmiany w dokumentacji
- `style:` - formatowanie, brak zmian w logice
- `refactor:` - refaktoring kodu
- `test:` - dodanie/modyfikacja testów
- `chore:` - zmiany w buildzie, zależnościach

Przykłady:
```
feat: dodaj filtr według wykształcenia
fix: napraw błąd w wykresie kołowym dla płci
docs: aktualizuj README z instrukcjami instalacji
```

## 🎯 Obszary do Rozwoju

### Priorytetowe
- [ ] Dodanie testów jednostkowych
- [ ] Optymalizacja wydajności
- [ ] Walidacja danych wejściowych
- [ ] Obsługa błędów

### Średni priorytet
- [ ] Dodanie nowych typów wizualizacji
- [ ] Eksport danych do CSV/Excel
- [ ] Responsywność na urządzeniach mobilnych
- [ ] Internationalizacja (i18n)

### Niski priorytet
- [ ] Ciemny tryb
- [ ] Animacje w wykresach
- [ ] Zaawansowane filtry
- [ ] API dla zewnętrznych aplikacji

## 📋 Lista Kontrolna PR

Przed wysłaniem PR sprawdź:

- [ ] Kod jest zgodny z PEP 8
- [ ] Aplikacja uruchamia się bez błędów
- [ ] Wszystkie filtry działają poprawnie
- [ ] Wykresy renderują się prawidłowo
- [ ] Brak błędów w konsoli przeglądarki
- [ ] Dodałeś/zaktualizowałeś komentarze
- [ ] Zaktualizowałeś dokumentację (jeśli potrzeba)
- [ ] Commit ma opisową wiadomość

## 🆘 Potrzebujesz Pomocy?

- **Dyskusje**: Użyj [GitHub Discussions](https://github.com/AlanSteinbarth/Filtrowanie-danych-z-ankiety/discussions)
- **Email**: alan.steinbarth@gmail.com
- **Issues**: Dla konkretnych problemów technicznych

## 🙏 Podziękowania

Dziękujemy wszystkim współtwórcom, którzy pomagają w rozwoju tego projektu!

---

**Pamiętaj**: Każdy wkład, niezależnie od wielkości, jest cenny! 🌟