#!/usr/bin/env bash
set -e

# Copy config.ini.default if it exists and config.ini doesn't exist.
if [ -e config.ini.default ] && [ ! -e config.ini ]; then
    cp config.ini.default config.ini
    chmod a+w config.ini
fi

PYTHON=$(command -v python3)
VENV=venv

if [ -f "$PYTHON" ]; then

    if [ ! -d $VENV ]; then
        # Create a virtual environment if it doesn't exist.
        $PYTHON -m venv $VENV
    fi

    # Activate the virtual environment and install requirements.
    # shellcheck disable=SC1090
    . $VENV/bin/activate
    pip3 install -r requirements.txt

else
    >&2 echo "Cannot find Python 3. Please install it."
fi
