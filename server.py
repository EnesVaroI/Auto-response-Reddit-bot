import os
import praw
from flask import Flask, send_from_directory, render_template, redirect

app = Flask(__name__)

port = int(os.environ.get("PORT", 5000))

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/<path:path>')
def all_routes(path):
    return redirect('/')

client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']
username = os.environ['USERNAME']
password = os.environ['PASSWORD']

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent="botscript by me",
    username=username,
    password=password
)

print("Reddit user name:")
print(reddit.user.me().name)

if __name__ == "__main__":
    reddit.redditor("Sapotis").message("text", "text")
    app.run(port=port)
