import pydub
from pydub import AudioSegment
from flask import Flask, render_template, request

app = Flask(__name__)

pydub.AudioSegment.converter = "ffmpeg-4.0.2/bin/ffmpeg.exe"
song = AudioSegment.from_mp3(r"static/file/METAMORPHOSIS.mp3")


def change_volume(data):
    output = 0
    if int(data) < 50:
        output = (int(data) - 50) // 2
    elif int(data) > 50:
        output = (int(data) - 50) // 2
    return output


def speed_up(sound, speed):
    print(int(speed))
    if (int(speed) < 50) and (speed != 1.0):
        speed = 1.0 - (int(speed)) / 100
        print(1)
    elif (int(speed) > 50) and (speed != 1.0):
        speed = 1.0 + (int(speed)) / 100
        print(2)
    elif int(speed) == 50:
        speed = 1.0
        print(3)
    print(speed)
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * speed)
    })
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)


@app.route('/')
@app.route('/index')
def index():
    volume = request.args.get('set_audio_volume_value')
    speed = request.args.get('set_audio_speed_value')
    print(volume)
    print(speed)
    if volume is None:
        volume = 50

    if speed is None:
        speed = 1.0

    louder_song = song + change_volume(volume)
    print(speed)
    louder_song = speed_up(louder_song, speed)

    louder_song.export("static/file/louder_song.mp3")
    print('True')

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
