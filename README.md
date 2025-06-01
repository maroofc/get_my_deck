# Steam Deck Stock Checker

This script monitors the Steam Deck refurbished store page and sends SMS notifications when a Steam Deck becomes available.

## Setup

1. Install the required Python packages:
```bash
pip install selenium webdriver-manager twilio
```

2. Configure your Twilio credentials and phone numbers in `config.py`:
```python
TWILIO_ACCOUNT_SID = "your_account_sid"
TWILIO_AUTH_TOKEN = "your_auth_token"
TWILIO_PHONE_NUMBER = "your_twilio_number"
RECIPIENT_PHONE_NUMBER = "your_phone_number"
```

## Configuration

You have two options for configuring your credentials and settings:

### 1. Simple (Beginner): Edit `config.py` Directly

Open `config.py` and fill in your details:
```python
TWILIO_ACCOUNT_SID = "your_account_sid"
TWILIO_AUTH_TOKEN = "your_auth_token"
TWILIO_PHONE_NUMBER = "your_twilio_number"
RECIPIENT_PHONE_NUMBER = "your_phone_number"
STEAM_DECK_URL = "https://store.steampowered.com/sale/steamdeckrefurbished"
```

### 2. Recommended (Secure): Use a `.env` File

1. Install the `python-dotenv` package:
   ```bash
   pip install python-dotenv
   ```
2. Create a file named `.env` in your project root with the following structure:
   ```env
   TWILIO_ACCOUNT_SID=your_account_sid
   TWILIO_AUTH_TOKEN=your_auth_token
   TWILIO_PHONE_NUMBER=+1234567890
   RECIPIENT_PHONE_NUMBER=+1234567890
   STEAM_DECK_URL=https://store.steampowered.com/sale/steamdeckrefurbished
   ```
3. The script will automatically load these values. **Do not share your `.env` file or commit it to public repositories.**
4. You can provide a `.env.example` (with placeholder values) for others to use as a template.

## Switching Between Chrome and Firefox

The script can use either Chrome or Firefox as the web driver. To switch between them:

### For Chrome:
1. Install Chrome browser if you haven't already
2. Modify `get_my_deck.py` to use Chrome imports and driver:
```python
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# In the start() function:
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=browser_options)
```

### For Firefox:
1. Install Firefox browser if you haven't already
2. Use the current Firefox configuration in `get_my_deck.py`:
```python
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

# In the start() function:
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service, options=browser_options)
```

## Running the Script

Simply run:
```bash
python get_my_deck.py
```

The script will:
1. Check the Steam Deck store page every 20 seconds
2. Send an SMS notification when a Steam Deck becomes available
3. Automatically restart the browser every 11 checks to prevent memory issues

## Notes
- The script uses headless mode by default (browser runs in the background)
- Make sure you have a stable internet connection
- The script will continue running until you stop it (Ctrl+C)
