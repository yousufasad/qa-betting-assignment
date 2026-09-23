
# QA Betting Assignment

QA automation and manual testing submission for the Single Bet Placement
feature of the betting application.

## Overview

This repository contains:

- Prioritized manual test plan
- Test execution results
- Defect reports with evidence
- Selenium + Pytest UI automation
- Requests + Pytest API automation
- Test strategy and recommendations

The automation framework is intentionally kept small and maintainable,
using the Page Object Model for UI tests.

---

## Application

Application:

https://qae-assignment-tau.vercel.app/

API Documentation:

https://qae-assignment-tau.vercel.app/api/docs

Feature under test:

Single Bet Placement

Scope:

- Desktop web
- Football/Soccer
- Upcoming/pre-match matches
- Single bets

---

## Technology Stack

- Python 3
- Pytest
- pytest-html
- Selenium WebDriver
- Requests
- Chrome
- Page Object Model
- XPath locators

### Run UI Test 
pytest tests/ui/test_single_bet.py 

### Run API 
Test pytest tests/api/test_bet_api.py 

### Generate HTML Report 
pytest tests/ui/test_single_bet.py --html=test-report.html --self-contained-html

pytest tests/api/test_bet_api.py --html=test-report.html --self-contained-html
