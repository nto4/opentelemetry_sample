import logging
from flask import Flask, jsonify

# Logger oluşturulması
logger = logging.getLogger('http_server_logger')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('server.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

app = Flask(__name__)

@app.route('/')
def index():
    logger.info("GET request received for path: /")
    # Respond with the file contents.
    try:
        with open('index.html', 'rb') as f:
            content = f.read()
        return content, 200, {'Content-Type': 'text/html'}
    except FileNotFoundError:
        return "File not found", 404

@app.route('/error')
def error():
    logger.error("Fake internal server error occurred")
    return jsonify({"error": "Fake internal server error"}), 500, {'Content-Type': 'application/json'}

if __name__ == "__main__":
    host = '0.0.0.0'
    port = 8000
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.DEBUG)
    print("Server started http://%s:%s" % (host, port))
    logger.info(f"Server started http://{host}:{port}")
    app.run(host=host, port=port, threaded=True)

