from flask import Flask, request, Response

app = Flask(__name__, static_url_path='')
# Check Configuration section for more details
# SESSION_TYPE = 'redis'
# app.config.from_object(__name__)
# Session(app)


@app.route('/', methods=['POST'])
def index():
    print(request.url)
    return Response(status=201)



if __name__ == '__main__':
    # app.secret_key = "Your_secret_string"
    # app.config['SESSION_TYPE'] = 'redis'
    app.run(debug=True, host='0.0.0.0')
