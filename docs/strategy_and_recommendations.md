# Test Strategy & Recommendations

## 1. Automation Approach

The automation framework uses Python, Selenium WebDriver, Pytest and requests.

The framework follows a simple Page Object Model structure for UI tests.
Configuration such as the application URL and User ID is maintained separately
in `utils/config.py`.

The goal is to keep the framework small, readable and easy to maintain.

## 2. Why These Two Tests Were Automated

### UI Automation – Single Bet Placement

The single bet journey was selected because it is the core business flow
of the application.

The automated test validates:

- Opening the application
- Selecting match odds
- Entering a valid stake
- Calculating the expected payout
- Validating the Bet Slip payout
- Placing the bet
- Validating the success receipt payout

This provides end-to-end coverage of the main user journey.

### API Automation – Insufficient Balance

The insufficient balance rule was selected because it is an important
backend business rule.

The API test validates that:

- The current balance can be retrieved
- An available match can be retrieved
- A stake greater than the available balance is rejected
- The API returns HTTP 422 for the invalid request

API automation provides faster feedback and validates the business rule
without depending on the UI.

## 3. Manual Testing Areas

The following areas remain suitable for manual and exploratory testing:

- Exploratory testing
- Visual and UI validation
- Usability checks
- Cross-browser testing
- Error message validation
- Unusual user interactions
- New or frequently changing functionality
- Regression scenarios not yet automated
- Mobile and responsive checks if they become in scope

## 4. Recommendations for Scaling

### Recommendation 1 – CI/CD Integration

Run the API tests and critical UI smoke tests as part of CI/CD.

A typical flow would be:

Code Change
→ Build
→ API Tests
→ UI Smoke Tests
→ Report
→ Notify

### Recommendation 2 – Test Data Management

Use controlled test data and reset it before each test so that start from a known state.

The automation already uses the balance reset API to provide a consistent starting balance. 
This approach should be continued as more tests are added to keep the tests independent and repeatable. 

### Recommendation 3 – Expand API Coverage

The current API automation covers insufficient balance validation. 
As the framework grows, additional API tests can be added for:

- Authentication/User ID validation
- Invalid requests
- Minimum and maximum stake validation
- Odds validation
- Successful bet placement
- Invalid match selections

## 5. Overall Strategy

The recommended approach is to automate stable, high-value and repeatable
business flows while keeping exploratory, visual and frequently changing
areas for manual testing.

Keep the automation framework simple and easy to maintain as the application
grows.

## 6. Requirement Clarification

There is difference in feature specification document regarding the minimum stake (€1.00 and €1.01). 
The expected value should be confirmed to ensure consistent testing.
