# Installing python and uv
[./uv.md](./uv.md)



https://cloud.digitalocean.com/networking/domains/voiceartistkay.com?i=a539de

https://flask-api.ihateiceforfree.com/




# Versioning
For private repos just using uv.lock files to ensure the resolved git hash doesn't change and just pointing to the default branch is fine.



https://packaging.python.org/en/latest/key_projects/#devpi

https://github.com/chriskuehl/dumb-pypi


dumb-pypi or https://github.com/astariul/github-hosted-pypi?tab=readme-ov-file might be a good way to handle a self-hosted PyPi index.



https://docs.astral.sh/uv/concepts/projects/dependencies/#index


uv add torch --index pytorch=https://download.pytorch.org/whl/cpu




# Galaga

```
cd pygame/galaga
ALLOW_AUTOFIRE=1 uv run pytest ./tests/test_starry_night_and_player.py 
```



# Starry Night
```
cd pygame/galaga
uv run pytest ./tests/test_starry_night.py -s
```


# Platforming
lib-sprites\tests\test_read_png_and_megaman.py

I want to take a basic black and white image, and apply some tileset to it.

# Youtube download
```
cd pygame/galaga
uv run ./tests/youtube_download.py
```

# TODO

## I filled the room with spiders.
Random words of encouragement but 1/1000 chance to say "I filled the room with spiders"
https://youtu.be/7s7Ld0XUbVQ?si=pVx6imcaLjsIS_0z&t=1873


## pytube
https://github.com/yt-dlp/yt-dlp

https://github.com/pytube/pytube

pygame\galaga\tests\misc.py


https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#differences-in-default-behavior


python -m pip install -U --pre "yt-dlp[default]"
