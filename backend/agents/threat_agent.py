from crewai import Agent


def create_analyzer_agent():
    return Agent(
        role="Threat Analyzer",
        goal=(
            "Analyze suspicious network activity and identify the "
            "most likely threat behavior using the provided evidence."
        ),
        backstory=(
            "You are a cybersecurity threat analyst who specializes in "
            "network intrusion detection and behavioral analysis."
        ),
        verbose=True,
        allow_delegation=False,
    )


def create_risk_assessor_agent():
    return Agent(
        role="Risk Assessment Specialist",
        goal=(
            "Assess the severity of a detected threat and explain the "
            "strongest evidence behind the risk level."
        ),
        backstory=(
            "You are a security risk specialist experienced in evaluating "
            "network anomalies, authentication attacks, and suspicious behavior."
        ),
        verbose=True,
        allow_delegation=False,
    )


def create_reporter_agent():
    return Agent(
        role="Security Reporter",
        goal=(
            "Create a concise security alert containing the threat, evidence, "
            "risk level, and recommended follow-up action."
        ),
        backstory=(
            "You are a security operations reporter who converts technical "
            "threat analysis into clear and actionable incident summaries."
        ),
        verbose=True,
        allow_delegation=False,
    )
