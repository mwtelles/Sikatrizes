class Comment:
    def __init__(self, text, video_id):
        self._text = text
        self._video_id = video_id

    def setText(self, text):
        self._text = text
    
    def getText(self):
        return self._text

    def getVideo_Id(self):
        return self._video_id