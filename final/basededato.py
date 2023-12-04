from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow



main = Flask(__name__)


main.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/adso22'
main.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db = SQLAlchemy(main)

ma = Marshmallow(main)
