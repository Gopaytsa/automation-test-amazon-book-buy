import argparse
import sys
import pytest


parser = argparse.ArgumentParser()

parser.add_argument('--browser',
                    help="Browser for tests run",
                    default='chrome',
                    choices=[
                      'chrome',
                      'firefox'
                    ])

parser.add_argument('--m',
                    help="Website for tests run",
                    action='store',
                    choices=[
                      'amazon',
                      'heroku',
                      'chrome',
                      'firefox'])

args = parser.parse_args()
BROWSER = args.browser
MARKER = args.m

print(MARKER)

print(f'Tests are running in {BROWSER} browser')

pytest_run = [f'--browser={BROWSER}']
print(f'{MARKER}')

if MARKER:
  print(f'{MARKER}')
  pytest_run += ['-m', f'{MARKER}']

if 'firefox' in BROWSER:
  pytest_run += ['-n4']
else:
  pytest_run += ['-n1']
  
print(pytest_run)
  
sys.exit(pytest.main(pytest_run))