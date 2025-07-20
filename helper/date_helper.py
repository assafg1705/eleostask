import re
from datetime import datetime, timedelta
import logging
from helper.utils import log_message, LogLevel

logger = logging.getLogger("DateHelper")

def validate_date_format(date: str):
    log_message(logger, f"Validating date format for: {date}", LogLevel.INFO)

    # validate date is in format 'MM/DD/YYYY'
    if not re.match(r"^(0[1-9]|1[0-2])/(0[1-9]|[12]\d|3[01])/\d{4}$", date):
        log_message(logger, f"Invalid format: {date}", LogLevel.ERROR)
        raise ValueError("Date must be in MM/DD/YYYY format.")

    # validate date is valid - for example: ensure 02/30/2025 is invalid
    try:
        date_obj = datetime.strptime(date, "%m/%d/%Y")
    except ValueError:
        log_message(logger, f"Invalid calendar date: {date}", LogLevel.ERROR)
        raise ValueError("Invalid calendar date.")

    # validate date is within a range of 1 year
    today = datetime.today()
    one_year = timedelta(days=365)
    if not (today - one_year <= date_obj <= today + one_year):
        log_message(logger, f"Date out of range: {date}", LogLevel.ERROR)
        raise ValueError("Date must be within one year from today.")

def parse_date(date: str):
    date_obj = datetime.strptime(date, "%m/%d/%Y")
    month = date_obj.month
    day = date_obj.day
    year = date_obj.year

    return day, month, year