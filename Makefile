# Makefile for Survey Data Filtering Dashboard
# Compatible with both Unix and Windows (using PowerShell)

.PHONY: help install install-dev test lint format security clean build docker run docs

# Default target
help: ## Show this help message
	@echo "Survey Data Filtering Dashboard - Makefile Commands"
	@echo "=================================================="
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# Installation targets
install: ## Install production dependencies
	pip install -r requirements.txt

install-dev: ## Install development dependencies
	pip install -r requirements.txt
	pip install -r requirements-dev.txt
	pre-commit install

# Development targets
run: ## Run the application locally
	streamlit run app.py

run-dev: ## Run the application in development mode
	streamlit run app.py --logger.level=debug

# Testing targets
test: ## Run all tests
	pytest

test-unit: ## Run unit tests only
	pytest tests/unit/

test-integration: ## Run integration tests only
	pytest tests/integration/

test-coverage: ## Run tests with coverage report
	pytest --cov=app --cov-report=html --cov-report=term

test-watch: ## Run tests in watch mode
	pytest-watch

# Code quality targets
lint: ## Run all linting tools
	flake8 .
	mypy app.py --ignore-missing-imports
	bandit -r . -x ./tests/

format: ## Format code with black and isort
	black .
	isort .

format-check: ## Check code formatting without making changes
	black --check .
	isort --check-only .

# Security targets
security: ## Run security checks
	bandit -r . -x ./tests/
	safety check
	semgrep --config=auto .

security-report: ## Generate detailed security report
	bandit -r . -x ./tests/ -f json -o security-report.json
	safety check --json --output safety-report.json
	semgrep --config=auto --json --output semgrep-report.json .

# Build targets
build: ## Build Python package
	python -m build

build-wheel: ## Build wheel only
	python -m build --wheel

build-sdist: ## Build source distribution only
	python -m build --sdist

# Docker targets
docker-build: ## Build Docker image
	docker build -t survey-data-filter:latest .

docker-build-dev: ## Build Docker image for development
	docker build -t survey-data-filter:dev --target builder .

docker-run: ## Run Docker container
	docker run -p 8501:8501 survey-data-filter:latest

docker-run-dev: ## Run Docker container in development mode
	docker run -p 8501:8501 -v $(PWD):/app survey-data-filter:dev

docker-compose-up: ## Start services with docker-compose
	docker-compose up -d

docker-compose-down: ## Stop services with docker-compose
	docker-compose down

docker-compose-logs: ## View docker-compose logs
	docker-compose logs -f

# Documentation targets
docs: ## Generate documentation
	sphinx-build -b html docs/ docs/_build/html

docs-serve: ## Serve documentation locally
	cd docs/_build/html && python -m http.server 8000

docs-clean: ## Clean documentation build
	rm -rf docs/_build/

# Database targets (for future use)
db-migrate: ## Run database migrations
	@echo "Database migrations not yet implemented"

db-seed: ## Seed database with sample data
	@echo "Database seeding not yet implemented"

db-reset: ## Reset database
	@echo "Database reset not yet implemented"

# Maintenance targets
clean: ## Clean up build artifacts and cache
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf htmlcov/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

clean-docker: ## Clean up Docker images and containers
	docker system prune -f
	docker image prune -f

# Release targets
tag: ## Create version tag (usage: make tag VERSION=v2.0.1)
	git tag -a $(VERSION) -m "Release $(VERSION)"
	git push origin $(VERSION)

release: ## Create release (run tests, build, tag)
	make test
	make lint
	make security
	make build
	@echo "Release ready! Run 'make tag VERSION=vX.Y.Z' to create tag"

# CI/CD targets
ci-install: ## Install dependencies for CI
	pip install -r requirements.txt -r requirements-dev.txt

ci-test: ## Run CI test suite
	pytest --cov=app --cov-report=xml --cov-fail-under=85

ci-quality: ## Run CI quality checks
	black --check .
	isort --check-only .
	flake8 .
	mypy app.py --ignore-missing-imports

ci-security: ## Run CI security checks
	bandit -r . -x ./tests/
	safety check

# Environment targets
env-create: ## Create Python virtual environment
	python -m venv venv

env-activate: ## Show activation command
	@echo "To activate virtual environment:"
	@echo "  On Unix/macOS: source venv/bin/activate"
	@echo "  On Windows:    venv\\Scripts\\activate"

# Data targets
data-validate: ## Validate data file
	python -c "import pandas as pd; df = pd.read_csv('35__welcome_survey_cleaned.csv', sep=';'); print(f'Data loaded: {len(df)} rows, {len(df.columns)} columns')"

data-info: ## Show data information
	python -c "import pandas as pd; df = pd.read_csv('35__welcome_survey_cleaned.csv', sep=';'); print(df.info()); print(df.describe())"

# Performance targets
profile: ## Profile application performance
	python -m cProfile -o profile.stats -m streamlit run app.py &
	@echo "Profiling started. Stop with Ctrl+C and analyze profile.stats"

benchmark: ## Run performance benchmarks
	python -c "import time; import pandas as pd; start=time.time(); df=pd.read_csv('35__welcome_survey_cleaned.csv', sep=';'); print(f'Data loading time: {time.time()-start:.2f}s')"

# Deployment targets
deploy-streamlit: ## Deploy to Streamlit Cloud (manual step)
	@echo "To deploy to Streamlit Cloud:"
	@echo "1. Push to GitHub"
	@echo "2. Go to share.streamlit.io"
	@echo "3. Connect your repository"

deploy-heroku: ## Deploy to Heroku
	@echo "To deploy to Heroku:"
	@echo "1. Create Procfile: echo 'web: streamlit run app.py --server.port=\$$PORT --server.address=0.0.0.0' > Procfile"
	@echo "2. heroku create your-app-name"
	@echo "3. git push heroku main"

# Development workflow
dev-setup: install-dev ## Complete development setup
	@echo "Development environment ready!"
	@echo "Run 'make run' to start the application"

dev-check: format lint test ## Run all development checks
	@echo "All development checks passed!"

# Production workflow
prod-check: ci-test ci-quality ci-security ## Run all production checks
	@echo "Production checks passed!"

# Version information
version: ## Show version information
	@echo "Survey Data Filtering Dashboard v2.0.0"
	@echo "Python: $(shell python --version)"
	@echo "Streamlit: $(shell streamlit version)"
	@echo "Git commit: $(shell git rev-parse --short HEAD)"

# System information
info: ## Show system information
	@echo "System Information:"
	@echo "=================="
	@echo "OS: $(shell python -c 'import platform; print(platform.system() + \" \" + platform.release())')"
	@echo "Python: $(shell python --version)"
	@echo "Pip: $(shell pip --version)"
	@echo "Git: $(shell git --version)"
	@echo "Docker: $(shell docker --version 2>/dev/null || echo 'Not installed')"
