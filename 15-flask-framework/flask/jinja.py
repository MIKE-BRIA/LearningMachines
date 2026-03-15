
### Building Url Dynamically
### Jinja 2 Template engine



## Building

from flask import Flask,render_template, request

##WSGI application
app = Flask(__name__)


@app.route('/')
def welcome():
    return '<html><H1>Welcome to a day in my life as someone who is successful</H1></html>'


@app.route('/index')
def index():
    return render_template('index.html',method=['get'])


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        name=request.form['name']
        return f'Hello {name}'
    else:
        return render_template('form.html')



###Variable Rule
@app.route('/success/<int:score>')
def success(score):
    res = ''

    if score >= 50:
        res='PASSED'
    else:
        res = 'FAILED'

    exp = {'score': score,'res':res}

    return render_template('result1.html', results=exp)



if __name__=='__main__':
    app.run(debug=True)
