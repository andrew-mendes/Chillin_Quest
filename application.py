import re, string, base64, datetime

from cs50 import SQL

from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp

from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename

from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import SubmitField

from helpers import allowed_file, login_required, error


# Configure application
app = Flask(__name__)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///chillinquest.db")

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    if request.path.startswith('/static/background.jpg'):
        response.headers["Cache-Control"] = "public, max-age=525600"
        response.headers["Expires"] = 525600
    else:
        response.headers["Cache-Control"] = "no-cache"
        response.headers["Pragma"] = "no-cache"
    
    return response    

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
# Configures secret key
app.config["SECRET_KEY"] = "secret"
Session(app)


@app.route("/", methods=["GET", "POST"])
@app.route("/quests/<status>", methods=["GET", "POST"])
@login_required
def index(status="all", searchterm=""):

    # Identify user
    user_id = session["user_id"]

    """Show Profile Card"""
    user_data = db.execute("SELECT pic, name, title FROM users WHERE id = ?", user_id)[0]
    name = user_data['name']
    title = user_data['title']
    avatar_img=user_data['pic']

    """Show Quest Totals"""
    oquests = db.execute("SELECT COUNT (id) FROM quests WHERE user_id = ? AND done = ?", user_id, False)[0]['COUNT (id)']
    cquests = db.execute("SELECT COUNT (id) FROM quests WHERE user_id= ? AND done = ?", user_id, True)[0]['COUNT (id)']
    totalquests = cquests + oquests

    """Show list of quests"""
    quests = db.execute("SELECT * FROM quests WHERE user_id = ?", user_id)

    # Obtain user's new quest inputs
    if request.method == "POST":
        quest = request.form.get("quest-name")
        description = request.form.get("quest-text")
        reward = request.form.get("quest-prize")
        done = False

        # Limit quest titles lenght
        if len(quest) > 25:
            return error("That's too long for a name.\nIt will not fit. Sorry friend.\nMax 25 characters")

        else:
            # Insert new quest into DB
            db.execute("INSERT INTO quests (title, description, reward, user_id, done) VALUES (?, ?, ?, ?, ?)", quest, description, reward, user_id, done)
            return redirect("/")

    else:
        return render_template("index.html", quests=quests, name=name, title=title, avatar_img=avatar_img, status=status, oquests=oquests, cquests=cquests, totalquests=totalquests)


@app.route("/account", methods=["GET", "POST"])
@login_required
def password_change():
    """Changes user's password"""

    # Identify user
    user_id = session["user_id"]
    token = db.execute("SELECT hash FROM users WHERE id = ?", user_id)
    change = False
    form = UploadForm()

    # Handles password change forms submission
    if request.method == "POST":
        new_password = request.form.get("new_password")
        confirmation = request.form.get("confirmation")

        # Ensure new password was submitted
        if not new_password:
            return error("Can you tell me the new password you want, friend?")
        # Ensure confirmation was submitted
        elif not confirmation:
            return error("Didn't hear that right, friend.\nCan you repeat that password again, twice in a row?\nNo mistakes!")
        # Ensure confirmation matches
        elif new_password != confirmation:
            return error("Hey, can you say that new password twice in a row?\nNo mistakes.")
        # Ensure new password is different
        elif check_password_hash(token[0]['hash'], new_password):
            return error("Wanna change or not, friend?\nYour new password is the same.")
        # Change the password
        else:
            hash = generate_password_hash(new_password)
            db.execute("UPDATE users SET hash = ? WHERE id = ?", hash, user_id)

            # Prepare confirmation of change
            change = True

            # Ensure user information is properly loaded on the page
            user_data = db.execute("SELECT pic, name, title FROM users WHERE id = ?", user_id)[0]
            return render_template("account.html", change=change, form=form, nickname=user_data['name'], title=user_data['title'], avatar_img=user_data['pic'])

    # User reached route via GET (as by clicking a link or via redirect)
    else:

        # Ensure user information is properly loaded on the page
        user_data = db.execute("SELECT pic, name, title FROM users WHERE id = ?", user_id)[0]
        return render_template("account.html", form=form, nickname=user_data['name'], title=user_data['title'], avatar_img=user_data['pic'])


