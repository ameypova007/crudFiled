import os
from flask import   redirect, abort, jsonify,request,url_for
from sound import app, db
from sound.models import Song, Podcast, AudioBook

@app.route("/post/new", methods=['GET', 'POST'])
def new_post():
    postdata = request.get_json()
    audio_type = postdata.get("audio_type")
    if audio_type == "song":
        title = postdata.get("title")
        duration = postdata.get("duration")
        song = Song(title=title, duration=duration)
        db.session.add(song)
        db.session.commit()

    if audio_type == "podcast":
        title = postdata.get("name")
        duration = postdata.get("duration")
        participants = postdata.get("participants")
        host = postdata.get("host")
        podcast = Podcast(name=title, duration=duration, participants = participants, host= host )
        db.session.add(podcast)
        db.session.commit()

    if audio_type == "audiobook":
        title = postdata.get("title")
        duration = postdata.get("duration")
        author = postdata.get("author")
        narrator =  postdata.get("narrator")
        audiobook = AudioBook(title=title, duration=duration, author = author, narrator= narrator )
        db.session.add(audiobook)
        db.session.commit()

    flash('Your post has been created!', 'success')
    a = {"created":200}
    return jsonify(a)

@app.route("/<string:get_audio_type>/<int:optional_parameter>")
@app.route("/<string:get_audio_type>")
def route(get_audio_type,optional_parameter=None):
    jsons = {}
    if get_audio_type == "Song":
        if get_audio_type == "Song" and optional_parameter !=None:
            post = Song.query.filter_by(id = int(optional_parameter))
        else:
            post = Song.query.all()
        for i in post:
            jsons[i.id] = {}
            jsons[i.id]["id"] = i.id
            jsons[i.id]["title"] = i.title
            jsons[i.id]["duration"] = i.duration
            jsons[i.id]["uploadedTime"] = i.uploadedTime

    if get_audio_type == "AudioBook":
        if optional_parameter != None:
            post = AudioBook.query.filter_by(id = int(optional_parameter))
        else:
            post = AudioBook.query.all()
            print("printing post",post)
        for i in post:
            jsons[i.id] = {}
            jsons[i.id]["id"] = i.id
            jsons[i.id]["title"] = i.title
            jsons[i.id]["duration"] = i.duration
            jsons[i.id]["uploadedTime"] = i.uploadedTime
            jsons[i.id]["author"] = i.author
    if get_audio_type == "Podcast":
        if get_audio_type == "Podcast" and optional_parameter !=None:
            post = Podcast.query.filter_by(id = int(optional_parameter))
            print("printing post",post)
        else:
            post = Podcast.query.all()
            print("printing post",post)
        for i in post:
            jsons[i.id] = {}
            jsons[i.id]["id"] = i.id
            jsons[i.id]["name"] = i.name
            jsons[i.id]["duration"] = i.duration
            jsons[i.id]["uploadedTime"] = i.uploadedTime
            jsons[i.id]["participants"] = i.participants
            jsons[i.id]["host"] = i.host
    return jsonify(jsons)

@app.route("/<string:audio_type>/<int:post_id>/update", methods=['GET', 'POST'])
def update_post(audio_type,post_id):
    postdata = request.get_json()
    if audio_type == "Song":
        post = Song.query.get_or_404(post_id)
        post.title = postdata.get("title")
        post.duration = postdata.get("duration")
        db.session.commit()

    elif audio_type == "AudioBook":
        post = AudioBook.query.get_or_404(post_id)
        post.title = postdata.get("title")
        post.duration = postdata.get("duration")
        post.author = postdata.get("author")
        post.narrator =  postdata.get("narrator")
        db.session.commit()

    elif audio_type == "Podcast":
        post = Podcast.query.get_or_404(post_id)
        post.name = postdata.get("name")
        post.duration = postdata.get("duration")
        post.participants = postdata.get("participants")
        post.host = postdata.get("host")
        db.session.commit()
        
    a = {"created":200}
    return redirect(url_for('route',get_audio_type = audio_type, optional_parameter = post_id))

@app.route("/<string:audio_type>/<int:post_id>/delete", methods=['POST'])
def delete_post(audio_type, post_id):
    if audio_type == "Song":
        post = Song.query.get_or_404(post_id)
    elif audio_type == "AudioBook":
        post = AudioBook.query.get_or_404(post_id)
    elif audio_type == "Podcast":
        post = Podcast.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('route',get_audio_type = audio_type))