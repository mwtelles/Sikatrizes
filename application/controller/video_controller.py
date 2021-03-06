from application import app
import json
from flask import render_template, request, current_app, jsonify, Response
from application.model.dao.category_dao import categoryDao
from application.model.dao.video_dao import videoDao
from application.model.entity.comment import Comment

@app.route("/video/search")
def search():
    try:
        text_searched = request.args.get('text').lower()
        videos = current_app.config['videos']
        search = [x.__dict__ for x in videos.get_video_list() if  text_searched in x.getTitle().lower() ]
        return Response(json.dumps(search),  mimetype='application/json') 
    except Exception as e:
        return str(e)

@app.route("/video/like", methods = ["POST"])
def like():
    try:
        videos = current_app.config ['videos']
        video_id = (request.form["video_id"])
        videosa = videos.get_video_by_id(video_id)
        videosa.setLikes(videosa.getLikes()+1)
        return jsonify(countLikes = videosa.getLikes())
    except Exception as e:
        return str(e)

@app.route("/video/comment")
def comment():
    try:
        comments = current_app.config['comments']                                                              
        comments.ids_generateds +=1                                                                                 
        comment = Comment(comments.ids_generateds,request.args.get('comment'),int(request.args.get('id_video')))    
        comments.addComment(comment)                                                                          
        response = {'id':comment.getId(), 'text':comment.getText(), 'video_id': comment.getVideo_Id()} 
        return jsonify(response)
    except Exception as e:
        return str(e)

@app.route("/video/comment/delete/")
def delete():
    try:
        comments = current_app.config['comments']
        delete = comments.delete_comment_by_id(int(request.args.get('id_comment'))) 
        if(delete == None):
            return jsonify(delete)
        return jsonify(True)
    except Exception as e:
        return str(e)

@app.route("/categories/<int:category_id>/videos/<int:video_id>")
def video(category_id, video_id):
    videos = current_app.config ['videos']
    categories = current_app.config ['categories']
    comments = current_app.config ['comments']

    comments = comments.find_comments_by_video_id(video_id) 
    category = categories.search(category_id)
    videory = videos.get_video_by_id(video_id)
    videory.setViews(videory.getViews()+1)

    return render_template('comment.html', videory = videory, category = category, comments = comments)



    
