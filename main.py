from flask import Flask,render_template,request
from model import save_user_credentials,check_user_existence,show_color

app = Flask(__name__)
@app.route('/',methods = ['GET', 'POST'])
def hello(name=None):
    '''if Get method then move too this request'''
    if request.method == "GET":
        print("getting")
        return render_template('index.html')
    else:
        print("posting")
        username = request.form.get('usr')
        password = request.form.get('pass')
        print("credentials", username, password)
        # check for seeing if this already exist
        check = check_user_existence(username)

        if check:
            color = show_color(username)
            return render_template('index.html',message=f"Already exists, fav color is {color}")
        else:
            save_user_credentials(username, password)
            return render_template('index.html',message=f"User credentials saved successfully! {username}")

@app.route('/login') 
def apple():
    return render_template('index2.html',hehe="huhuhu")


if __name__ == '__main__':
    app.run(debug=True)
