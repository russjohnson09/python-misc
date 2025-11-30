https://docs.astral.sh/uv/guides/projects/

https://flask.palletsprojects.com/en/stable/quickstart/


uv init
uv add flask
uv run -- flask run -p 8082

docker build . -t flask-api
docker run -p 8082:8000 flask-api



https://flask.palletsprojects.com/en/stable/tutorial/deploy/


https://flask.palletsprojects.com/en/stable/deploying/gunicorn/