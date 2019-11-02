gcloud app deploy app.yaml \
	--project plasmic-compute-256214 \
	--quiet

gcloud app logs tail \
	--project plasmic-compute-256214 \
	--service story-overlay
