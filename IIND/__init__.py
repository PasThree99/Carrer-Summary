from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = '1f9b3dbffaaf9eff399efd93'
from IIND import routes
