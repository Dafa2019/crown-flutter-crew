#!/usr/bin/env python3
"""Crown Flutter Crew - Entry Point"""
import sys
from crown_flutter_crew.crew import CrownFlutterCrew


def run():
    inputs = {
        'project_description': (
            sys.argv[1] if len(sys.argv) > 1
            else 'Build a production-ready Flutter e-commerce app with Clean Architecture, '
                 'Riverpod 3.0, Stripe payments, push notifications, and full CI/CD pipeline.'
        )
    }
    CrownFlutterCrew().crew().kickoff(inputs=inputs)


if __name__ == '__main__':
    run()
