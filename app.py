import json
import yaml

from config import *
from datetime import date
from flask import escape, Flask, render_template, request
from google.cloud import storage


app = Flask(__name__)

storage_client = storage.Client()
bucket = storage_client.get_bucket(BUCKET_NAME)


@app.route('/', methods=['GET'])
def index():
	story_id = request.args.get('story_id')

	blob_path = '{}/story.yaml'.format(story_id)
	blob = bucket.get_blob(blob_path)
	data = blob.download_as_string()
	story = yaml.load(data, Loader=yaml.FullLoader)

	filename = '{}.html'.format(story['model'])
	today = date.today()
	date_str = today.strftime('%b %d')
	year_str = today.strftime('%Y')
	subtitle = escape(story['subtitle'])
	title = [escape(part) for part in story['title']]
	return render_template(filename,
						   date=date_str,
						   duration=story['duration'],
						   story_id=story_id,
						   subtitle=json.dumps(subtitle),
						   title_parts=json.dumps(title),
						   year=year_str)


@app.route('/captions/<story_id>', methods=['GET'])
def get_captions(story_id):
	blob_path = '{}/captions.vtt'.format(story_id)
	blob = bucket.get_blob(blob_path)
	return blob.download_as_string()
