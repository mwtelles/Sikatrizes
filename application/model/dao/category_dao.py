from application.model.entity.category import Category
from application.model.entity.video import Video
from flask import current_app
import logging

class categoryDao:
    def __init__(self):

        self._categories = []
        self._categories.append(Category(1, "Naruto", "Descricao Naruto", "/categories/naruto.png"))
        self._categories.append(Category(2, "Demon Slayer", "Descricao One Piece", "/categories/OnePiece.png"))
        self._categories.append(Category(3, "Outros", "Descricao Outros", "/categories/Outros.png"))
    
    def getCategories(self):
        return self._categories

    def search (self, id):
        category = None
        for index, item in enumerate(self.getCategories()):
            if item.getId() == id:
                category = item
                return category
        return category
