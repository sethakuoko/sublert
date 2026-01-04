#!/usr/bin/python

# Slack webhooks for notifications
posting_webhook = "https://hooks.slack.com/services/<secret>"
errorlogging_webhook = "https://hooks.slack.com/services/<secret>"
slack_sleep_enabled = True  # bypass Slack rate limit when using free workplace, switch to False if you're using Pro/Ent version.
at_channel_enabled = True   # Add @channel notifications to Slack messages, switch to False if you don't want to use @channel

# Telegram Bot Configuration
telegram_bot_token = "YOUR_BOT_TOKEN_HERE"  # Get from @BotFather
telegram_chat_id = "YOUR_CHAT_ID_HERE"      # Your chat/group ID

# Telegram Error Logging (optional, can use same bot)
telegram_error_bot_token = "YOUR_BOT_TOKEN_HERE"
telegram_error_chat_id = "YOUR_ERROR_CHAT_ID_HERE"

# Rate limiting
telegram_sleep_enabled = True  # Changed from slack_sleep_enabled

# Mention all users (Telegram doesn't have @channel, so disabled by default)
mention_all_enabled = False  # Changed from at_channel_enabled

# crtsh postgres credentials, please leave it unchanged.
DB_HOST = 'crt.sh'
DB_NAME = 'certwatch'
DB_USER = 'guest'
DB_PASSWORD = ''
