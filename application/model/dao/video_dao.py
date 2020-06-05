from application.model.entity.video import Video
from flask import current_app

class videoDao:
    def __init__(self):

        self._video_list = []
        self._video_list.append(Video(1, "AstroWorld", "For this life I cannot change", "/static/assets/images/thumbs/w.jpg", "/static/assets/videos/astroworld.mp4", 3,"05/06/2020"))
        self._video_list.append(Video(2, "Culture", "Way back when I was trappin' out Toyotas", "/static/assets/images/thumbs/n.jpg", "/static/assets/videos/culture.mp4", 1,"05/06/2020"))
        self._video_list.append(Video(3, "Amaterasu", "A genjutsu of this level doesn't work on me", "/static/assets/images/thumbs/i.jpg", "/static/assets/videos/amaterasu.mp4", 1,"05/06/2020"))
        self._video_list.append(Video(4, "K11", "If u want to join", "/static/assets/images/thumbs/a.jpg", "/static/assets/videos/k11.mp4", 3,"05/06/2020"))
        self._video_list.append(Video(5, "Reaper Death", "Welcome to the chop street", "/static/assets/images/thumbs/k.jpg", "/static/assets/videos/reaper-death.mp4", 2,"05/06/2020"))
        self._video_list.append(Video(6, "CrowdControl", "I’m in the back with a ski mask and I’m roaming the block", "/static/assets/images/thumbs/c.jpg", "/static/assets/videos/crowd-control.mp4", 3,"05/06/2020"))
        self._video_list.append(Video(7, "Samurai", "cabe em meu coração?", "/static/assets/images/thumbs/s.jpg", "/static/assets/videos/samurai.mp4", 3,"05/06/2020"))
        self._video_list.append(Video(8, "VLXYS", "Can we get it how we used", "/static/assets/images/thumbs/m.jpg", "/static/assets/videos/magic-cloth.mp4", 1,"05/06/2020"))

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