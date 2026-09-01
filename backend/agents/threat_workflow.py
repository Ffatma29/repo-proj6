from crewai import Crew, Task

from agents.threat_agent import (
    create_analyzer_agent,
    create_reporter_agent,
    create_risk_assessor_agent,
)


def analyze_threat(threat_data: dict) -> str:
    analyzer = create_analyzer_agent()
    assessor = create_risk_assessor_agent()
    reporter = create_reporter_agent()

    analyzer_task = Task(
        description=(
            "Analyze this suspicious network event:\n"
            f"{threat_data}\n\n"
            "Identify the suspicious behavior and explain the evidence."
        ),
        expected_output=(
            "A concise analysis identifying the suspicious behavior "
            "and supporting evidence."
        ),
        agent=analyzer,
    )

    risk_task = Task(
        description=(
            "Assess the risk of the network event using the event data "
            "and the threat analysis from the previous agent.\n"
            f"Original event: {threat_data}"
        ),
        expected_output=(
            "A risk assessment containing the severity, reasoning, "
            "and strongest evidence."
        ),
        agent=assessor,
        context=[analyzer_task],
    )

    report_task = Task(
        description=(
            "Create a concise security alert based on the original event "
            "and the previous analysis. Include threat, evidence, risk "
            "level, and recommended follow-up action."
        ),
        expected_output=(
            "A readable security alert with threat, evidence, risk level, "
            "and recommended action."
        ),
        agent=reporter,
        context=[analyzer_task, risk_task],
    )

    crew = Crew(
        agents=[analyzer, assessor, reporter],
        tasks=[analyzer_task, risk_task, report_task],
        verbose=True,
    )

    result = crew.kickoff()

    return str(result)

