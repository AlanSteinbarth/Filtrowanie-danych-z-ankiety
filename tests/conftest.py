"""
Pytest configuration and shared fixtures for the test suite.
"""

import pytest
import pandas as pd
import streamlit as st
from unittest.mock import Mock, patch
import tempfile
import os


@pytest.fixture
def sample_dataframe():
    """Create a sample DataFrame for testing."""
    return pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'London', 'Paris', 'Tokyo'],
        'Salary': [50000, 60000, 70000, 55000],
        'Department': ['IT', 'HR', 'Finance', 'IT']
    })


@pytest.fixture
def sample_csv_file(sample_dataframe):
    """Create a temporary CSV file for testing."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        sample_dataframe.to_csv(f.name, index=False)
        yield f.name
    os.unlink(f.name)


@pytest.fixture
def mock_streamlit():
    """Mock Streamlit functions for testing."""
    with patch.multiple(
        'streamlit',
        set_page_config=Mock(),
        title=Mock(),
        sidebar=Mock(),
        selectbox=Mock(),
        multiselect=Mock(),
        slider=Mock(),
        dataframe=Mock(),
        plotly_chart=Mock(),
        metric=Mock(),
        success=Mock(),
        error=Mock(),
        warning=Mock(),
        info=Mock()
    ):
        yield st


@pytest.fixture
def mock_file_upload():
    """Mock file upload for testing."""
    mock_file = Mock()
    mock_file.name = "test_data.csv"
    mock_file.type = "text/csv"
    mock_file.size = 1024
    return mock_file


@pytest.fixture(autouse=True)
def reset_streamlit_state():
    """Reset Streamlit session state before each test."""
    if hasattr(st, 'session_state'):
        st.session_state.clear()


def pytest_configure(config):
    """Pytest configuration."""
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )
    config.addinivalue_line(
        "markers", "integration: marks tests as integration tests"
    )
    config.addinivalue_line(
        "markers", "unit: marks tests as unit tests"
    )
