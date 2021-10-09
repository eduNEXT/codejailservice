import os

from codejailservice import app

if __name__ == "__main__":
    host = os.getenv("FLASK_CODEJAILSERVICE_HOST", "0.0.0.0")
    port = os.getenv("FLASK_CODEJAILSERVICE_PORT", 8000)
    app.run(host=host, port=port)

application = app
