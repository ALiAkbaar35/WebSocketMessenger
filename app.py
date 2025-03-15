# app.py
# This file exists to provide the app object for Gunicorn
# It imports the app created by the create_app() factory function

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)