from application.model.entity.video import Video
from flask import current_app

class videoDao:
    def __init__(self):

        self._video_list = []
        self._video_list.append(Video(1, "AstroWorld", "Descricao AstroWorld", "/static/assets/images/thumbs/w.jpg", "/static/assets/videos/astroworld.mp4", 3,"05/06/2020"))
        self._video_list.append(Video(2, "Culture", "Descricao Culture", "/static/assets/images/thumbs/n.jpg", "/static/assets/videos/culture.mp4", 1,"05/06/2020"))
        self._video_list.append(Video(3, "Amaterasu", "Descricao Amaterasu", "/static/assets/images/thumbs/i.jpg", "/static/assets/videos/amaterasu.mp4", 1,"05/06/2020"))
        self._video_list.append(Video(4, "K11", "Descricao K11", "/static/assets/images/thumbs/a.jpg", "/static/assets/videos/k11.mp4", 3,"05/06/2020"))
        self._video_list.append(Video(5, "Reaper Death", "Descricao Reaper Death", "/static/assets/images/thumbs/k.jpg", "/static/assets/videos/reaper-death.mp4", 2,"05/06/2020"))
        self._video_list.append(Video(6, "CrowdControl", "Descricao Crowd Control", "/static/assets/images/thumbs/c.jpg", "/static/assets/videos/crowd-control.mp4", 3,"05/06/2020"))
        self._video_list.append(Video(7, "Samurai", "Descricao Samurai", "/static/assets/images/thumbs/s.jpg", "/static/assets/videos/samurai.mp4", 3,"05/06/2020"))
        self._video_list.append(Video(8, "VLXYS", "Descricao VLXYS", "/static/assets/images/thumbs/m.jpg", "/static/assets/videos/magic-cloth.mp4", 1,"05/06/2020"))

    def get_video_list(self):
        return self._video_list

    def get_video_by_id (self, video_id):
        find_video = None
        for i, video in enumerate (self.get_video_list()):
            if video.getId() == int(video_id):
                find_video = video
        return find_video

    def get_videos_by_category_id (self, category_id):
        find_videoList = []
        for i, video in enumerate (self.get_video_list()):
            if video.getCategory_id() == category_id:
                find_videoList.append(video)
        return find_videoList
            

    def get_moreLiked (self):
        videos = current_app.config ['videos']
        moreLikedVideo = sorted(videos.get_video_list(), key=lambda i: i.getLikes(), reverse=True)
        return moreLikedVideo