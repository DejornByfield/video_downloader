from flask import Blueprint, request, jsonify
from .downloader import download_video
from .models import Download 
from .database import db 

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return jsonify({"message: Video Downloader API is running!"})

@main.route('/download', methods=['POST'])
def download():
    data = request.get_json()
    url = data.get('url')

    if not url:
        return jsonify({'error': 'Missing URL'}), 400

    try:
        result = download_video(url)
        download = Download(
            url=url,
            title=result['title'],
            filepath=result['filepath'],
            filesize=str(result['filesize']),
        )
        db.session.add(download)
        db.session.commit()
        return jsonify({'message': 'Download successful!', 'video': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500