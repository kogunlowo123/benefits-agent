"""Test configuration for Benefits Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "benefits-agent", "category": "Human Resources"}
