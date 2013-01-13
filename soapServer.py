import os
from time import ctime
from flask import Flask
from flaskext.enterprise import Enterprise

app = Flask(__name__)
enterprise = Enterprise(app)

class Account(enterprise._scls.ClassModel):
    __namespace__ = 'tns'
    Id = enterprise._sp.String
    
class DemoService(enterprise.SOAPService):
    __soap_target_namespace__ = 'http://soap.sforce.com/2005/09/outbound'
    
    account = Account() 
    
    @enterprise.soap(_returns=enterprise._sp.String)
    def get_time(self):
        return ctime()
    
    @enterprise.soap(enterprise._sp.String,enterprise._sp.Integer,_returns=enterprise._scls.Array(enterprise._sp.String))
    def say_hello(self,name,times):
        results = []
        for i in range(0, times):
            results.append('Hello, %s' % name)
        return results
    
    @enterprise.soap(account, _returns=enterprise._sp.Boolean)
    def notifications(self, account):
        Ack = True
        return Ack
 
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    app.run()
