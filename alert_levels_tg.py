def get_volume_alert_details(curr_volume, prev_volume_mean, symbol, interval):
    alerts = []
    if curr_volume > prev_volume_mean * 15:
        alerts.append({
            "level": "1500%+",
            "curr_volume": curr_volume,
            "prev_volume_mean": prev_volume_mean,
            "symbol": symbol,
            "interval": interval
        })
    elif curr_volume > prev_volume_mean * 10:
        alerts.append({
            "level": "1000%+",
            "curr_volume": curr_volume,
            "prev_volume_mean": prev_volume_mean,
            "symbol": symbol,
            "interval": interval
        })
    elif curr_volume > prev_volume_mean * 7:
        alerts.append({
            "level": "700%+",
            "curr_volume": curr_volume,
            "prev_volume_mean": prev_volume_mean,
            "symbol": symbol,
            "interval": interval
        })
    elif curr_volume > prev_volume_mean * 5:
        alerts.append({
            "level": "500%+",
            "curr_volume": curr_volume,
            "prev_volume_mean": prev_volume_mean,
            "symbol": symbol,
            "interval": interval
        })

    return alerts
