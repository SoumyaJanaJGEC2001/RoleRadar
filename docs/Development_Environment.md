# RoleRadar AI — Development Environment

## Environment Manager

Conda

## Environment Name

roleradar_env

## Python Version

Python 3.11

## Initial Purpose

The initial environment supports development of the Greenhouse public job-board collector, raw-response storage, data validation, and automated testing.

## Initial Libraries

- requests
- python-dotenv
- pydantic
- pytest
- ruff

## Future Library Groups

Future libraries will be added only when their project phase begins.

### Data processing

- pandas
- numpy

### Database

- sqlalchemy
- psycopg

### Statistics and machine learning

- scipy
- statsmodels
- scikit-learn
- mlflow

### API and dashboard

- fastapi
- uvicorn
- streamlit

### Workflow automation

- prefect

### Agentic AI

- langgraph
- selected LLM client library

### Cloud

GCP libraries will be added only during the deployment phase.

## Environment Rules

- Do not use the base Conda environment for project development.
- Do not reuse environments from unrelated projects.
- Add libraries only when required by the current phase.
- Record dependency changes in version control.
- Never place API keys or passwords directly inside source code.