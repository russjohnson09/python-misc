https://cloud.digitalocean.com/networking/domains/ihateiceforfree.com?i=a539de

https://cloud.digitalocean.com/droplets/400003442/graphs?i=a539de&period=hour



64.23.182.77


# Add new user ssh
droplet console

root@vak-wordpress-2:~# cat ~/.ssh/authorized_keys 
# Added and Managed by DigitalOcean Droplet Agent (code name: DOTTY)
ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBHw+YLeKyi+B8MJ6SpcHUGEMlGhhQsUS9asnO7Ii9Rze7gK1Yy5L345CRjJQNBWIUFc37kWBiYfckoIgfva7MRA= {"os_user":"root","actor_email":"russjohnson09@gmail.com","expire_at":"2025-11-30T19:20:01Z"}-dotty_ssh



 ssh -i ~/.ssh/id_ed25519 russj@64.23.182.77 -vvv


 ls -al /root/voiceartistkay/


 HTTPS_SETUP_LETSENCRYPT.md


 git@bitbucket.org:russjohnson09/voiceartistkay.git


 https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-20-04



 I'm actually going to just do a docker container and run that instead of doing what I did for voiceartistkay ^^.


# Docker setup

 https://docs.docker.com/engine/install/ubuntu/

 ```
 sudo apt update
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

```
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Signed-By: /etc/apt/keyrings/docker.asc
EOF
```

```
 sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin --fix-missing
```


```
sudo docker run hello-world
```


Add lets encrypt to some generic port.


cat /etc/nginx/sites-enabled/voiceartistkay


sudo certbot certonly --webroot
