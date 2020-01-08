gcloud app deploy app.yaml \
	--project plasmic-compute-256214 \
	--quiet \
	--service story-overlay

gcloud app logs tail \
	--project plasmic-compute-256214 \
	--service story-overlay
