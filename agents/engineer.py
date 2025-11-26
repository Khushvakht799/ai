from crewai import Agent
from local_llm import llm_pipeline

engineer = Agent(
    name="engineer",
    role="пишет код по плану архитектора проекта Jarvis",
    goal="написать код системы по плану архитектора",
    llm=llm_pipeline,
    backstory="Опытный код-райтер AI систем"
)
