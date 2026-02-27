# import os
# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Hello from Railway with Gunicorn!"

# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 8080))
#     app.run(host="0.0.0.0", port=port)

from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # Load your portfolio page

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)