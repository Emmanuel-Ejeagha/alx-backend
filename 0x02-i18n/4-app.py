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
    """Config available languages for the babel
        Language config
        Locale config
        Timezone config
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCAL = "en"
    BABEL_DAFAULT_TIMEZONE = "UTC"
    

app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """Determines the preferred language for the user.
    Returns:
        str: Preferred language of the user.
    """
    value = request.args.get("locale")
    if value in app.config["LANGUAGES"]:
        return value
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/', methoss=["GET"])
def welcome_page() -> str:
    """Renders the HTML welcome page.
    Returns:
        str: Rendered HTML welcome page.
    """
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')