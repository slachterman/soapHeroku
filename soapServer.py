from time import ctime
from flask import Flask
from flaskext.enterprise import Enterprise

app = Flask(__name__)
enterprise = Enterprise(app)

class DemoService(enterprise.SOAPService):
    @enterprise.soap(_returns=enterprise._sp.String)
    def get_time(self):
        return ctime()
    
    @enterprise.soap(enterprise._sp.String,enterprise._sp.Integer,_returns=enterprise._scls.Array(enterprise._sp.String))
    def say_hello(self,name,times):
        results = []
        for i in range(0, times):
            results.append('Hello, %s' % name)
        return results

if __name__ == '__main__':
    app.run(debug=True)
