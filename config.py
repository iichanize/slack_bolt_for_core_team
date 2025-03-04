from dotenv import load_dotenv
load_dotenv()

import os
SLACK_BOT_TOKEN = os.getenv('SLACK_BOT_TOKEN')
SLACK_APP_TOKEN = os.getenv('SLACK_APP_TOKEN')
TARGET_CHANNEL_ID = os.getenv('TARGET_CHANNEL_ID')
SLACK_SIGNING_SECRET = os.getenv('SLACK_SIGNING_SECRET')