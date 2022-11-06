from flask import Flask, render_template, request, redirect

app = Flask(__name__, template_folder='templates')


class Book():
    title = ''
    author = ''
    genre = ''


temp = list()

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        genre = request.form.get('genre')

        p1 = Book()
        p1.title = title
        p1.author = author
        p1.genre = genre

        temp.append(p1)

    return render_template('index.html', books=temp)


@app.route('/addbook')
def addabook():
    return render_template('addbook.html')


@app.route('/deletebook/<string:title>')
def deleteabook(title):
    for i in temp:
        if i.title == title:
            temp.remove(i)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
