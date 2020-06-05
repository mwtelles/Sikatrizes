from application import app
from flask import render_template, request, current_app, jsonify
from application.model.dao.category_dao import categoryDao
from application.model.dao.video_dao import videoDao
from application.model.entity.comment import Comment

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
        comments = current_app.config['comments']                                                                   # MODEL COMENTARIOS
        comments.ids_generateds +=1                                                                                 #GERA UM NOVO ID PARA O COMENTARIO
        comment = Comment(comments.ids_generateds,request.args.get('comment'),int(request.args.get('id_video')))    #CRIA COMENTARIO
        comments.addComment(comment)                                                                          #ADICIONA COMENTARIO NO MODEL
        response = {'id':comment.getId(), 'text':comment.getText(), 'video_id': comment.getVideo_Id()} 
        return jsonify(response)
    except Exception as e:
        return str(e)

@app.route("/categories/<int:category_id>/videos/<int:video_id>")
def video(category_id, video_id):
    videos = current_app.config ['videos']
    categories = current_app.config ['categories']
    comments = current_app.config ['comments']

    category = categories.search(category_id)
    videory = videos.get_video_by_id(video_id)
    videory.setViews(videory.getViews()+1)

    return render_template('comment.html', videory = videory, category = category, comments = comments.getCommentList())



    
