# Alert Levels for KuCoin

## Overview
`alert_levels_tg.py` is a Python script designed to analyze cryptocurrency trading volumes on the KuCoin exchange and generate alerts for significant volume spikes. It supports customizable alert thresholds and integrates with messaging services for notifications.

## Features
- Analyzes trading volume data from KuCoin.
- Generates alerts for volume spikes based on predefined thresholds.
- Supports integration with Telegram for sending real-time notifications.

## Dependencies
- Python 3.x
- Requests: For making API calls to KuCoin.
- pandas: For data manipulation and analysis.

## Setup
1. Ensure Python 3.x is installed on your system.
2. Install required Python packages:
3. Configure your KuCoin API credentials and Telegram bot token in respective configuration files.

## Usage
Import `alert_levels_tg.py` into your trading analysis script or bot, and call the `get_volume_alert_details` function with current volume, previous mean volume, the symbol of interest, and the desired time interval.

```python
from alert_levels_tg import get_volume_alert_details

# Example usage
curr_volume = 12000
prev_volume_mean = 8000
symbol = "BTC-USDT"
interval = "1h"
alerts = get_volume_alert_details(curr_volume, prev_volume_mean, symbol, interval)

for alert in alerts:
 print(alert)
```

##Customization
Modify the thresholds list in alert_levels_tg.py to adjust the volume spike levels that trigger alerts.

##Contributing
Contributions to improve alert_levels_tg.py are welcome. Please feel free to fork the repository, make your changes, and submit a pull request.

##License
This script is released under the MIT License. 
