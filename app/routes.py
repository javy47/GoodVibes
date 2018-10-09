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

        artists = [
        {
            'musician': 'John Lenin',
            # 'page': '/index'
        },
        {
             'musician':  'Drake',
             # 'page': '/artistpage'
        }
        ,
        {
            'musician': 'Eminem',
            # 'page': '/artistpage'
        }
        ]
        return render_template('artist_list.html', artists=artists)

@app.route('/drake')
def artist():

    artists = {"name": "Drake",
               "bio": "The multi-Grammy-award-winning rapper Drake has had two shots at fame — and nailed them both."
                        " He first came to prominence in the teen soap Degrassi: "
                        "The Next Generation in the role of Jimmy Brooks"
                        ", a wheelchair-bound character he played for seven years. After leaving the show he became one of"
                        " the biggest rappers on the planet after signing a deal with Lil Wayne's label Young "
                        "Money Entertainment. He is rarely out of the headlines,"
                        " whether it’s for dating Rihanna or Jennifer"
                        " Lopez, founding his own label, OVO Sound, or fronting the NBA’s Toronto Raptors as the team's"
                        " global ambassador. It's no surprise that Jay Z labeled him as the Kobe Bryant of hip hop." ,
               "hometown": "Toronto, Canada" ,
               "event1": "Washington, DC 07:00 PM Aubrey & The Three Migos Tour",
               "event2": "Nashville, TN 07:00 PM Aubrey & The Three Migos Tour",
               "event3": "Philadelphia, PA 07:00 PM Aubrey & The Three Migos Tour"


                }
    return render_template('drake.html', artists=artists)


@app.route('/create_artist', methods=['GET', 'POST'])
def create_artist():

    form = ArtistForm()

    if form.validate_on_submit():
        flash('Login requested for user {}'.format(
            form.artist.data))
        artists = {
            "name": form.artist.data,
            "bio": form.bio.data,
            "hometown": form.hometown.data}
        return render_template('drake.html',form=form, artists=artists)
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

   db.session.add_all(artist1, artist2, artist3, venue1, venue2, venue3, event1, event2, a2e, a2e1)
   db.session.commit()

   return redirect(url_for('index'))
