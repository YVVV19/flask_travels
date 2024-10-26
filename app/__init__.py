from flask import Flask, render_template
from .db import (
    Config,
    Departure,
    Film,
)


app = Flask(__name__)


from . import routes