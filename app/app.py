from flask import Flask, request, jsonify
import os
import redis

app = Flask(__name__)
r = redis.Redis(host=os.getenv('REDIS_HOST', 'localhost'), port=6379, decode_responses=True)

@app.route('/health')
def health():
    return jsonify({"status": "ok", "version": os.getenv("APP_VERSION", "1.0.0")})

@app.route('/ready')
def ready():
    try:
        r.ping()
        return jsonify({"status": "ready"})
    except:
        return jsonify({"status": "not ready"}), 503

@app.route('/')
def index():
    try:
        visites = r.incr('visites')
        return jsonify({"message": "Bienvenue sur l'application Relevés", "visites": visites, "version": os.getenv("APP_VERSION", "1.0.0")})
    except:
        return jsonify({"erreur": "Redis non disponible"}), 503

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
