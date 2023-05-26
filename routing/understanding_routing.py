from flask import Flask
app = Flask(__name__)
@app.route('/')

def routing():
    return('hello world!')

@app.route('/dojo')
def dojo():
    return ('dojo')
    
@app.route('/say/flask')
def flask():
    return('flask')

@app.route('/say/micheal')
def micheal():
    return('miceal')


@app.route('/say/john')
def john():
    return('john')




@app.route('/say/<int:number>/<string:word>') #ai ***
def repeat(number, word):
    return f'{word} ' * number
    
    




if __name__=="__main__":
    app.run(debug=True)
    
    
    