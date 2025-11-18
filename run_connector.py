from ai_agents.connector.connector_agent import ExampleAgent as ConnectorAgent

# Sample API interaction
connector = ConnectorAgent(name="ConnectorAgent")

api_task = {"endpoint": "/api/data", "method": "GET", "payload": {}}
response = connector.run_task(api_task)
print(f"API Response: {response}")
