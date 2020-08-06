from flask import render_template, flash, redirect, url_for
from app.forms import CommentForm
from app.models import Comment
from app import app, db

@app.route('/')
@app.route('/index')
def index():
    cm = Comment.query.all()
    return render_template('index.html', title='Home', cm = cm)

@app.route('/showreviews')
def showreviews():
    cm = Comment.query.all()
    return render_template('showreviews.html', title="Reviews", cm=cm)

@app.route('/leaveComment', methods=['GET', 'POST'])
def leaveComment():
    form = CommentForm()
    if form.validate_on_submit():
        flash('Your comment "{}" has been added successfully!'.format(
        form.body.data))

        c = Comment(firstname=form.firstname.data, lastname=form.lastname.data, body=form.body.data)
        db.session.add(c)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('leaveComment.html', title='Home', form = form)

@app.route('/schulmedizin')
def schulmedizin():
    return render_template('schulmedizin.html', title="Schulmedizin")

@app.route('/akupunktur')
def akupunktur():
    return render_template('akupunktur.html', title="Akupunktur")

@app.route('/homoeopathie')
def homoeopathie():
    return render_template('homoeopathie.html', title="Homoeopathie")

@app.route('/ernaehrung')
def ernaehrung():
    return render_template('ernaehrung.html', title="Ernaehrung")

@app.route('/mikrobiologie')
def mikrobiologie():
    return render_template('mikrobiologie.html', title="Mikrobiologie")

@app.route('/weitere')
def weitere():
    return render_template('weitere.html', title="Weitere Methoden")
