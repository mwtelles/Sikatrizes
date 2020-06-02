class Video:
    def __init__(self, id, title, description, thumb, url_video, category_id):
        self._id = id
        self._title = title
        self._description = description
        self._thumb = thumb
        self._url_video = url_video
        self._category_id = category_id
        self._likes = 0
        self._views = 0

    def setId(self, id):
        self._id = id

    def getId(self):
        return self._id

    def setTitle(self, title):
        self._title = title

    def getTitle(self):
        return self._title

    def setDescription(self, description):
        self._description = description

    def getDescription(self):
        return self._description

    def setThumb(self, thumb):
        self._thumb = thumb

    def getThumb(self):
        return self._thumb

    def setUrl_video(self, url_video):
        self._url_video = url_video

    def getUrl_video(self):
        return self._url_video

    def setCategory_id(self, category_id):
        self._category_id = category_id

    def getCategory_id(self):
        return self._category_id

    def setLikes(self, likes):
        self._likes = likes

    def getLikes(self):
        return self._likes

    def setViews(self, views):
        self._views = views

    def getViews(self):
        return self._views


    


     