@app.route("/done/<quest_id>", methods=["POST"])
@login_required
def done(quest_id=None):
    """Toggle user's quests done status"""

    # Identify user
    user_id = session["user_id"]

    # Obtain user quest of choice
    if request.method == "POST":
        quest_done = db.execute("SELECT done FROM quests WHERE id = ? AND user_id = ?", quest_id, user_id)[0]["done"]

        if quest_done == True:
            db.execute("UPDATE quests SET (done, timestamp) = (?, ?) WHERE id = ? AND user_id = ?", False, None, quest_id, user_id)

        else:
            db.execute("UPDATE quests SET (done, timestamp) = (?, ?) WHERE id = ? AND user_id = ?", True, datetime.datetime.now(), quest_id, user_id)

        return redirect("/")

    else:
        return error("Something wrong is not right, traveller.\nWhat've you been meddling with?")


@app.route("/delete/<quest_id>", methods=["GET", "POST"])
@login_required
def delete(quest_id=None):
    """Delete user's quests"""

    # Identify user
    user_id = session["user_id"]

    # Obtain user quest of choice
    if request.method == "POST":

        db.execute("DELETE FROM quests WHERE id = ? AND user_id = ?", quest_id, user_id)

        return redirect('/')

    else:
        return redirect('/')


@app.route("/editquest/<quest_id>", methods=["POST","GET"])
@login_required
def edit(quest_id=None):
    """Edit user's quests"""

    # Identify user
    user_id = session["user_id"]

    # Obtain user quest of choice
    if request.method == "GET":
        questinfo = db.execute("SELECT id, title, description, reward FROM quests WHERE id = ? AND user_id = ?", quest_id, user_id)[0]

        return render_template("editquest.html", questinfo=questinfo)

    # Update quest information
    elif request.method == "POST":

        quest_title = request.form.get("quest-edit-name")
        quest_description = request.form.get("quest-edit-text")
        quest_reward = request.form.get("quest-edit-prize")

        db.execute("UPDATE quests SET (title, description, reward) = (?, ?, ?) WHERE id = ? AND user_id = ?", quest_title, quest_description, quest_reward, quest_id, user_id)

        return redirect("/")


@app.route("/farewell", methods=["POST"])
@login_required
def farewell():
    """Delete account and all user information"""

    change = True

    # Identify user
    user_id = session["user_id"]

    confirmation = request.form.get("deleteconfirm")

    if confirmation == "DELETE":

        # Burn it all
        db.execute("DELETE FROM quests WHERE user_id = ?", user_id)
        db.execute("DELETE FROM users WHERE id = ?", user_id)

        # Forget any user_id
        session.clear()

        return render_template("login.html", change=change)

    else:

        return error("You didn't really say DELETE.\nCan't do, friend.")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return error("No introductions?\nWhat's your username, adventurer?")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return error("Tell me the password to the club, would ya?")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return error("Something wrong with that name or password of yours, traveller.\nAre you really from around?")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return render_template("login.html")

@app.route("/picture", methods=["POST"])
@login_required
def picture():
    """Upload user profile picture"""

    # Identify user
    user_id = session["user_id"]
    # Define form
    form = UploadForm()

    if request.method == "POST":

        if form.validate_on_submit():

            if form.file.data and allowed_file(secure_filename(form.file.data.filename)):

                picture = form.file.data.read()
                avatar_img = base64.b64encode(picture).decode(encoding='utf-8')

                change = True

                db.execute("UPDATE users SET pic = ? WHERE id = ?", avatar_img, user_id)

                # Ensure user information is properly loaded on the page
                user_data = db.execute("SELECT pic, name, title FROM users WHERE id = ?", user_id)[0]
                return render_template("account.html", form=form, change=change, nickname=user_data['name'], title=user_data['title'], avatar_img=user_data['pic'])

            else:

                return error("Is that a picture?\nCan't see ya!")

    else:
        return redirect("/account")

class UploadForm(FlaskForm):
    file = FileField()
    submit = SubmitField("Submit picture")


