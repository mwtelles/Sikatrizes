from application import app
from application.model.dao.category_dao import categoryDao
from application.model.entity.category import Category
from flask import render_template, request
from application.model.dao.video_dao import videoDao
from application.model.entity.video import Video
from flask import current_app


@app.route ("/categories/<int:category_id>")
def categories(category_id):
    categories_id = categoryDao().search(category_id)
    videos = current_app.config['videos']
    videos_in_category = videos.get_videos_by_category_id(category_id)
    return_category = categoryDao()
    category = return_category.search(category_id)
    search_category_list = return_category.getCategories()
    return render_template("categories.html", category = category, search_category_list = search_category_list, videos_in_category = videos_in_category)
    