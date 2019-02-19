from flask import Flask, request, Response

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/on_publish', methods=['POST'])
def index():
    print(request.form)
    return Response(status=201)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
