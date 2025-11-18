import pytest
from ai_agents.simulation.simulation_agent import ExampleAgent as SimulationAgent

@pytest.fixture
def simulation():
    return SimulationAgent(name="SimulationAgent")

def test_simulation_scenario(simulation):
    scenario = "Stress Test Market"
    outcome = simulation.run_task(scenario)
    assert "Processed" in outcome
    assert simulation.status == "idle"
