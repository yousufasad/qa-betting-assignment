# Execution Results & Bug Reports

## Execution Summary

| Test Case | Result |
|---|---|
| TC-01 – Successful Single Bet Placement | FAIL |
| TC-02 – Minimum Stake Boundary | PASS |
| TC-03 – Maximum Stake Boundary | PASS |
| TC-05 – Replace Selected Outcome | PASS |
| TC-04 – Insufficient Balance Validation | PASS |
| TC-06 – Receipt and Balance Consistency | FAIL |

## Exploratory Checks

The following exploratory checks were also performed:

- Success receipt match ordering
- Success receipt potential payout
- Balance synchronization after successful bet
- Past match betting eligibility
- Initial Bet Slip balance visibility

## BUG-01 – Match Order Flipped in Success Receipt

**Severity:** High

### Reproduction Steps

1. Open the application with a valid user.
2. Select an upcoming football match.
3. Select a valid betting outcome.
4. Enter a valid stake.
5. Place the bet.
6. Compare the match order in the Bet Slip with the success receipt.

### Expected Result

The receipt should display the same home and away team order as the selected match.

### Actual Result

The match order is reversed in the success receipt.

Example:
- Bet Slip: Tottenham vs Liverpool
- Receipt: Liverpool vs Tottenham

### Business Impact

The confirmation receipt displays incorrect match information, which can cause confusion when users review their completed bet.

### Evidence

Observed across multiple successful bets.

### Screenshot
https://github.com/yousufasad/qa-betting-assignment/blob/db68f15d9046d53fe7c85141b50cdd07f2100cd8/docs/screenshots/bug-01-match-order-01.png

https://github.com/yousufasad/qa-betting-assignment/blob/1b24c9b690e16c3db7ba595e1d70339a704fc76c/docs/screenshots/bug-01-match-order-02.png

## BUG-02 – Incorrect Potential Payout in Success Receipt

**Severity:** Critical

### Reproduction Steps

1. Select an upcoming football match.
2. Select an outcome with odds other than 2.00.
3. Enter a valid stake.
4. Note the potential payout shown in the Bet Slip.
5. Place the bet.
6. Compare the payout on the receipt with the Bet Slip.

### Expected Result

Receipt payout should equal:
Stake × Selected Odds and should match the potential payout shown before placement.

### Actual Result

The receipt displays a different payout from the Bet Slip.

Examples:

- Stake €10 x Odds 2.40 = €24.00 in Bet Slip
- Receipt displayed €20.00

### Business Impact

The success receipt displays incorrect transaction information and may cause confusion when users verify their bet details.

### Evidence

Multiple successful bets reproduced the issue.

### Screenshot
https://github.com/yousufasad/qa-betting-assignment/blob/fc13cdaada6ef4d7517cccdb18eb7b8521d32642/docs/screenshots/bug-02-payout-01.png

https://github.com/yousufasad/qa-betting-assignment/blob/fde7b2c64eb17ad053955444df03faeced1f3d51/docs/screenshots/bug-02-payout-02.png

## BUG-03 – Balance Display Not Updated Until Page Reload

**Severity:** High

### Reproduction Steps

1. Note the current available balance.
2. Place a valid bet.
3. Observe the balance immediately after successful placement.
4. Reload the page.
5. Observe the balance again.

### Expected Result

The displayed balance should update immediately after successful bet placement.

### Actual Result

The displayed balance remains unchanged immediately after placement and updates only after page reload.

### Business Impact

The user may temporarily see an incorrect available balance after placing a bet.

### Evidence

Example:

Before bet: €125.50  
Immediately after bet: €125.50  
After reload: €115.50

## BUG-04 – Past Match Can Be Selected and Bet Placed

**Severity:** Critical

### Reproduction Steps

1. Open the application.
2. Locate a past football match.
3. Select an available outcome.
4. Enter a valid stake.
5. Click Place Bet.

### Expected Result

Past matches should not be eligible for betting. Only upcoming/pre-match events should be selectable.

### Actual Result

A past match can be selected and a bet can be successfully placed.

### Business Impact

The application allows betting on an event outside the defined pre-match betting scope.

### Evidence

Successful bet placement was observed on a past match.

### Screenshot
https://github.com/yousufasad/qa-betting-assignment/blob/7d6ea54b962d29cf22c8f519863636be5f828a4c/docs/bug-04-past-match-01.png

https://github.com/yousufasad/qa-betting-assignment/blob/fdd7bf1877e72b989558779fafb933a358b450a8/docs/bug-04-past-match-02.png


