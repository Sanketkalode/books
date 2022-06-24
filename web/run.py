from app import create_app
from config import load_config

"""To start flask application run this file."""

if __name__ == "__main__":
    config = load_config()
    app = create_app(config)
    PORT = 5000
    app.run(host="0.0.0.0",port=PORT)
