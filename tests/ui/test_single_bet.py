from decimal import Decimal

from pages.matches_page import MatchesPage
from pages.bet_slip_page import BetSlipPage

from utils.config import BASE_URL, USER_ID


def test_successful_single_bet(driver, reset_balance):
    """
    E2E test for the critical single-bet journey.

    Why this test was selected:
    Bet placement is the core business flow of the application.

    Note: This test currently fails because the potential payout
    displayed in the receipt does not match the expected calculation.
    """

    # Create page objects for the matches page and bet slip
    matches_page = MatchesPage(driver)
    bet_slip = BetSlipPage(driver)

    # Open the application
    application_url = (
        f"{BASE_URL}/?user-id={USER_ID}"
    )

    # Open the application URL in the browser
    matches_page.open(application_url)

    # Select Away odds from the match
    selected_odds = Decimal(
        matches_page.select_first_away_odds()
    )

    # Enter a valid stake
    stake = Decimal("1.00")

    # Calculate the expected payout and round it to 2 decimal places
    expected_payout = (
        stake * selected_odds
    ).quantize(Decimal("0.01"))

    # Enter the stake amount in the bet slip
    bet_slip.enter_stake(stake)

    # Validate Bet Slip payout
    slip_payout = Decimal(
        bet_slip.get_potential_payout()
    )

    # Verify that the bet slip payout matches the expected payout
    assert slip_payout == expected_payout, (
        f"Expected payout €{expected_payout:.2f}, "
        f"but received €{slip_payout:.2f}"
    )

    # Place the bet
    bet_slip.click_place_bet()

    # Validate receipt payout
    receipt_payout = Decimal(
        bet_slip.get_success_receipt_payout()
    ).quantize(Decimal("0.01"))

    # Verify that the receipt payout matches the expected payout
    assert receipt_payout == expected_payout, (
        f"Expected receipt payout €{expected_payout:.2f}, "
        f"but received €{receipt_payout:.2f}"
    )