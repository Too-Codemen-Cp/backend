from app.routes import app
import os

if __name__ == "__main__":
    if not os.path.isdir("static"):
        os.mkdir("static")

    app.run(debug=True, port=8000, host="0.0.0.0")