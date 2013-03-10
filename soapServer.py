import os
from time import ctime
from flask import Flask
from flaskext.enterprise import Enterprise

app = Flask(__name__)
enterprise = Enterprise(app)

class Account(enterprise._scls.ClassModel):
    __namespace__ = 'http://soap.sforce.com/2005/09/outbound'
    Id = enterprise._sp.Integer

class AccountNotification(enterprise._scls.ClassModel):
    __namespace__ = 'http://soap.sforce.com/2005/09/outbound'
    Id = enterprise._sp.Integer
    Account = Account()
    
class DemoService(enterprise.SOAPService):
    __soap_target_namespace__ = 'http://soap.sforce.com/2005/09/outbound'
    
    @enterprise.soap(Account(), _returns=enterprise._sp.Boolean)
    def notifications(self, acct):
        Ack = True
        #print acct.Id
        return Ack
 
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    app.run()
