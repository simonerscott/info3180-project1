"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, redirect, url_for, flash, jsonify
# from flask_login import login_user, logout_user, current_user, login_required
from forms import NewUser
from models import UserProfile
import os
from werkzeug.utils import secure_filename
from sqlalchemy.sql import exists
import random  
import time



###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')
    



@app.route("/profile", methods = ["GET", "POST"])
def profile():
    
    file_folder = app.config["UPLOAD_FOLDER"]
    form = NewUser()
    
    if request.method == 'POST' and form.validate_on_submit():
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        username = request.form["username"]
        age = request.form["age"]
        bio = request.form["bio"]
        gender = request.form["gender"]
        date = time.strftime('%Y/%b/%d')
        
        
        while True:
            userid = random.randint(620000000, 629999999) 
            if not db.session.query(exists().where(UserProfile.userid == str(userid))).scalar():
                break
        
        
        file = request.files['file']
        filename = secure_filename(file.filename)
        #os.rename(secure_filename(file.filename), id)
        
        user = UserProfile(str(userid), firstname, lastname, username, age, bio, gender, date, filename)
        db.session.add(user)
        db.session.commit()
            
        file.save(os.path.join(file_folder, filename))
        
        flash("User Added!")
        return redirect(url_for("profile"))
        
        # submiting to the db, validate info(if not ask user to fix errors), submit to the db then upload photo to the upload
    else:
        return "render html template"



@app.route("/profile/<userid>", methods = ["GET", "POST"])
def userProfile(userid):
    # UserProfile.query.filter_by(username = userid).all()
    ##f request.method == "POST":
    ##    return "something"
    ##else:
       ## return "something else"
    user = db.session.query(UserProfile).filter(UserProfile.userid == str(userid)).first()
    if not user:
        flash("Cannot Find User", category = "danger")
    else: 
        if request.headers.get('content-type') == 'application/json' or request.method == 'POST':
            return jsonify(userid = user.userid, username = user.username, image = user.image, gender = user.gender, age = user.age,\
                          created_on = user.created_on)
        return render_template('profile.html', user = user)
    return redirect(url_for('profiles'))
    
    
    
    


@app.route("/profiles", methods = ["GET", "POST"])
##    if request.methos == "POST":
  ##      return render_template('profiles.html', users = db.session.query(UserProfile).query.all() )
  ##  else:
  ##      return "something else"
        
def profiles():
    """View a list of profiles"""
    userlist   = []
    result  = db.session.query(UserProfile).all()
    for user in result:
        userlist.append({"username":user.username,"userid":user.userid})
    if request.headers.get('content-type') == 'application/json' or request.method == 'POST':
        return jsonify(users = userlist)
    return render_template('profiles.html', userlist = userlist)
        
   
   
   
        

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
