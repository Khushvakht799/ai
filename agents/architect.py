from crewai import Agent
from local_llm import llm_pipeline

architect = Agent(
    name="Architect",
    role="Планирует структуру проекта Jarvis",
    goal="Создать архитектурный план системы",
    llm=llm_pipeline,
    backstory="Опытный архитектор AI систем"
)
