# Test Plan — Single Bet Placement Feature

**Author:** Asad Yousuf
**User ID under test:** candidate-XBDm8Gl4Ygz6
**Application:** https://qae-assignment-tau.vercel.app
**API docs:** https://qae-assignment-tau.vercel.app/api/docs
**Platform:** Desktop web (Chrome, latest)
**Spec reference:** Single Bet Placement Feature Specification

## TC-01 – Successful Single Bet Placement

**Priority:** Critical

**Risk Rationale:**
Bet placement is the core business flow. Failure can prevent users from placing valid bets.

**Preconditions:**
- Valid user is logged in.
- An upcoming football match is available.

**Steps:**
1. Select an outcome from an upcoming football match.
2. Enter a valid stake.
3. Click Place Bet.
4. Review the success receipt and Bet Slip.

**Expected Result:**
- Bet is successfully placed.
- Receipt displays Bet ID, match, selection, stake, odds, potential payout and timestamp.
- Balance is reduced by the stake.
- Bet Slip is cleared.

**Execution Result: FAIL**

## TC-02 – Minimum Stake Boundary

**Priority:** High

**Risk Rationale:**
Incorrect minimum-stake validation could allow invalid bets or reject valid bets.

**Preconditions:**

- Valid user is logged in.
- An upcoming football match is available.

**Steps:**

1. Select an outcome from an upcoming football match.
2. Enter €0.99 as the stake.
3. Verify the validation behavior.
4. Change the stake to €1.00.
5. Verify the Place Bet action.

**Expected Result:**

- €0.99 is rejected.
- €1.00 is accepted as the minimum valid stake.

**Execution Result: PASS**

## TC-03 – Maximum Stake Boundary

**Priority:** High

**Risk Rationale:**
The maximum stake protects the application from accepting bets above the configured limit.

**Preconditions:**

- Valid user is logged in.
- Sufficient balance is available.
- An upcoming football match is available.

**Steps:**

1. Select an outcome from an upcoming football match.
2. Enter €100.00 as the stake.
3. Verify that the bet can be placed.
4. Change the stake to €100.01.
5. Verify the Place Bet button.

**Expected Result:**

- €100.00 is accepted and Place Bet is enabled.
- €100.01 is rejected and Place Bet is disabled or greyed out.

**Execution Result: PASS**

## TC-04 – Insufficient Balance Validation

**Priority:** High

**Risk Rationale:**
Users must not be able to place a bet greater than their available balance.

**Preconditions:**

- Valid user is logged in.
- An upcoming football match is available.
- Available balance is known.

**Steps:**

1. Note the available balance.
2. Select an outcome from an upcoming football match.
3. Enter a stake greater than the available balance.
4. Verify the Place Bet action.

**Expected Result:**

- Bet placement is prevented.
- An insufficient-balance validation is displayed.
- No amount is deducted from the balance.

**Execution Result: PASS**

## TC-05 – Replace Selected Outcome

**Priority:** High

**Risk Rationale:**
The application supports only one active selection. Incorrect selection handling could result in the wrong outcome being submitted.

**Preconditions:**

- Valid user is logged in.
- An upcoming football match is available.

**Steps:**

1. Select an outcome from an upcoming football match.
2. Select a different outcome for the same match.
3. Review the Bet Slip.

**Expected Result:**

- The previous selection is replaced.
- Only the latest selection is shown in the Bet Slip.
- The odds and potential payout correspond to the latest selection.

**Execution Result: PASS**

## TC-06 – Receipt and Balance Consistency

**Priority:** Critical

**Risk Rationale:**
Incorrect receipt or balance information can result in incorrect transaction information being displayed to the user.

**Preconditions:**

- Valid user is logged in.
- An upcoming football match is available.
- Sufficient balance is available.

**Steps:**

1. Select an outcome from an upcoming football match.
2. Enter a valid stake.
3. Note the stake, odds and potential payout in the Bet Slip.
4. Place the bet.
5. Compare the receipt with the Bet Slip.
6. Check the displayed balance after placement.

**Expected Result:**

- Receipt values match the Bet Slip.
- Potential payout equals stake x selected odds.
- Match and selection details are correct.
- Balance is updated after successful placement.

**Execution Result: FAIL**
