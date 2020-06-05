from application import app
from flask import render_template, current_app
from application.model.entity.video import Video



@app.route ("/")
def index():
    videos = current_app.config['videos']
    videora = videos.get_moreLiked()
    category_list = current_app.config['categories'].getCategories()
    return render_template("index.html", category_list = category_list, videora = videora)

