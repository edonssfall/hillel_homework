from flask import Flask, render_template, request, url_for
from time import strftime
from socket import gethostname, gethostbyname
from random import choice
from string import ascii_lowercase, ascii_uppercase

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/whoami/", methods=['GET', 'POST'])
def hello_world():
    user_agent = request.headers.get('User-Agent')
    remote_name = gethostname()
    remote_ip = gethostbyname(remote_name)
    time_server = strftime("%c")
    return render_template("whoami.html", user_agent=user_agent, remote_ip=remote_ip, remote_name=remote_name, time_server=time_server)
    
@app.route("/source_code/")
def source_code():
    text = list()
    with open("flask application.py", "r") as flask_file:
        flask_file = flask_file.readlines()
        for lines in flask_file:
            text.append(lines)
    return render_template("source_code.html", text=text)

@app.route("/random/", methods=["GET", "POST"])
def rando():
    length = request.values.get("length")
    specials = request.values.get("specials")
    digits = request.values.get("digits")
    if specials == None: specials = "0"
    if digits == None: digits = "0"
    if length == None: length = ""
    if len(length) == 0 or not 0 <= int(length) <= 100:
        warning = str()
        if len(length) == 0 or not 0 <= int(length) <= 100:
            warning += "Length must be from 0 to 100 and you enter:"
            if len(length) == 0:
                warning += " None"
            else:
                warning += request.values.get("length")
        return render_template("warning_random.html", warning=warning)

    else:
        chars_list = ascii_lowercase + ascii_uppercase
        specials_list = "!№;%:?*()_+"
        digits_list = "0123456789"
        if specials == "1":
            chars_list += specials_list
        if digits == "1":
            chars_list += digits_list
        output_random = str()
        for _ in range(int(length)):
            output_random += choice(chars_list)
        return render_template("random.html", output_random=output_random)
                
if __name__ == "__main__":
    app.run(debug=True)

