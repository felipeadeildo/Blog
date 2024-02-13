from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(
    app,
    origins="http://localhost:5173",
    resources={r"/api/*": {"origins": "*"}},
    supports_credentials=True,
)

app.secret_key = "secret"

import api

app.register_blueprint(api.bp)


if __name__ == "__main__":
    app.run(debug=True, port=8866)
