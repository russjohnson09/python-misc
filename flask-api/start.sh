

# uv run 

# docker build . -t flask-api
# docker run flask-api
# docker exec -it laughing_shockley sh

# # equivalent to 'from app import app'
# 8000 is the default port
# four workers
uv run gunicorn -b 0.0.0.0 -w 4 'app:app'

# tail -f /dev/null