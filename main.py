import os.path

import pydub.scipy_effects
import pydub
from pydub import AudioSegment
from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect

from data import db_session
from data.sounds import Sound

app = Flask(__name__)
db_session.global_init("db/sounds.sqlite")
pydub.AudioSegment.converter = "ffmpeg-4.0.2/bin/ffmpeg.exe"


def change_volume(data):
    output = 0
    if int(data) < 50:
        output = (int(data) - 50) // 2
    elif int(data) > 50:
        output = (int(data) - 50) // 2
    return output


def speed_up(sound, speed):
    if (int(speed) < 50) and (speed != 1.0):
        speed = 1.0 - (50 - int(speed)) / 100
    elif (int(speed) > 50) and (speed != 1.0):
        speed = 1.0 + (int(speed)) / 100
    elif int(speed) == 50:
        speed = 1.0
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * speed)
    })
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)


def pan_all(vol):
    result = 0
    if int(vol) < 50 and vol != 0:
        result = -((50 - int(vol)) * 2 / 100)
    elif int(vol) > 50 and vol != 0:
        result = (int(vol) - 50) * 2 / 100
    return result


@app.route('/')
@app.route('/index')
def index():
    f = 0
    song = None
    if os.path.isfile('static/file/new.wav'):
        song = AudioSegment.from_mp3(r"static/file/new.wav")
        f = 1
    volume = request.args.get('set_audio_volume_value')
    speed = request.args.get('set_audio_speed_value')
    high_pass = request.args.get('set_audio_high_pass_value')
    low_pass = request.args.get('set_audio_low_pass_value')
    pan = request.args.get('set_audio_pan_value')
    print(volume)
    print(speed)
    if volume is None:
        volume = 50

    if speed is None:
        speed = 1.0

    if high_pass is None:
        high_pass = 0

    if low_pass is None:
        low_pass = 0

    if pan is None:
        pan = 0

    if song is not None:
        louder_song = song + change_volume(volume)
        louder_song = speed_up(louder_song, speed)
        if int(high_pass) > 0:
            louder_song = louder_song.high_pass_filter(int(high_pass) * 10, order=3)
        if int(low_pass) > 0:
            louder_song = louder_song.low_pass_filter(int(low_pass) * 10, order=3)
        louder_song = louder_song.pan(pan_all(pan))

        louder_song.export("static/file/louder_song.mp3")

    return render_template('index.html', new_audio_flag=f)


@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save('static/file/new.wav')
    return redirect(url_for('index'))


@app.route('/library')
def library():
    db_sess = db_session.create_session()
    sounds = db_sess.query(Sound)
    return render_template("library.html", sounds=sounds)


if __name__ == '__main__':
    app.run()
