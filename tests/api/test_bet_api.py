import requests

from utils.config import BASE_URL, USER_ID


def test_api_rejects_stake_above_balance():
    """
    API test for insufficient balance validation.

    Why this test was selected:
    Insufficient balance is an important business rule.
    API testing validates the rule directly without
    depending on the UI.
    """

    # Add the user ID to the request header for API authentication
    headers = {
        "x-user-id": USER_ID
    }

    # Get current balance
    balance_response = requests.get(
        f"{BASE_URL}/api/balance",
        headers=headers,
        timeout=10
    )

    # Verify the balance API returns a successful response
    assert balance_response.status_code == 200

    # Extract the current balance from the API response
    balance = balance_response.json()["balance"]

    # Get an available match from the API
    matches_response = requests.get(
        f"{BASE_URL}/api/matches",
        headers=headers,
        timeout=10
    )

    # Verify the matches API returns a successful response
    assert matches_response.status_code == 200

    # Get the match from the API response
    match = matches_response.json()[0]

    # Create a stake greater than the available balance
    invalid_stake = balance + 1

    # Create the request body with the match, selection, and invalid stake
    request_body = {
        "matchId": match["id"],
        "selection": "HOME",
        "stake": invalid_stake
    }

    # Send the bet request with an invalid stake
    response = requests.post(
        f"{BASE_URL}/api/place-bet",
        headers=headers,
        json=request_body,
        timeout=10
    )

    # Verify that the API rejects the invalid bet
    assert response.status_code == 422