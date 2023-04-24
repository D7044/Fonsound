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


# функция для изменения громкости
def change_volume(data):
    output = 0
    if int(data) < 50:
        output = (int(data) - 50) // 2
    elif int(data) > 50:
        output = (int(data) - 50) // 2
    return output


# функция для ускорения аудио файла
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


# функция для перемещения звука из левого наушника в правый и наоборот
def pan_all(vol):
    result = 0
    if int(vol) < 50 and vol != 0:
        result = -((50 - int(vol)) * 2 / 100)
    elif int(vol) > 50 and vol != 0:
        result = (int(vol) - 50) * 2 / 100
    return result


# страница со всеми аудио файлами
@app.route('/')
@app.route('/library')
def library():
    db_sess = db_session.create_session()
    sounds = db_sess.query(Sound)
    return render_template("library.html", sounds=sounds)


# страница с аудио файлами категории природа
@app.route('/nature')
def nature():
    db_sess = db_session.create_session()
    sounds = db_sess.query(Sound).filter(Sound.category == 'Природа')
    return render_template("library.html", sounds=sounds)


# страница с аудио файлами категории приборы
@app.route('/instrumentation')
def instrumentation():
    db_sess = db_session.create_session()
    sounds = db_sess.query(Sound).filter(Sound.category == 'Приборы')
    return render_template("library.html", sounds=sounds)


# страница с аудио файлами категории насилие
@app.route('/violence')
def violence():
    db_sess = db_session.create_session()
    sounds = db_sess.query(Sound).filter(Sound.category == 'Насилие')
    return render_template("library.html", sounds=sounds)


# страница с аудио файлами категории видеоигры
@app.route('/video_games')
def video_games():
    db_sess = db_session.create_session()
    sounds = db_sess.query(Sound).filter(Sound.category == 'Видеоигры')
    return render_template("library.html", sounds=sounds)


# страница с аудио файлами категории быт
@app.route('/mode_of_life')
def mode_of_life():
    db_sess = db_session.create_session()
    sounds = db_sess.query(Sound).filter(Sound.category == 'Быт')
    return render_template("library.html", sounds=sounds)


# страница с эквалайзером
@app.route('/equalizer')
def equalizer():
    f = 0
    song = None
    if os.path.isfile('static/file/new.wav'):
        song = AudioSegment.from_mp3(r"static/file/new.wav")
        f = 1
    # получение значений ползунков
    volume = request.args.get('set_audio_volume_value')
    speed = request.args.get('set_audio_speed_value')
    high_pass = request.args.get('set_audio_high_pass_value')
    low_pass = request.args.get('set_audio_low_pass_value')
    pan = request.args.get('set_audio_pan_value')
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

    # сама обработка звука
    if song is not None:
        louder_song = song + change_volume(volume)
        louder_song = speed_up(louder_song, speed)
        if int(high_pass) > 0:
            louder_song = louder_song.high_pass_filter(int(high_pass) * 10, order=3)
        if int(low_pass) > 0:
            louder_song = louder_song.low_pass_filter(int(low_pass) * 10, order=3)
        louder_song = louder_song.pan(pan_all(pan))

        louder_song.export("static/file/louder_song.mp3")
        print('True')

    return render_template('index.html', new_audio_flag=f)


# выбор файла для эквалайзера
@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save('static/file/new.wav')
    return redirect(url_for('equalizer'))


if __name__ == '__main__':
    app.run()
