import requests

#REQUEST CODES
addSensorCode = "1"

class MakeSenseDBException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def addSensor(sensorId, netId, sensorOnt, sensorName="", sensorDescription=""):
	print sensorName+sensorDescription
	payload = {'requestCode': addSensorCode, 'sensorId': sensorId, 'netId': netId, 'sensorOnt': sensorOnt, 'sensorDescription':sensorDescription, 'sensorName':sensorName}
	r = requests.post("http://uclteam10.azurewebsites.net/apicontroller.php", data=payload)
	if r.text == "23000":
		raise MakeSenseDBException("A sensor with Id '"+sensorId+"' already exists in the database")

addSensor("thing","thing2","12")