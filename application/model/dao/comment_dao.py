class commentDao:
    def __init__(self):
        self._commentList = []
        self.ids_generateds = 1

    def getCommentList(self):
        return self._commentList

    def addComment(self, comment):
        self._commentList.append(comment)

    def find_comments_by_video_id(self, id_video):
        comments = current_app.config['comments']
        comments_video = []
        for i, comment in enumerate(comments.get_comments()):
            if comment.get_video_id() == id_video:
                comments_video.append(comment)
        return comments_video
    
    def delete_comment_by_id(self,id_comment):
        comments = current_app.config['comments']
        for i, comment in enumerate(comments.get_comments()):
            if comment.get_id() == id_comment:
                self._comments.pop(i)
                return comment
        return None