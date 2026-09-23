# qa-betting-assignment

### Run UI Test

pytest tests/ui/test_single_bet.py

### Run API Test

pytest tests/api/test_bet_api.py

### Generate HTML Report

pytest tests/ui/test_single_bet.py --html=test-report.html --self-contained-html

pytest tests/api/test_bet_api.py --html=test-report.html --self-contained-html
