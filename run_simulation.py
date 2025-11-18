from ai_agents.simulation.simulation_agent import ExampleAgent as SimulationAgent

simulation = SimulationAgent(name="SimulationAgent")

scenarios = ["Forecast Q4", "Stress Test Market", "Risk Scenario A"]
for scenario in scenarios:
    outcome = simulation.run_task(scenario)
    print(f"Simulation Outcome: {outcome}")
