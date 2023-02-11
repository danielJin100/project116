# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Daniel Jin"
    age = "14"

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage

@app.route('/father')
def Father():
    name = 'Ming'
    age = "51"
    return render_template('father.html' , name = name , age = age)

# define the route to mother webpage
@app.route('/mother')
def Mother():
    name = 'Yi'
    age = "46"
    return render_template('mother.html' , name = name , age = age)

# define the route to friends webpage
@app.route('/friends')
def Friends():
    return render_template('friend.html')
# add other routes, if you want
@app.route('/messy')
def Hello():
    name = 'Messy!'
    age = "NaN + 14"
    return render_template('messy.html' , name = name , age = age)



# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
