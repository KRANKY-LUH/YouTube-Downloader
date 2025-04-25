from flask import Flask, request, render_template, send_file
import yt_dlp
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    output_path = 'video.mp4'

    ydl_opts = {
        'format': 'best',
        'outtmpl': output_path
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        return f"Erreur lors du téléchargement : {e}"

    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
