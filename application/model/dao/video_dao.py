from application.model.entity.video import Video

class videoDao:
    def __init__(self):

        self._video_list = []
        self._video_list.append(Video(1, "AstroWorld", "Descricao AstroWorld", "/static/assets/images/thumbs/n.jpg", "/static/assets/videos/astroworld.mp4", 1))
        self._video_list.append(Video(2, "Culture", "Descricao Culture", "/static/assets/images/thumbs/n.jpg", "/static/assets/videos/culture.mp4", 2))
        self._video_list.append(Video(3, "Amaterasu", "Descricao Amaterasu", "/static/assets/images/thumbs/i.jpg", "/static/assets/videos/amaterasu.mp4", 2))
        self._video_list.append(Video(4, "K11", "Descricao K11", "/static/assets/images/thumbs/a.jpg", "/static/assets/videos/k11.mp4", 1))
        self._video_list.append(Video(5, "Reaper Death", "Descricao Reaper Death", "/static/assets/images/thumbs/k.jpg", "/static/assets/videos/reaper-death.mp4", 2))
        self._video_list.append(Video(6, "CrowdControl", "Descricao Crowd Control", "/static/assets/images/thumbs/c.jpg", "/static/assets/videos/crowd-control.mp4", 3))
        self._video_list.append(Video(7, "Samurai", "Descricao Samurai", "/static/assets/images/thumbs/s.jpg", "/static/assets/videos/samurai.mp4", 3))

    def get_video_list(self):
        return self._video_list

    def get_video_by_id (self, video_id):
        find_video = None
        for i, video in enumerate (self.get_video_list()):
            if video.getId() == int(video_id):
                find_video = video
        return find_video