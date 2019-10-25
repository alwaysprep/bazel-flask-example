from flask import Flask
import pandas as pd

app = Flask(__name__)


@app.route('/')
def hello_world():
    df = pd.DataFrame({
        'a': [1, 2, 3],
        'b': [11, 33, 22]}
    )
    return df.to_json()


if __name__ == '__main__':
    app.run()
