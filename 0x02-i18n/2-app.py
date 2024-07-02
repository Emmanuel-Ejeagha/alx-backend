#!/usr/bin/env python3
"""
    This module helps me to learn about internalization and localization
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """config available languages for the babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Instantiate the flask application
app = Flask(__name__)

# load configuration from class config object
app.config.from_object(Config)

# Instantiate Babel
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Get locale languages"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/", strict_slashes=False, methods=["GET"])
def welcome_page():
    """Welcome page for our application"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')