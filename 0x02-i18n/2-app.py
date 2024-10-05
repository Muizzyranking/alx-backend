#!/usr/bin/env python3
"""
This module contains a Flask application with Babel integration
for handling translations and timezone settings.
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """
    Config class used to configure available
    languages, default locale, and timezone.
    """
    LANGUAGES = ["en", "fr"]

    BABEL_DEFAULT_LOCALE = "en"

    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Determine the best match for supported languages from the request.

    Uses the request's 'Accept-Language' headers to select
    the best match from the supported languages.

    Returns:
        The best matching language as a string.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    The index function serves the homepage of the application.
    It renders an HTML template called '2-index.html'.

    Returns:
        The rendered HTML template as a string.
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
