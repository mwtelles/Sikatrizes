from application import app
from application.model.dao.category_dao import categoryDao
from application.model.entity.category import Category
from flask import render_template, request
from application.model.dao.video_dao import videoDao
from application.model.entity.video import Video

@app.route ("/categories/<int:category_id>")
def categories(category_id):
    categories_id = categoryDao().search(category_id)
    return_category = categoryDao()
    search_category_list = return_category.getCategories()
    return render_template("categories.html", categories_id = categories_id, search_category_list = search_category_list)
    