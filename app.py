from flask import Flask, request

app=Flask(__name__)

@app.route("/welcome")
def welcome_page():
    return "welcome"

# @app.route("/welcome/home")
# def welcome_home():
#     return "welcome home"

# @app.route("/welcome/back")
# def welcome_back():
#     return "welcome back"

@app.route("/welcome/<place>")
def welcome_to_page(place):
    return f"welcome {place}"


@app.route("/math")
def calculate():
    operation=request.args["operation"]
    a=request.args["a"]
    b=request.args["b"]
    num_one=int(a)
    num_two=int(b)
    if operation == "add":
        return str(num_one+num_two)
    if operation == "sub":
        return str(num_one-num_two)
    if operation == "mult":
        return str(num_one*num_two)
    if operation == "div":
        return str(num_one/num_two)  
