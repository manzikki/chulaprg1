from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return """
<form action="getform" method="post">
    <textarea name="text" rows="20" cols="100"></textarea>
    <br/>
    <input type="submit">
</form>
           """

@app.route('/getform', methods=['POST'])
def getform():
    return 'You entered: {}'.format(request.form['text'])


if __name__ == '__main__':
    app.run()
