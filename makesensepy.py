import requests

def addSensor(sensorId, netId, sensorOnt):
	payload = {'sensorId': sensorId, 'netId': netId, 'sensorOnt': sensorOnt}
	r = requests.post("http://uclteam10.azurewebsites.net/testpost.php", data=payload)

addSensor("thing","thing2","12")
