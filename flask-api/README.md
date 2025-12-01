
uv run -- flask --debug run -p 8082


https://docs.astral.sh/uv/guides/projects/

https://flask.palletsprojects.com/en/stable/quickstart/


uv init
uv add flask



# Deploy new version
git pull
docker build . -t flask-api
docker stop flask-api
docker rm flask-api
docker run --name=flask-api -v ./static:/app/static -d -p 8085:8000 flask-api

curl localhost:8085/test/test.html


## Nginx and letsencrypt setup
cp flask-api.conf /etc/nginx/sites-enabled/
/etc/init.d/nginx reload 

curl flask-api.localhost

curl flask-api.ihateiceforfree.com

sudo certbot certonly --webroot --webroot-path ./static --domains flask-api.ihateiceforfree.com
sudo certbot

choose flask-api.ihateiceforfree.com




https://flask.palletsprojects.com/en/stable/tutorial/deploy/


https://flask.palletsprojects.com/en/stable/deploying/gunicorn/