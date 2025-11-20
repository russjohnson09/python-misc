
# WSL
[Get WSL Ubuntu installed and opened up.](https://stackoverflow.com/questions/32378494/how-to-run-airflow-on-windows)

curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env
uv --version
uv 0.9.10


uv add apache-airflow
uv add apache-airflow[celery]

rm -rf .venv
uv sync
uv run airflow config list --defaults > "airflow.cfg"

AIRFLOW_HOME=. uv run airflow standalone

password will be visible in the output
Simple auth manager | Password for user 'admin': nPvqKKUgahWfYcFD
airflow\simple_auth_manager_passwords.json.generated
It will also be available here.





Verify it comes with python 3.6.5 or so (python3 -version).

https://stackoverflow.com/questions/32378494/how-to-run-airflow-on-windows
https://coding-stream-of-consciousness.com/2018/11/06/apache-airflow-windows-10-install-ubuntu/


https://airflow.apache.org/docs/apache-airflow/stable/start.html





ModuleNotFoundError: No module named 'fcntl'
https://stackoverflow.com/questions/45228395/error-no-module-named-fcntl







Run pip install apache-airflow[EXTRAS]==AIRFLOW_VERSION --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-AIRFLOW_VERSION/constraints-PYTHON_VERSION.txt", for example pip install "apache-airflow[celery]==3.0.0" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-3.0.0/constraints-3.10.txt



https://airflow.apache.org/docs/apache-airflow/stable/start.html





```
docker compose up


uv airflow ...
```


https://yesidays.medium.com/setting-up-apache-airflow-postgresql-with-docker-compose-2674a4d28055


https://airflow.apache.org/docs/docker-stack/index.html


https://airflow.apache.org/docs/apache-airflow-ctl/stable/index.html


# Airflow Ctl
https://airflow.apache.org/docs/apache-airflow-ctl/stable/start.html


Using this instead of the web server?

Does the scheduler have a rest api?

Or is it the webserver interacting with the scheduler or something else?

