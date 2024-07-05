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


@babel.localeselector
def get_locale() -> Union[str, None]:
    """Determines the preferred language for the user.

    Returns:
        str: Preferred language for the user.
    """
    value = request.args.get("locale")
    if value in app.config["LANGUAGES"]:
        return value
    return request.accept_languages.best_match(app.config["LANGUAGES"])


users: Mapping[int, Mapping[str, Union[str, None]]] = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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


@app.route("/", methods=["GET"])
def welcome_page() -> str:
    """Renders the HTML welcome page.

    Returns:
        str: Rendered HTML welcome page.
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
