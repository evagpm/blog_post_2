'''
At the command line: 
conda activate PIC16B
export FLASK_ENV=development; flask run

'''

from flask import Flask, render_template, g, request
import sqlite3

app = Flask(__name__)

#Show base page with links to submit and view
@app.route("/")
def main():
    return render_template("basic.html")

#Establish submit page
@app.route("/submit", methods=['POST', 'GET'])
def submit():
    if request.method == 'GET' :
        return render_template("submit.html")
    else:
        insert_message(request)
        return render_template("submit.html", done = True)

#Function retrieves or creates the connection
def get_message_db():
    #Checks if message_db exists in g
    try:
        g.message_db

    #If it doesn't, it creates it
    except AttributeError:
        g.message_db = sqlite3.connect("messages_db.sqlite")
        cursor = g.message_db.cursor()

        #Also creates a messages table, if needed
        cmd = """
            CREATE TABLE IF NOT EXISTS messages (
            id int,
            handle varchar(50),
            message varchar(200))
            """
        cursor.execute(cmd)

    #Returns that connection
    return g.message_db

#Function inserts the message into the table
def insert_message(request):
    #Get inputs from form
    message = request.form['message']
    handle = request.form['handle']

    #Use function to get cursor
    cursor = get_message_db().cursor()

    #Count the number of rows in messages
    cursor.execute("SELECT COUNT(*) FROM messages")
    nrows = cursor.fetchall()[0][0]

    #Add row for new message
    cmd = "INSERT INTO messages VALUES ("
    cmd += str(nrows + 1) + ", \"" + handle + "\", \"" + message + "\")"
    cursor.execute(cmd)
    get_message_db().commit() #Commit changes so they save
    get_message_db().close() #Always close connection when done

#Establish view page
@app.route("/view")
def view():
    rows = random_messages(6)
    return render_template('view.html', rows = rows)

#Function returns a list of rows of messages from the table
def random_messages(n):
    #Use function to get cursor
    cursor = get_message_db().cursor()

    #Extract n random rows
    cmd = "SELECT * FROM messages ORDER BY RANDOM() LIMIT "+ str(n) + ";"
    cursor.execute(cmd)
    rows = cursor.fetchall()
    get_message_db().close() #Always close connection when done

    return rows