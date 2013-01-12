import suds

url = 'http://localhost:5000/_enterprise/soap?wsdl'
client = suds.client.Client(url)

sTime = client.service.get_time()
print sTime

