import os
from time import ctime
from flask import Flask
from flaskext.enterprise import Enterprise

app = Flask(__name__)
enterprise = Enterprise(app)

Array = enterprise._scls.Array
String = enterprise._sp.String
Integer = enterprise._sp.Integer

class ID(enterprise._scls.ClassModel):
    __namespace__ = 'urn:enterprise.soap.sforce.com'
    Id = String

class Account(enterprise._scls.ClassModel):
    __namespace__ = 'urn:sobject.enterprise.soap.sforce.com'    
    Id = String
    AccountNumber = Integer
    Type = String
    
class AccountNotification(enterprise._scls.ClassModel):
    __namespace__ = 'http://soap.sforce.com/2005/09/outbound'
    Id = Integer
    sObject = Array(Account)
    
class DemoService(enterprise.SOAPService):
    __soap_target_namespace__ = 'http://soap.sforce.com/2005/09/outbound'
    
    @enterprise.soap(ID(), ID(), String, String, String, AccountNotification(), _returns=enterprise._sp.Boolean)
    def notifications(self, OrganizationId, ActionId, SessionId, EnterpriseUrl, PartnerUrl, Notification):
        Ack = True
        #print acct.Id
        return Ack
 
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    app.run()
