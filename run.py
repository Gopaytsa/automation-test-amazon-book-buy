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
                      'parallel'])

args = parser.parse_args()
BROWSER = args.browser
MARKER = args.m

print(f'Tests are running in {BROWSER} browser')

pytest_run = [f'--browser={BROWSER}']


if MARKER is not None:
  print(f'{MARKER}')
  pytest_run += ['-m', f'{MARKER}']
  

if 'parallel' in MARKER:
  pytest_run += ['-n4']
else:
  pytest_run += ['-n1']
  
  
sys.exit(pytest.main(pytest_run))