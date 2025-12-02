https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-20-04

Image is tagged -t as  static-sites-hello. Container runs in background 
```
docker build . -t static-sites-hello
docker stop static-sites-hello
docker run -p 8080:80 -v ./static-html-directory:/usr/share/nginx/html:ro -d nginx
```

docker ps


curl localhost:8080


# Nginx 80 setup
Must be accessible on port 80 first hello.ihateiceforfree.com.

Then redirect.

cat /etc/

cp /root/python-misc/static-sites/hello/hello.conf /etc/nginx/sites-enabled/hello
/etc/init.d/nginx reload

cat /etc/nginx/sites-enabled/hello

curl hello.localhost
curl hello.ihateiceforfree.com





# Letsencrypt
sudo snap install --classic certbot

I split this up into the initial cert using webroot as the challenge and then just running certbot and using the reinstall on the cert just generated.

sudo certbot certonly --webroot --webroot-path ~/python-misc/static-sites/hello/static-html-directory/ --domains hello.ihateiceforfree.com

sudo certbot

choose hello.ihateiceforfree.com

Successfully deployed certificate for hello.ihateiceforfree.com to /etc/nginx/sites-enabled/hello
Congratulations! You have successfully enabled HTTPS on https://hello.ihateiceforfree.com