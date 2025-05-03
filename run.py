# run.py

from app import create_app

app = create_app()

if __name__ == "__main__":
    # optional: enable debug here or via FLASK_ENV=development
    app.run(host="0.0.0.0", port=5001)
