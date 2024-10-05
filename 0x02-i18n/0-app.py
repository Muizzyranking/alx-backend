#!/usr/bin/env python3
"""
Module containing a simple flask app.
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    This serves as the home page of the flask app.
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
