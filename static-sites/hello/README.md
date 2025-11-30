
Image is tagged -t as  static-sites-hello. Container runs in background 
```
docker build . -t static-sites-hello
docker stop static-sites-hello
docker run --name=static-sites-hello -p 8080:80 -v ./static-html-directory:/usr/share/nginx/html:ro -d static-sites-hello

docker run --name=static-sites-hello -p 8080:80 -v /root/python-misc/static-sites/hello/static-html-directory:/usr/share/nginx/html:ro -d static-sites-hello

docker run --name=static-sites-hello -p 8080:80 -d static-sites-hello
```

docker ps


curl localhost:8080


# Nginx 80 setup
Must be accessible on port 80 first hello.ihateiceforfree.com.

Then redirect.

cat /etc/

ln -s /root/python-misc/static-sites/hello/hello.conf /etc/nginx/sites-available/hello

ln -s /root/python-misc/static-sites/hello/hello.conf /etc/nginx/sites-enabled/hello

cat /etc/nginx/sites-enabled/hello


/etc/init.d/nginx reload

curl hello.localhost

curl hello.ihateiceforfree.com





# Letsencrypt standalone
sudo certbot certonly --webroot --webroot-path ~/python-misc/static-sites/hello/static-html-directory/ --domains hello.ihateiceforfree.com




testroot@vak-wordpress-2:~/python-misc/static-sites/hello# sudo certbot certonly --webroot
Saving debug log to /var/log/letsencrypt/letsencrypt.log
Please enter the domain name(s) you would like on your certificate (comma and/or
space separated) (Enter 'c' to cancel): 