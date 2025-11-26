from crewai import Crew, Task
from agents.architect import architect
from agents.engineer import engineer
from agents.tester import tester

# Задачи
tasks = [
    Task(description="Создай архитектурный план Jarvis", agent=architect),
    Task(description="Напиши код по плану", agent=engineer),
    Task(description="Проверь код и исправь ошибки", agent=tester)
]

# Команда
crew = Crew(agents=[architect, engineer, tester], tasks=tasks)
result = crew.run()

print("=== РЕЗУЛЬТАТ ===")
print(result)
