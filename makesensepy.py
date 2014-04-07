import requests

#REQUEST CODES
authenticationCode = "1"
addSensorCode = "10"

class AuthenticationException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class MakeSenseDBException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def getConnection(username, apiId):
	return MakeSenseConnection(username, apiId)


class MakeSenseConnection:
	def __init__(self, username, apiId):
		payload = {'requestCode':authenticationCode, 'username':username, 'apiId':apiId}
		r = requests.post("http://uclteam10.azurewebsites.net/apicontroller.php", data=payload)
		if r.text=="1001":
			raise AuthenticationException("username or API access id is not valid")
		else:
			self.username = username
			self.id = apiId

	def addSensor(self,sensorId, netId, sensorOnt, sensorName="", sensorDescription=""):
		print sensorName+sensorDescription
		payload = {'requestCode': addSensorCode, 'sensorId': sensorId, 'netId': netId, 'sensorOnt': sensorOnt, 'sensorDescription':sensorDescription, 'sensorName':sensorName, 'username': self.username, 'id':self.id}
		r = requests.post("http://uclteam10.azurewebsites.net/apicontroller.php", data=payload)
		if r.text == "23000":
			raise MakeSenseDBException("A sensor with Id '"+sensorId+"' already exists in the database")


conn = getConnection("oscar",11)
conn.addSensor("lolId", "anNetwork", "1")
#addSensor("thing","thing2","12")