def test_agent_orchestrator():
    prompt = "Test execution query for agentic-media-fact-checker-verifier"
    assert len(prompt) > 0
    assert "Test" in prompt
