import yaml

from config import *
from google.cloud import storage


storage_client = storage.Client()


def load_story(story_id):
	# Download story yaml from Google Cloud Storage
	bucket = storage_client.get_bucket(BUCKET_NAME)
	blob_path = '{}/{}'.format(story_id, STORY_FILENAME)
	blob = bucket.blob(blob_path)
	file_path = '/tmp/{}'.format(STORY_FILENAME)
	blob.download_to_filename(file_path)
	# Load story file
	with open(file_path) as f:
		data = f.read()
	return yaml.load(data, Loader=yaml.FullLoader)
