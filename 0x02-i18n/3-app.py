#!/usr/bin/env python3
"""This module helps with internalization and localization of the application.

    Config - contains configuration settings for the application.

    get_locale:
        Returns the preferred language for the user.

    welcome_page:
        Renders and returns the HTML welcome page.
"""

from flask_babel import Babel
from flask import Flask, render_template, request


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

# Instantiate Babel to manage localization and internationlization
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Determines the preferred language for the user.

    Returns:
        str: Preferred language for the user.
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/", methods=["GET"])
def welcome_page() -> str:
    """Renders the HTML welcome page.

    Returns:
        str: Rendered HTML welcome page.
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
