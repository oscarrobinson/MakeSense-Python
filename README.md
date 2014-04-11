#MakeSense-Python


Python module for adding data to the makesense platform


##Using makesensepy

###Getting a connection

```getConnection(string: username, int: apiId)``` returns ```MakeSenseConnection``` object

To create a connection to the MakeSense database, you simply call
```python
conn = getConnection(username, 1)
```

Where username is your MakeSense username and the number (1 in this example) is your API ID which you find on your MakeSense account

If your credentials are incorrect, ```getConnection()``` throws an ```AuthenticationException```



###Adding your data

If connection was successful, the MakeSense connection object is now stored in the variable you assigned it to

####Adding a Network

```void :: addNetwork(string: networkId, string: networkName="", string: networkDescription="")```

To add a network to the system you simply call
```python
conn.addNetwork("13124124")
```
on your connection object.  The number is an id number for the network, it can be anything you want.

If a network with your chosen id already exists, the method throws a ```MakeSenseDBException```

You can also add networks with a network name:
```python
conn.addNetwork("13124124", "Network Name")
```
and with a network description:
```python
conn.addNetwork("13124124", "Network Name", "This is the main network of sensors at MakeSenseHQ monitoring temperature")
```
####Adding a Sensor
```void :: addSensor(string: sensorId, string: networkId, string: sensorOntologyCode, string: sensorName="", string: sensorDescription="")```

To add a sensor you call

```python
conn.addSensor("234234234af", "13124124", "2")
```
```234234234af``` is a unique id you have chosen for your sensor.

```13124124``` is the id of the network the sensor is part of.

```2``` is the ontology code for the sensor (i.e what type of data it is sending).

If a sensor with the given sensorId already exists in the network with the given networkId, a ```MakeSenseDBException``` is thrown.

You can also add sensors with a name:
```python
conn.addSensor("234234234af", "13124124", "2", "Sensor Name")
```
and with a description:
```python
conn.addSensor("234234234af", "13124124", "2", "Sensor Name", "Temperature Sensor in room 1.21")
```




