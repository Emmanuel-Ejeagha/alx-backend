#!/usr/bin/env python3
"""Use Config to set Babel’s default locale ("en") and timezone ("UTC")."""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)

class Config:
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'

app.config.from_object(Config)
babel = Babel(app)


@app.route("/", strict_slashes=False, methods=["GET"])
def welcome_pg():
    """Welcome page"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
    