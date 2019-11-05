import json

from flask import escape, Flask, render_template


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
	date = escape('TODAY')
	duration = 30
	location = escape('<MWC> "LA')
	title_parts = [
		escape('NVIDIA'),
		escape('at & <Mobile> "World Congress:'),
		escape('5G Meets AI')
	]
	return render_template('512x1024.html',
						   date=date,
						   duration=duration,
						   location=json.dumps(location),
						   title_parts=json.dumps(title_parts))
