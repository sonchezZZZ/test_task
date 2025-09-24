import os
from flask import Flask

app = Flask(__name__)

@app.route('/health')
def health():
    return "OK", 200

@app.route('/version')
def version():
    version = os.getenv("VERSION", "unknown")
    return version, 200
  
@app.errorhandler(404)
def not_found(e):
    return "No route to host", 404  # Mimic network-level message

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 80)))
