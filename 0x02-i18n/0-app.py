#!/usr/bin/env python3
"""
Module containing a simple flask app.
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def root():
    """
    Home page.
    """
    return render_template('0-index.html')
