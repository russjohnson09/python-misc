uv run -- flask --debug run -p 8082 -h localhost



# Extend using volume

systemctl stop docker


https://forums.docker.com/t/how-do-i-change-the-docker-image-installation-directory/1169

https://superuser.com/questions/1326168/how-to-add-mount-block-storage-on-digitalocean-droplet-under-server-root


https://docs.digitalocean.com/products/volumes/how-to/expand-partitions/


sudo e2fsck -f /dev/disk/by-id/scsi-0DO_Volume_volume-nyc1-01-part1




https://docs.astral.sh/uv/guides/projects/

https://flask.palletsprojects.com/en/stable/quickstart/


uv init
uv add flask



# Deploy new version
docker container prune
docker image prune -all
git pull
git checkout main
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