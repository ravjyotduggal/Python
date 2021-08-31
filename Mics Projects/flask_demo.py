from flask import Flask, render_template

app = Flask(__name__)

posts = [

    {
        "author": "Ravjyot",
        "title": "Hello World",
        "post_date": "Aug 2020"
    },
    {
        "author": "Tim",
        "title": "Hey there",
        "post_date": "Sep 2020"
    }

]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


if __name__ == "__main__":
    app.run(debug=True)
