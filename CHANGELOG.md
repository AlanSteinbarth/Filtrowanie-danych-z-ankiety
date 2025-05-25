# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned for v2.1.0
- Database integration for data persistence
- User authentication system
- Advanced export formats
- API endpoints for data access
- Mobile-responsive design improvements

## [2.0.0] - 2025-05-26 - Enterprise Release 🚀

### Added - Infrastructure
- Complete CI/CD pipeline with GitHub Actions
- Code quality workflows (linting, formatting, type checking)
- Security scanning (Bandit, Safety, Semgrep)
- Automated testing framework with pytest
- Pre-commit hooks for code quality
- Enterprise-level project structure

### Added - Documentation
- Comprehensive user guide and documentation
- Issue templates (bug reports, feature requests, questions)
- Pull request templates with quality checklist
- Security policy (SECURITY.md)
- Code of conduct (CODE_OF_CONDUCT.md)
- Contributing guidelines (CONTRIBUTING.md)

### Added - Development Tools
- Development dependencies (requirements-dev.txt)
- Environment configuration (.env.example)
- Build configuration (setup.py, pyproject.toml)
- Package management (MANIFEST.in)
- Testing structure with fixtures and mocks

### Added - Quality Assurance
- Code coverage reporting
- Static analysis tools
- Performance monitoring
- Security vulnerability scanning
- Automated releases with changelog generation

### Changed - Application Structure
- Modular code organization with proper separation
- Enhanced error handling and logging
- Improved performance optimizations
- Better user interface and experience

### Infrastructure
- GitHub repository integration
- Automated workflows for CI/CD
- Release management
- Version tagging and semantic versioning

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