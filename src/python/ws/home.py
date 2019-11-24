import pandas as pd
from flask import Blueprint

home = Blueprint("home", __name__, url_prefix="/")


@home.route("/")
def hello():
    df = pd.DataFrame({
        'a': [1, 2, 3],
        'b': [11, 33, 22]}
    )
    return df.to_json()
