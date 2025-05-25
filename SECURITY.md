# Security Policy

## 🔒 Supported Versions

Aktualnie wspierane wersje projektu z aktualizacjami bezpieczeństwa:

| Version | Supported          |
| ------- | ------------------ |
| 2.1.x   | :white_check_mark: |
| 2.0.x   | :white_check_mark: |
| 1.x.x   | :x:                |

## 🚨 Reporting a Vulnerability

### Jak zgłosić vulnerability?

**NIE** używaj publicznych issues do zgłaszania problemów bezpieczeństwa!

#### Preferowane metody zgłaszania:

1. **GitHub Security Advisories** (zalecane)
   - Idź do zakładki "Security" w repozytorium
   - Kliknij "Report a vulnerability"
   - Wypełnij formularz z szczegółami

2. **Email bezpośredni**
   - Email: alan.steinbarth@gmail.com
   - Temat: `[SECURITY] Vulnerability in Filtrowanie-danych-z-ankiety`

### Informacje do dołączenia:

- **Opis vulnerability** - szczegółowy opis problemu
- **Kroki reprodukcji** - jak odtworzyć problem
- **Impact assessment** - potencjalny wpływ na bezpieczeństwo
- **Proposed solution** - sugerowane rozwiązanie (opcjonalne)
- **Environment details** - wersja Python, OS, wersja aplikacji

### Co się dzieje po zgłoszeniu?

1. **Potwierdzenie odbioru** - w ciągu 48 godzin
2. **Wstępna ocena** - w ciągu 7 dni
3. **Szczegółowa analiza** - w ciągu 14 dni
4. **Rozwiązanie/patch** - w zależności od krytyczności
5. **Public disclosure** - po wydaniu patcha

### Timeline dla różnych poziomów krytyczności:

- **Critical** - 7 dni
- **High** - 14 dni  
- **Medium** - 30 dni
- **Low** - 90 dni

## 🛡️ Security Best Practices

### Dla użytkowników:

1. **Zawsze używaj najnowszej wersji**
   ```bash
   pip install --upgrade streamlit pandas plotly
   ```

2. **Sprawdzaj integrity plików danych**
   - Nie ładuj danych z niezaufanych źródeł
   - Waliduj format i zawartość CSV

3. **Używaj środowisk wirtualnych**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

4. **Regularnie aktualizuj zależności**
   ```bash
   pip list --outdated
   pip install --upgrade -r requirements.txt
   ```

### Dla deweloperów:

1. **Uruchamiaj security checks lokalnie**
   ```bash
   bandit -r . -f json
   safety check
   pip-audit
   ```

2. **Używaj pre-commit hooks**
   ```bash
   pre-commit install
   pre-commit run --all-files
   ```

3. **Nigdy nie commituj secrets**
   - Używaj `.env` files (dodane do `.gitignore`)
   - Używaj GitHub Secrets dla CI/CD

4. **Code review dla security**
   - Wszystkie PR muszą przejść review
   - Specjalna uwaga na input validation
   - Sprawdzanie dependency updates

## 🔍 Automated Security Scanning

Projekt używa automatycznych narzędzi do skanowania bezpieczeństwa:

### GitHub Actions Security Pipeline:

- **Bandit** - skanowanie kodu Python pod kątem security issues
- **Safety** - sprawdzanie known vulnerabilities w dependencies
- **pip-audit** - audyt pakietów Python
- **CodeQL** - advanced security analysis
- **Dependabot** - automatyczne updates dependencies

### Lokalne security tools:

```bash
# Instalacja narzędzi security
pip install bandit safety pip-audit

# Uruchomienie skanowania
bandit -r . -f json -o security-report.json
safety check --json
pip-audit --format=json
```

## 📊 Security Metrics

Monitorujemy następujące metryki bezpieczeństwa:

- Zero known high/critical vulnerabilities
- 100% dependency scanning coverage  
- Regular security updates (miesięcznie)
- Security review dla wszystkich PR
- Automated security testing w CI/CD

## 🚀 Incident Response

W przypadku security incident:

1. **Immediate containment** - izolacja problemu
2. **Assessment** - ocena skali i wpływu
3. **Communication** - informowanie stakeholders
4. **Remediation** - implementacja rozwiązania
5. **Post-mortem** - analiza i lessons learned

## 📞 Contact Information

- **Security Team**: alan.steinbarth@gmail.com
- **Project Maintainer**: [@AlanSteinbarth](https://github.com/AlanSteinbarth)
- **Response Time**: 48 hours dla critical issues

## 🙏 Hall of Fame

Dziękujemy osobom, które odpowiedzialnie zgłosiły problemy bezpieczeństwa:

_Lista zostanie zaktualizowana gdy otrzymamy pierwsze zgłoszenia._

---

**Pamiętaj**: Bezpieczeństwo to odpowiedzialność całej społeczności! 🛡️
