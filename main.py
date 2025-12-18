#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from crew import ConsultingAgentCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'client_company': 'TechCorp Global',
        'strategic_objective': 'enter the Southeast Asian market and establish a strong presence in the enterprise software segment',
        'target_market': 'Southeast Asia enterprise software market',
        'current_year': str(datetime.now().year)
    }

    try:
        ConsultingAgentCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "client_company": "TechCorp Global",
        "strategic_objective": "enter the Southeast Asian market and establish a strong presence in the enterprise software segment",
        "target_market": "Southeast Asia enterprise software market",
        'current_year': str(datetime.now().year)
    }
    try:
        LatestAiDevelopment().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        LatestAiDevelopment().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "client_company": "TechCorp Global",
        "strategic_objective": "enter the Southeast Asian market and establish a strong presence in the enterprise software segment",
        "target_market": "Southeast Asia enterprise software market",
        "current_year": str(datetime.now().year)
    }

    try:
        LatestAiDevelopment().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

def run_with_trigger():
    """
    Run the crew with trigger payload.
    """
    import json

    if len(sys.argv) < 2:
        raise Exception("No trigger payload provided. Please provide JSON payload as argument.")

    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        raise Exception("Invalid JSON payload provided as argument")

    inputs = {
        "crewai_trigger_payload": trigger_payload,
        "client_company": "",
        "strategic_objective": "",
        "target_market": "",
        "current_year": ""
    }

    try:
        result = LatestAiDevelopment().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew with trigger: {e}")
