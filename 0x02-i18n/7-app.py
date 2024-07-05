#!/usr/bin/env python3
"""This module helps with internalization and localization of the application.

    Config - contains configuration settings for the application.

    get_locale:
        Returns the preferred language for the user.

    welcome_page:
        Renders and returns the HTML welcome page.
"""

from flask_babel import Babel
from flask import Flask, render_template, request, g
from typing import Mapping, Union
import pytz
from datetime import datetime


class Config:
    """config available languages for the babel
        Language config
        Locale config
        Timezone config
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Instantiate the flask application
app = Flask(__name__)

# load configuration from class config object
app.config.from_object(Config)

# Instantiate Babel application to start babel
babel = Babel(app)


users: Mapping[int, Mapping[str, Union[str, None]]] = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.timezoneselector
def get_timezone() -> str:
    """Determine the preferred timezone for the user"""

    # Get timezone from url parameters
    value = request.args.get("timezone")
    if value:
        try:
            pytz.timezone(value)
            return value
        except pytz.exceptions.UnknownTimeZoneError:
            return None

    # Get timezone from user setting
    if g.user:
        try:
            value = g.user["timezone"]
            pytz.timezone(value)
            return value
        except pytz.exceptions.UnknownTimeZoneError:
            return None

    # Use default timezone
    return app.config["BABEL_DEFAULT_TIMEZONE"]


@babel.localeselector
def get_locale() -> Union[str, None]:
    """Determines the preferred language for the user.

    Returns:
        str: Preferred language for the user.
    """
    value = request.args.get("locale")

    #  Get locale from url parameters
    if value is not None and value in app.config["LANGUAGES"]:
        return value

    # Get locale from users setting
    if g.user and g.user["locale"] in app.config["LANGUAGES"]:
        return g.user["locale"]

    # Get locale from request header
    preferred_lang = request.accept_languages.values()
    if preferred_lang:
        return request.accept_languages.best_match(preferred_lang)

    # Use the default language
    return app.config["BABEL_DEFAULT_LOCALE"]


def get_user() -> Union[Mapping[str, Union[str, None]], None]:
    """Get user information from the database"""
    login_info = request.args.get('login_as')
    if login_info:
        return users.get(int(login_info), None)
    return None


@app.before_request
def before_request() -> None:
    """handle before request"""
    value = get_user()
    if value:
        g.user = value
    else:
        g.user = None


@app.route("/", methods=["GET"])
def welcome_page() -> str:
    """Renders the HTML welcome page.

    Returns:
        str: Rendered HTML welcome page.
    """
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
