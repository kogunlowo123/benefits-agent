# Benefits Agent

[![CI](https://github.com/kogunlowo123/benefits-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/benefits-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Human Resources | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Employee benefits administration agent that answers benefits questions, guides enrollment decisions, compares plan options, processes life event changes, and manages open enrollment communications.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `answer_benefits_question` | Answer an employee question about benefits using policy knowledge base |
| `compare_plans` | Compare health/dental/vision plan options for an employee |
| `process_life_event` | Process a qualifying life event benefits change |
| `estimate_costs` | Estimate benefits costs for different plan and coverage options |
| `send_enrollment_reminder` | Send enrollment reminder to employees with pending actions |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/benefits/ask` | Answer benefits question |
| `POST` | `/api/v1/benefits/compare` | Compare plans |
| `POST` | `/api/v1/benefits/life-event` | Process life event |
| `POST` | `/api/v1/benefits/estimate` | Estimate costs |
| `POST` | `/api/v1/benefits/remind` | Send enrollment reminder |

## Features

- Benefits Guidance
- Enrollment Support
- Plan Comparison
- Life Event Processing
- Open Enrollment

## Integrations

- Workday
- Adp
- Gusto
- Benefitfocus
- Ease

## Architecture

```
benefits-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── benefits_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Benefits Platform + HRIS + Knowledge Base**

---

Built as part of the Enterprise AI Agent Platform.
