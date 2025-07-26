from flask import Flask, send_from_directory, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/songs')
def get_songs():
    songs = [f.split('.')[0] for f in os.listdir('music') if f.endswith('.mp3')]
    return jsonify(songs)

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    app.run(debug=True)
