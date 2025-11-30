
uv run -- flask run -p 8082



https://docs.astral.sh/uv/guides/projects/

https://flask.palletsprojects.com/en/stable/quickstart/


uv init
uv add flask



# Deploy new version
docker build . -t flask-api
docker run -p 8085:8000 flask-api



https://flask.palletsprojects.com/en/stable/tutorial/deploy/


https://flask.palletsprojects.com/en/stable/deploying/gunicorn/