#!/usr/bin/env python3
"""
    This module helps me to learn about internalization and localization
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False, methods=["GET"])
def welcome_page():
    """Welcome page for our application"""

    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
