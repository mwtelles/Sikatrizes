from flask import current_app

class Category:
    def __init__(self, id, name, description, thumb):
        self._id = id
        self._name = name
        self._description = description

    def setId(self, id):
        self._id = id

    def getId(self):
        return self._id

    def setName(self, name):
        self._name = name
    
    def getName(self):
        return self._name

    def setDescription(self, description):
        self._description = description

    def getDescription(self):
        return self._description

    def setThumb(self, thumb):
        self._thumb = thumb

    def getThumb(self):
        return self._thumb

    def get_video_category_id (self):
        videos = current_app.config ['videos']
        videos_category = []
        for i, video in enumerate (videos.get_video_list()):
            if video.getCategory_id () == self.getId():
                videos_category.append (video)
        return videos_category