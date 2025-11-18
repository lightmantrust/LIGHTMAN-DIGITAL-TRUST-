import pytest

@pytest.fixture(scope="session")
def sample_task():
    return "Run predictive model"

@pytest.fixture(scope="session")
def sample_scenario():
    return "Forecast Q4"
