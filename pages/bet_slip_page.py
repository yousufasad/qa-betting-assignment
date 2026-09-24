from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BetSlipPage:
    """
    Page Object for the Bet Slip and success receipt.
    """

    # Locator for the stake input field in the bet slip
    STAKE_INPUT = (
        By.XPATH,
        "//input[@id='bet-slip-stake-input']"
    )

    # Locator for the potential payout displayed in the bet slip
    POTENTIAL_PAYOUT = (
        By.XPATH,
        "//span[@id='bet-slip-potential-payout']"
    )

    # Locator for the Place Bet button in the bet slip
    PLACE_BET_BUTTON = (
        By.XPATH,
        "//button[@id='bet-slip-place-bet']"
    )

    # Locator for the potential payout shown in the success receipt
    SUCCESS_PAYOUT = (
        By.XPATH,
        "//span[@id='modal-success-payout']"
    )

    def __init__(self, driver):

        # Initialize the WebDriver and explicit wait
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def enter_stake(self, amount):

        # Wait until the stake input is visible
        stake_input = self.wait.until(
            EC.visibility_of_element_located(
                self.STAKE_INPUT
            )
        )

        # Clear the existing stake and enter the new amount
        stake_input.clear()
        stake_input.send_keys(str(amount))

    def get_potential_payout(self):

        # Wait until the potential payout is visible
        payout = self.wait.until(
            EC.visibility_of_element_located(
                self.POTENTIAL_PAYOUT
            )
        )

        # Remove the € symbol and extra spaces, then return the payout value
        return payout.text.replace("€", "").strip()

    def click_place_bet(self):

        # Wait until the Place Bet button is clickable
        button = self.wait.until(
            EC.element_to_be_clickable(
                self.PLACE_BET_BUTTON
            )
        )

        # Click the Place Bet button
        button.click()

    def get_success_receipt_payout(self):

        # Wait until the success receipt payout is visible
        payout = self.wait.until(
            EC.visibility_of_element_located(
                self.SUCCESS_PAYOUT
            )
        )

        # Remove the € symbol and extra spaces, then return the payout value
        return payout.text.replace("€", "").strip()