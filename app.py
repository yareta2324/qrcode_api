from flask import Flask, request
from common.qrcode import qrcode_stream

app = Flask(__name__)


@app.route('/v1/', methods=['GET', 'POST'])
def index():
    """ Qr code stream data API v1.0.1 """
    url = request.args.get('url').strip()

    if url is not None:
        return qrcode_stream(url=url)
    else:
        return '<h1>URL cannot be empty</h1>'


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=False)
