import pytest
from ai_agents.connector.connector_agent import ExampleAgent as ConnectorAgent

@pytest.fixture
def connector():
    return ConnectorAgent(name="ConnectorAgent")

def test_api_call(connector):
    api_task = {"endpoint": "/api/data", "method": "GET", "payload": {}}
    response = connector.run_task(api_task)
    assert isinstance(response, str)
    assert "Processed" in response
