export cf_env="dev"
echo $cf_env
pkill gunicorn
cd /home/namita/flask_workspace/python-microservices/central_service
pip install -r requirements.txt
echo $PWD
gunicorn -c conf/gunicorn.py --bind unix:/tmp/gunicorn.sock --reload wsgi & disown
sudo service nginx restart