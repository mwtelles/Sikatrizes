from flask import Flask 
import os
from application.model.dao.video_dao import videoDao
from application.model.dao.category_dao import categoryDao
from application.model.dao.comment_dao import commentDao

template_folder = os.path.abspath("application/view/templates")
static_folder = os.path.abspath("application/view/static")


app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)

videos = videoDao ()
categories = categoryDao ()
comments = commentDao ()

app.config['comments'] = comments
app.config['videos'] = videos
app.config['categories'] = categories

from application.controller import index_controller
from application.controller import category_controller
from application.controller import video_controller