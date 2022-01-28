'''
In this example, we are going to look at creating, serving, and deploying a *very simple* webapp. In the following several lecture, we'll see how to add some interesting interactivity to our app. 

# Prerequisites

- You need to have the flask package installed in your PIC16B Anaconda environment. 
- You need a Heroku account.
- You need the Heroku command line interface: 
    - To install, at the command line (for MacOS)
    brew tap heroku/brew && brew install heroku

- At the command line, run 
    conda activate PIC16B

# Local Preview

At the command line: 
conda activate PIC16B
export FLASK_ENV=development; flask run

# Deployment

*Note*: these notes are written for the version of the app that Phil is using, which is indeed called pic16b-minimal-demo. In order to make your own version, you would need to give the app a different name (because one with this name already exists on the internet now).

Sign up for Heroku, create app called pic16b-minimal-demo

```
heroku login
heroku git:remote -a pic16b-minimal-demo

git add *.
git commit -m'add files for heroku'
git push heroku
```

Then, the website is at 
https://pic16b-minimal-demo.herokuapp.com

    
# Sources

This set of lecture notes is based in part on previous materials developed by [Erin George](https://www.math.ucla.edu/~egeo/) (UCLA Mathematics) and the tutorial [here](https://stackabuse.com/deploying-a-flask-application-to-heroku/). 
'''

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    #return "seeing if I can change it!"
    return render_template("base.html")


'''
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
# simplest possible approach
def main():
    return "hi there!"

# slightly less trivial
def main():
     return render_template("main.html")

# A little fancier

# @app.route("/")
#def main():
#    return render_template("main_better.html")

# getting basic user data
@app.route('/ask/', methods=['POST', 'GET'])
def ask():
    if request.method == 'GET':
        return render_template('ask.html')
    else:
        try:
            return render_template('ask.html', name=request.form['name'], student=request.form['student'])
        except:
            return render_template('ask.html')

# 
@app.route('/profile/<name>/')
def hello_name(name):
    return render_template('profile.html', name=name)
'''