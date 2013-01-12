import suds

url = 'http://thawing-forest-6142.herokuapp.com/_enterprise/soap?wsdl'
client = suds.client.Client(url)

sTime = client.service.get_time()
print sTime
