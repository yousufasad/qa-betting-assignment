# QA Betting Assignment

QA automation and manual testing submission for the **Single Bet Placement** feature of the Sporty betting application.

The project includes a prioritized test plan, execution results, defect reports, and UI/API automation.

---

## Project Overview

### Feature Under Test

**Single Bet Placement**

### Scope

* Desktop web application
* Football/Soccer
* Upcoming/pre-match matches
* Single bets only

### Out of Scope

* Live betting
* Multi/accumulator bets
* Other sports
* Mobile UX testing

---

## Repository Structure

```text
qa-betting-assignment/
│
├── README.md
├── .gitignore
├── conftest.py
├── pytest.ini
├── requirements.txt
│
├── docs/
│   ├── test_plan.md
│   ├── execution_and_bug_reports.md
│   ├── strategy_and_recommendations.md
│   └── screenshots/
│
├── pages/
│   ├── matches_page.py
│   └── bet_slip_page.py
│
├── tests/
│   ├── api/
│   │   └── test_bet_api.py
│   └── ui/
│       └── test_single_bet.py
│
└── utils/
    └── config.py
```

---

## Documentation

### Test Plan

`docs/test_plan.md`

Contains the prioritized manual test scenarios and execution status.

### Execution & Bug Reports

`docs/execution_and_bug_reports.md`

Contains test execution results, identified defects, severity/priority, and reproduction details.

Defect evidence is available in:

`docs/screenshots/`

### Strategy & Recommendations

`docs/strategy_and_recommendations.md`

Contains the testing strategy, risk areas, automation approach, and recommendations.

---

## Technology Stack

* Python 3
* Pytest
* Selenium WebDriver
* Requests
* pytest-html
* Chrome
* Page Object Model (POM)

---

## Setup

Clone the repository:

```bash
git clone https://github.com/yousufasad/qa-betting-assignment.git
cd qa-betting-assignment
```

Create a virtual environment:

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running Tests

### UI Test

```bash
pytest tests/ui/test_single_bet.py
```

### API Test

```bash
pytest tests/api/test_bet_api.py
```

### Run All Tests

```bash
pytest
```

---

## HTML Test Reports

Generate an HTML report for the UI test:

```bash
pytest tests/ui/test_single_bet.py --html=test-report.html --self-contained-html
```

Generate an HTML report for the API test:

```bash
pytest tests/api/test_bet_api.py --html=test-report.html --self-contained-html
```

Generated HTML reports are excluded from Git using `.gitignore`.

---

## Automation Coverage

### UI Automation

The UI test covers the critical single-bet flow:

```text
Open Application
      ↓
Select Odds
      ↓
Enter Stake
      ↓
Validate Potential Payout
      ↓
Place Bet
      ↓
Validate Success Receipt
```

### API Automation

The API test validates insufficient-balance handling:

```text
Get Balance
      ↓
Get Match
      ↓
Use Stake Above Balance
      ↓
POST /api/place-bet
      ↓
Verify HTTP 422
```

---

## Known Automation Result

The UI automation intentionally detects an existing application defect:

**BUG-02 — Incorrect Potential Payout in Success Receipt**

Example:

```text
Expected payout: €2.80
Actual receipt payout: €2.00
```

The assertion is intentionally kept so the automation demonstrates that it can detect the application defect.

---

## Test Configuration

Application configuration is maintained in:

```text
utils/config.py
```

The configuration includes the application base URL and test user ID.

---

## Author

**Yousuf Asad**

QA Engineer | Manual & Automation Testing
