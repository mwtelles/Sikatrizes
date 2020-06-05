from flask import current_app

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
        for i, comment in enumerate(comments.getCommentList()):
            if comment.getVideo_Id() == id_video:
                comments_video.append(comment)
        return comments_video
    
    def delete_comment_by_id(self, comment_id):
        commentary = current_app.config['comments']
        for i, comment in enumerate(commentary.getCommentList()):
            if comment.getId() == comment_id:
                self._commentList.pop(i)
                return comment
        return None