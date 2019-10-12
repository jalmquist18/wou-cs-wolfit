from datetime import datetime, timedelta

from time import time

from app.helpers import pretty_date


def test_just_now():
    assert pretty_date(datetime.utcnow()) == "just now"

def test_seconds_ago():
    assert pretty_date(datetime.utcnow() - timedelta(seconds=18)) == "18 seconds ago"

def test_a_minute_ago():
        assert pretty_date(datetime.utcnow() - timedelta(minutes=1)) == "a minute ago"

def test_minutes_ago():
    assert pretty_date(datetime.utcnow() - timedelta(minutes=2)) == "2 minutes ago"

def test_an_hour_ago():
        assert pretty_date(datetime.utcnow() - timedelta(hours=1)) == "an hour ago"

def test_hours_ago():
    assert pretty_date(datetime.utcnow() - timedelta(hours=7)) == "7 hours ago"

def test_from_time_stamp():
    assert pretty_date(int(time())-12) == "12 seconds ago"

def test_no_value_passed():
    assert pretty_date() == "just now"

def test_just_about_now():
    assert pretty_date(datetime.utcnow() + timedelta(seconds=1)) == "just about now"

def test_yesterday():
    assert pretty_date(datetime.utcnow() - timedelta(days=1)) == "Yesterday"

def test_days_ago():
    assert pretty_date(datetime.utcnow() - timedelta(days=3)) == "3 days ago"

def test_weeks_ago():
    assert pretty_date(datetime.utcnow() - timedelta(weeks=4)) == "4 weeks ago"

def test_months_ago():
    assert pretty_date(datetime.utcnow() - timedelta(weeks=50)) == "11 months ago"

def test_years_ago():
    assert pretty_date(datetime.utcnow() - timedelta(weeks=121)) == "2 years ago"
