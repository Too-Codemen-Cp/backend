import os
from flask import (
    Flask,
    Response,
    request,
    jsonify,
    send_from_directory,
)
from werkzeug.utils import secure_filename

from .helpers import recognize_static

root_dir = os.path.dirname(os.path.abspath(__file__)).replace("/app", "")
UPLOAD_FOLDER = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "static",
)
app = Flask(
        __name__, static_folder=UPLOAD_FOLDER
)

app.config["TRAP_HTTP_EXCEPTIONS"] = True
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/<path:path>" , methods=["GET"])
def send_static(path) -> Response:
    return send_from_directory(UPLOAD_FOLDER, path)

@app.route("/file", methods=["POST"])
def upload_file() -> Response | tuple[Response, int]:
    try:
        file = request.files["file"]
        if file.filename:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            return jsonify({"result": recognize_static(filename)}, 200)
    except Exception as ex:
        return (
            jsonify(
                {
                    "result": "false",
                    "error_type": str(type(ex)),
                    "error_message": str(ex),
                }
            ),
            500,
        )