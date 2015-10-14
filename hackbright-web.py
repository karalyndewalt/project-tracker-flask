from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github','jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    html = render_template("student_info.html",first=first,last=last,github=github)
    return html

@app.route("/student_search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/student-add")
def student_adder():
    """add a new student to the database"""
    first_name = request.args.get('first_name','Jane')
    last_name = request.args.get('last_name','Hacks')
    github = request.args.get('github','jhacks')

    #send the information taken from the user to the hackbright.db, 
    # through the function in hb.py -->def make_new_student(first_name, last_name, github)
    #it does not 'need' to be displayed, but you could render a page
    #to show that the correct information was accepted (ah-la skills-flask application)
    # Also, we should not provide a default because that would add Jane to
    #the database over, and over...

    return render_template("student-add.html")

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
