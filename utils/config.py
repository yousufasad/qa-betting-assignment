# Configuration settings for the QA automation framework

import os

# Base URL of the Sporty QA assignment application
BASE_URL = "https://qae-assignment-tau.vercel.app"

# Read USER_ID from environment variable
USER_ID = os.getenv(
    "USER_ID",
    "candidate-XBDm8Gl4Ygz6"
)