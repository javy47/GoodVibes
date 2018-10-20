from flask import render_template, redirect, flash, url_for
from app import app, db
from app.forms import ArtistForm
from app.models import Artist, ArtistToEvent, Events, Venues



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



@app.route('/artist_list')
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
def artist(name):

    aname = Artist.query.filter_by(name=name).first()

    artists = {"name": aname.name,
               "link": "/artist/"+aname.name,
               "bio": aname.description,
               }
    x = ArtistToEvent.query.filter_by(artist=aname).first()

    event = ArtistToEvent.query.filter_by(Artist_id=aname.id).all()

    i = 0
    alist = []
    vlist= []
    event_list = [{"name": alist, "venue": vlist}]
    artist_iden= []

    for placeholder in event:
        artist_iden.append(event[i].id)
        m = Events.query.get(event[i].id)
        n = m.venue
        vlist.append(n)
        alist.append(m)

        event_list = [{"name": alist,
                       "venue": vlist,
                       }]
        if (i+1) == len(event):
            return render_template('artist.html', artists=artists, event_list=event_list)

        i= i +1

    return render_template('artist.html', artists=artists, event_list=event_list)


@app.route('/create_artist', methods=['GET', 'POST'])
def create_artist():

    form = ArtistForm()

    # alist = Artist.query.order_by(Artist.name).all()

    if form.validate_on_submit():
        artist1 = Artist(name=form.artist.data, description=form.bio.data)
        db.session.add(artist1)
        db.session.commit()
        flash('Artist {} has been created'.format(artist1))

    return render_template('create_artist.html', form=form)


@app.route('/reset_db')
def reset_db():
   flash("Resetting database: deleting old data and repopulating with dummy data")

   meta = db.metadata
   for table in reversed(meta.sorted_tables):
       print('Clear table {}'.format(table))
       db.session.execute(table.delete())
   db.session.commit()

   artist1 = Artist(name="Drake", description= "Soon to be added")
   artist2 = Artist(name='Kendrick Lamar', description="Added after Drake")
   artist3 = Artist(name='Bob Marley', description='This one was added after kendrick')
   venue1 = Venues(location='Baltimore Soundstage, Maryland', date='01/24/2018')
   venue2 = Venues(location='The 20th Century Theater, Ohio', date='04/28/2018')
   venue3 = Venues(location='The New Parish, California', date='04/29/2018')
   event1 = Events(name='Aubrey & The Three Migos ', price='$350', venue_id=1)
   event2 = Events(name='Leeds Festival 2018', price='$170', venue_id=2)
   a2e = ArtistToEvent(Artist_id=1, Event_id=1)
   a2e1= ArtistToEvent(Artist_id=2, Event_id=2)

   db.session.add(artist1)
   db.session.add(artist2)
   db.session.add(artist3)
   db.session.add(venue1)
   db.session.add(venue2)
   db.session.add(venue3)
   db.session.add(event1)
   db.session.add(event2)
   db.session.add(a2e)
   db.session.add(a2e1)
   db.session.commit()

   return redirect(url_for('index'))
