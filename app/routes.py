from flask import render_template, redirect, flash
from app import app
from app.forms import ArtistForm



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
