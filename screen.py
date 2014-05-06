import pyscreenshot
import flask
from StringIO import StringIO

app = flask.Flask(__name__)


@app.route('/screen.png')
def serve_pil_image():
    img_buffer = StringIO()
    pyscreenshot.grab().save(img_buffer, 'PNG', quality=50)
    img_buffer.seek(0)
    return flask.send_file(img_buffer, mimetype='image/png')


@app.route('/')
def serve_img():
    return flask.render_template('screen.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
