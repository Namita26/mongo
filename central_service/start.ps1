$env:FLASK_APP = "app.py"
$env:FLASK_ENV = "development"
$env:cf_env = "development"
python -m flask run