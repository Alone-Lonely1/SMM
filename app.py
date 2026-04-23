from flask import Flask, jsonify, request
import PAID

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend is running!"

@app.route("/run")
def run_paid():
    package_type = request.args.get("type")

    try:
        if package_type == "month":
            PAID.main()
            return jsonify({"status": "month success"})

        elif package_type == "daily":
            PAID.main()
            return jsonify({"status": "daily success"})

        else:
            return jsonify({"status": "invalid type"})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
