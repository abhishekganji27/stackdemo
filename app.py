from flask import Flask
# from redis import Redis

app = Flask(__name__)
# redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    # count = redis.incr('hits')
    return 'Hello World!...home route' 
    # I have been seen {} times.\n'.format(count)

@app.route('/sample')
def sample():
    return 'this is the sample route'
    
@app.route('/new')
def sample():
    return 'this is the new route, in stackdemo:v8'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
