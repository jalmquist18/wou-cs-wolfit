#!/bin/bash
export WOLFIT_SETTINGS=$(pwd)/dev.settings
export ACTIVITY_LOGGER="wolfit-activity-log.herokuapp.com"
flask run --host=0.0.0.0
