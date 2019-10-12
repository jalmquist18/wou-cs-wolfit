from datetime import datetime, timedelta

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
