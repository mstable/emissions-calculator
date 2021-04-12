from datetime import datetime, timedelta


def iso_date_to_datetime(date_str):
    "Convert ISO date to Python datetime object"
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    return dt


def datetime_to_timestamp(dt):
    "Convert datetime to UNIX timestamp"
    timestamp = int((dt - datetime(1970, 1, 1)).total_seconds())
    return timestamp
