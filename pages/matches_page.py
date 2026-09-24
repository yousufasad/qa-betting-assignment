from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MatchesPage:
    """
    Page Object for the football match list.
    """

    # Locator for all match cards displayed on the matches page
    MATCH_CARDS = (
        By.XPATH,
        "//div[contains(@class,'matchCard')]"
    )

    def __init__(self, driver):

       # Initialize the WebDriver and explicit wait
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self, url):

        # Open the application and
        self.driver.get(url)

        #wait until a match is displayed.
        self.wait.until(
            EC.presence_of_element_located(
                self.MATCH_CARDS
            )
        )

    def select_first_away_odds(self):

        # Wait until all match cards are present on the page
        matches = self.wait.until(
            EC.presence_of_all_elements_located(
                self.MATCH_CARDS
            )
        )

        # Select the first match card from the list
        first_match = matches[0]

        # Find the Away (2) odds button inside the first match
        away_button = first_match.find_element(
            By.XPATH,
            ".//button[contains(@id,'-away')]"
        )

        # Get the odds value from the Away button
        odds = away_button.find_element(
            By.XPATH,
            ".//*[contains(@class,'oddsButtonValue')]"
        ).text

        # Select the Away (2) betting option
        away_button.click()

        # Return the selected Away odds value
        return odds