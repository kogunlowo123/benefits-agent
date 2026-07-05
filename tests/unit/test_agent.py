"""Benefits Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_answer_benefits_question():
    """Test Answer an employee question about benefits using policy knowledge base."""
    tools = AgentTools()
    result = await tools.answer_benefits_question(question="test", employee_id="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_compare_plans():
    """Test Compare health/dental/vision plan options for an employee."""
    tools = AgentTools()
    result = await tools.compare_plans(employee_id="test", plan_type="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_process_life_event():
    """Test Process a qualifying life event benefits change."""
    tools = AgentTools()
    result = await tools.process_life_event(employee_id="test", event_type="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_estimate_costs():
    """Test Estimate benefits costs for different plan and coverage options."""
    tools = AgentTools()
    result = await tools.estimate_costs(plan_options="test", employee_tier="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.benefits_agent_agent import BenefitsAgentAgent
    agent = BenefitsAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