@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    """Change user profile information"""

    # Identify user
    user_id = session["user_id"]
    change = False

    nickname = request.form.get("nickname")
    usertitle = request.form.get("usertitle")

    # Handles user profile information update submission
    if request.method == "POST":

        # Create a regex pattern to match all special characters in string
        pattern = r'[' + string.punctuation + ']'
        # Remove special characters from the string
        nickname = re.sub(pattern, '', nickname)
        usertitle = re.sub(pattern, '', usertitle)

        # Verification
        if int(len(nickname)) > 25:
            return error("Name is too long; Didn't read.\n(max 25 characters)")

        if int(len(usertitle)) > 50:
            return error("Title is too long; Didn't read.\n(max 50 characters)")

        else:
            db.execute("UPDATE users SET (name, title) = (?, ?) WHERE id = ?", nickname, usertitle, user_id)


            # Prepare confirmation of change
            change = True
            form = UploadForm()

            # return render_template("account.html", form=form, avatar_img=avatar_img)
            user_data = db.execute("SELECT pic, name, title FROM users WHERE id = ?", user_id)[0]

            # Return to account page
            return render_template("account.html", change=change, form=form, nickname=user_data['name'], title=user_data['title'], avatar_img=user_data['pic'])

    # User reached route via GET (as by clicking a link or via redirect)
    else:

        # Ensure user information is properly loaded on the page
        user_data = db.execute("SELECT pic, name, title FROM users WHERE id = ?", user_id)[0]
        return render_template("account.html", nickname=user_data['name'], title=user_data['title'], avatar_img=user_data['pic'])


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Obtain forms input
    if (request.method == "POST"):
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Ensure username input
        if not username:
            return error("No introductions?\nWhat should be your username, adventurer?")
        # Ensure password input
        elif not password:
            return error("Nay passwords,\nnay joining the club.\nGood now?")
        # Ensure password confirmation input
        elif not confirmation:
            return error("Didn't hear that right.\nCan you repeat that password again, twice in a row?\nNo mistakes.")
        # Ensure password and confirmation match
        elif password != confirmation:
            return error("Hey, can you say the same password twice in a row?\nNo mistakes.")

        # Encrypt password
        hash = generate_password_hash(password)

        # Create default avatar
        avatar = open("static/avatarsample.jpg", "rb")
        avatar = avatar.read()
        avatar_img = base64.b64encode(avatar).decode(encoding='utf-8')

        # Create default name and title
        name = "Nameless Adventurer"
        title = "Titleless Adventurer"

        # Create first quest
        path = 'templates/firststeps.txt'
        firstquest = open(path,'r')
        description = firstquest.read()
        quest = 'First steps: Hey, click here!'
        reward = 'Knowledge'
        done = False

        # Register user in the database
        try:
            db.execute("INSERT INTO users (username, hash, name, title, pic) VALUES (?, ?, ?, ?, ?)", username, hash, name, title, avatar_img)

            # Register first quest
            user_id = db.execute("SELECT id FROM users WHERE username = ?", username)
            db.execute("INSERT INTO quests (title, description, reward, user_id, done) VALUES (?, ?, ?, ?, ?)", quest, description, reward, user_id[0]['id'], done)

            # Return user to home page
            return redirect('/')

        # Ensures no user duplicates
        except:
            return error("I'm sure I already know someone else with that same name traveller.\nTry another one, would ya?")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/search", methods=["GET"])
@login_required
def search():
    """Run and render quest searches on homepage"""

    # Identify user
    user_id = session["user_id"]

    """Obtain profile card information"""
    user_data = db.execute("SELECT pic, name, title FROM users WHERE id = ?", user_id)[0]
    name = user_data['name']
    title = user_data['title']
    avatar_img=user_data['pic']

    quests = db.execute("SELECT * FROM quests WHERE user_id = ? AND title LIKE (?) OR description LIKE (?)", user_id, "%" + request.args.get("q") + "%", "%" + request.args.get("q") + "%")

    return render_template("index.html", quests=quests, name=name, title=title, avatar_img=avatar_img, status="all");
