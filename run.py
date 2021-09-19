"""
Module for tests running with parameters described in README file.
"""
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
                    help='Marker to tests run',
                    choices=[
                      'amazon',
                      'heroku'
                      ])

args = parser.parse_args()
BROWSER = args.browser
MARKER = args.m

print(f'Tests are running in {BROWSER} browser')

pytest_run = [f'--browser={BROWSER}']

if 'amazon' in MARKER:
  pytest_run += ['n1']
else:
  pytest_run += ['n4']
  
if MARKER:
  print(f'Tests running with {MARKER}')
  pytest_run += ['-m', f'{MARKER}']
  
sys.exit(pytest.main(pytest_run))