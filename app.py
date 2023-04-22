import FakeHits
from flask import Flask, render_template , request


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        fakepassword = request.form.get('Fake')
        webhook = request.form.get('Webhook')
        id = request.form.get('Roblox')
        v = FakeHits.Main(webhook,id,fakepassword)
        b = v.__repr__
        print(b)
    return render_template('build/index.html')


if __name__ == '__main__':
    app.run(debug=True)