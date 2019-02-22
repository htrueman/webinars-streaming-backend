import subprocess

import requests
from flask import Flask, request, Response

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/file_stream/<filename>', methods=['GET'])
def file_stream(filename):
    command = 'ffmpeg -re -i /var/video-records/{filename}.flv ' \
              '-acodec copy -vcodec copy -f flv rtmp://nginx:1935/stream/{filename}'\
        .format(filename=filename)
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    print(output, error)
    return Response(status=201)


@app.route('/stream-action/<action>', methods=['POST'])
def stream_action(action):
    bad_response = Response(status=400)
    response = Response(status=201)
    user_id = request.form.get('user_id')

    if action == 'on_publish':
        r = requests.post('http://django:8000/check-publish-stream-allowed',
                          data={'user_id': user_id})
        if r.status_code != 200:
            return bad_response
    elif action == 'on_publish_done':
        return bad_response
    elif action == 'on_play':
        r = requests.post('http://django:8000/check-play-stream-allowed',
                          data={'user_id': user_id})
        if r.status_code != 200:
            return bad_response

    return response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
