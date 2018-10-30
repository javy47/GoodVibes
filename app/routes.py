from flask import render_template, redirect, flash, url_for, request
from werkzeug.urls import url_parse
from app import app, db
from app.forms import ArtistForm, LoginForm, RegistrationForm, EventForm, VenueForm
from app.models import Artist, ArtistToEvent, Events, Venues, User
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime



@app.route('/')
@app.route('/index')
def index():

    messages = {
            'about': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
            'Lorem Ipsum has been the industry standard dummy text ever since the 1500s'
            'when an unknown printer took a galley of type and scrambled it to make a type specimen book.'
            'It has survived not only five centuries, but also the leap into electronic typesetting,'
            'remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset'
            'sheets containing Lorem Ipsum passages, and more recently with desktop'
            'publishing software like Aldus PageMaker including versions of Lorem Ipsum'
        }
    return render_template('index.html', messages=messages)


@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.user.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid Username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()

    if form.validate_on_submit():
        user1 = User(username=form.username.data)
        user1.set_password(form.password.data)
        db.session.add(user1)
        db.session.commit()
        flash('Congratulation you have been registered')
        redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/artist_list')
@login_required
def artist_list():

        alist = Artist.query.order_by(Artist.name).all()

        artists = []
        x = 0
        for i in alist:
             artists.append({'musician': alist[x]})
             if x == len(alist):
                 break
             x = x + 1

        return render_template('artist_list.html', artists=artists)

@app.route('/artist/<name>')
@login_required
def artist(name):

    a = Artist.query.filter_by(name=name).first()

    events = []
    for a2e in a.eventA:
        events.append(a2e.event)

    return render_template('artist.html', artist=a, event_list=events)


@app.route('/create_artist', methods=['GET', 'POST'])
@login_required
def create_artist():

    form = ArtistForm()

    if form.validate_on_submit():
        artist1 = Artist(name=form.artist.data, description=form.bio.data)
        db.session.add(artist1)
        db.session.commit()
        flash('Artist {} has been created'.format(artist1))

    return render_template('create_artist.html', form=form)


@app.route('/create_venue', methods=['GET', 'POST'])
@login_required
def create_venue():
    form = VenueForm()

    if form.validate_on_submit():
        venue1 = Venues(location=form.venue.data, date=" ")
        db.session.add(venue1)
        db.session.commit()
        flash('Artist {} has been created'.format(venue1))

    return render_template('create_venue.html', form=form)


@app.route('/create_event', methods=['GET', 'POST'])
@login_required
def create_event():

    form = EventForm()
    form.artistName.choices = [(artist1.id, artist1.name) for artist1 in Artist.query.all()]
    form.venueName.choices = [(venue.id, venue.location) for venue in Venues.query.all()]

    if form.validate_on_submit():

        venue = Venues.query.filter_by(id=form.venueName.data).first()
        names = form.artistName.data
        flash('Venue = {}'.format(venue))

        nameList = []
        for i in range(len(names)):
            nameList.append(names[i])
            flash(' Name List{}'.format(nameList[i]))

        event1 = Events(name=form.eventName.data, price='S400', venue_id=venue.id, event_date=form.eventDate.data)
        db.session.add(event1)
        db.session.commit()
        for a in range(len(nameList)):

            value = nameList[a]
            a2e = ArtistToEvent(Artist_id=value, Event_id=event1.id)
            db.session.add(a2e)


    db.session.commit()
    return render_template('create_event.html', form=form)



@app.route('/reset_db')
@login_required
def reset_db():
   flash("Resetting database: deleting old data and repopulating with dummy data")

   meta = db.metadata
   for table in reversed(meta.sorted_tables):
       print('Clear table {}'.format(table))
       db.session.execute(table.delete())
   db.session.commit()

   artist1 = Artist(name="Drake", description= "Soon to be added")
   artist2 = Artist(name='Kendrick Lamar', description="Added after Drake")

   venue1 = Venues(location='Baltimore Soundstage, Maryland', date='01/24/2018')
   venue2 = Venues(location='The 20th Century Theater, Ohio', date='04/28/2018')
   venue3 = Venues(location='The New Parish, California', date='04/29/2018')
   event1 = Events(name='Aubrey & The Three Migos ', price='$350', venue_id=1, event_date=datetime.utcnow())
   event2 = Events(name='Leeds Festival 2018', price='$170', venue_id=2, event_date=datetime.utcnow())
   a2e = ArtistToEvent(Artist_id=1, Event_id=1)
   a2e1= ArtistToEvent(Artist_id=2, Event_id=2)


   db.session.add(artist1)
   db.session.add(artist2)

   db.session.add(venue1)
   db.session.add(venue2)
   db.session.add(venue3)
   db.session.add(event1)
   db.session.add(event2)
   db.session.add(a2e)
   db.session.add(a2e1)

   db.session.commit()

   return redirect(url_for('index'))
