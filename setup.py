"""
Setup configuration for Survey Data Filtering Dashboard.
"""

from setuptools import setup, find_packages
import os

# Read README for long description
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="survey-data-filter",
    version="2.0.0",
    author="Alan Steinbarth",
    author_email="alan.steinbarth@gmail.com",
    description="Advanced data filtering and visualization tool for survey analysis",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/AlanSteinbarth/Filtrowanie-danych-z-ankiety",
    project_urls={
        "Bug Reports": "https://github.com/AlanSteinbarth/Filtrowanie-danych-z-ankiety/issues",
        "Source": "https://github.com/AlanSteinbarth/Filtrowanie-danych-z-ankiety",
        "Documentation": "https://github.com/AlanSteinbarth/Filtrowanie-danych-z-ankiety#readme",
    },
    packages=find_packages(exclude=["tests*"]),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Office/Business :: Financial :: Spreadsheet",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Framework :: Streamlit",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "black>=23.12.1",
            "flake8>=7.0.0",
            "isort>=5.13.2",
            "mypy>=1.8.0",
            "pytest>=7.4.3",
            "pytest-cov>=4.1.0",
            "bandit>=1.7.5",
            "safety>=2.3.4",
            "pre-commit>=3.6.0",
        ],
        "docs": [
            "sphinx>=7.2.6",
            "sphinx-rtd-theme>=2.0.0",
            "myst-parser>=2.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "survey-filter=app:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.csv", "*.md", "*.txt", "*.yml", "*.yaml"],
    },
    keywords=[
        "streamlit",
        "data-analysis",
        "survey",
        "filtering",
        "visualization",
        "dashboard",
        "pandas",
        "plotly",
        "data-science",
    ],
    zip_safe=False,
)
