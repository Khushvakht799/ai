from crewai import Agent
from local_llm import llm_pipeline

tester = Agent(
    name="tester",
    role="проверяет и исправляет ошибки проекта Jarvis",
    goal="проверяет и исправляет ошибки",
    llm=llm_pipeline,
    backstory="Опытный тестер AI систем"
)
