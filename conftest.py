# Pytest fixtures and test setup for the QA automation framework

import pytest
import requests

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.config import BASE_URL, USER_ID


@pytest.fixture
def driver():
    """
    Start Chrome before the UI test
    and close Chrome after the test.
    """

    # Create Chrome options and start the browser maximized
    options = Options()
    options.add_argument("--start-maximized")

    # Launch Chrome browser with the configured options
    driver = webdriver.Chrome(options=options)

    # Provide the browser driver to the test
    yield driver

    # Close the browser and end the WebDriver session
    driver.quit()

# Remove JAVA_HOME from the pytest HTML report metadata
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)


@pytest.fixture
def reset_balance():
    """
    Reset the balance before the test.

    This keeps the test independent and repeatable.
    """

    response = requests.post(
        f"{BASE_URL}/api/reset-balance",
        headers={"x-user-id": USER_ID},
        timeout=10
    )

    # Verify that the balance reset request was successful
    response.raise_for_status()
