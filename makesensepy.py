import requests

address = "http://localhost:8888/apicontroller.php"

#REQUEST CODES
authenticationCode = "1"
addSensorCode = "10"
addReadingCode  = "20"

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

class DataException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


def getConnection(username, apiId):
	return MakeSenseConnection(username, apiId)


class MakeSenseConnection:
	def __init__(self, username, apiId):
		payload = {'requestCode':authenticationCode, 'username':username, 'apiId':apiId}
		r = requests.post(address, data=payload)
		if r.text=="1001":
			raise AuthenticationException("username or API access id is not valid")
		else:
			self.username = username
			self.id = apiId

	def addSensor(self,sensorId, netId, sensorOnt, sensorName="", sensorDescription=""):
		if len(sensorId)>30:
			raise DataException("SensorId is too long (Max 30 chars)")
		if len(netId)>20:
			raise DataException("NetworkId is too long (Max 20 chars)")
		try:
			int(sensorOnt)
		except ValueError:
			raise DataException("Sensor Ontology Code is not an integer")
		if len(sensorName)>150:
			raise DataException("SensorName is too long (Max 150 chars)")
		if len(sensorDescription)>20000:
			raise DataException("SensorDescription is too long (Max 20000 chars)")
		payload = {'requestCode': addSensorCode, 'sensorId': sensorId, 'netId': netId, 'sensorOnt': sensorOnt, 'sensorDescription':sensorDescription, 'sensorName':sensorName, 'username': self.username, 'id':self.id}
		r = requests.post(address, data=payload)
		if r.text == "23000":
			raise MakeSenseDBException("A sensor with Id '"+sensorId+"' already exists in the database")
		elif r.text[:4] == "1001":
			raise AuthenticationException("username or API access id is not valid")

	def addReading(self, sensorId, reading, timestamp):
		if len(sensorId)>30:
			raise DataException("SensorId is too long (Max 30 chars)")
		if len(reading)>40:
			raise DataException("Reading is too long (Max 40 chars)")
		try:
			int(timestamp)
		except ValueError:
			raise DataException("Timestamp is not a valid int")
		payload = {'requestCode':addReadingCode, 'username': self.username, 'id':self.id, 'sensorId': sensorId, 'reading':reading, 'timestamp':timestamp}
		r = requests.post(address, data=payload)
		if r.text[:4] == "1001":
			raise AuthenticationException("username or API access id is not valid")
		elif r.text == "23000":
			raise MakeSenseDBException("Data at time "+timestamp+" already exists for sensor with id "+sensorId)


conn = getConnection("oscar",11)
conn.addReading("robkera","112", "121341");
#addSensor("thing","thing2","12")