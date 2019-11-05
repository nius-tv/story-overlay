import json

from config import *
from flask import escape, Flask, render_template, request
from story import load_story


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
	show_bg = request.args.get('show_bg', False)
	story_id = request.args.get('story_id')
	
	story = load_story(story_id)
	print(story)

	date = escape('TODAY')
	subtitle = escape(story['subtitle'])
	title = [escape(part) for part in story['title']]
	return render_template(HTML_TEMPLATE_FILENAME,
						   date=date,
						   duration=story['duration'],
						   show_bg=show_bg,
						   subtitle=json.dumps(subtitle),
						   title_parts=json.dumps(title))
