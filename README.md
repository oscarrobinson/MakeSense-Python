#MakeSense-Python


Python module for adding data to the makesense platform

##Installing makesensepy

**To use makesensepy you must first have the [requests](http://docs.python-requests.org/en/latest/) module installed**

Download the files either by downloading the .zip from [here](https://github.com/scarrobin/MakeSense-Python/archive/master.zip) or by typing
```git clone https://github.com/scarrobin/MakeSense-Python.git``` in the terminal

then simply unzip and navigate to the MakeSense-Python folder and type
```python setup.py install```

The makesensepy module is now installed on your system


##Using makesensepy

Before using makesensepy, remember to
```python
import makesensepy
```
at the top of your python file

###Getting a connection

```getConnection(string: username, int: apiId)``` returns ```MakeSenseConnection``` object

To create a connection to the MakeSense database, you simply call
```python
conn = makesensepy.getConnection(username, "1")
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

If a sensor with the given sensorId already exists in the system, a ```MakeSenseDBException``` is thrown.

You can also add sensors with a name:
```python
conn.addSensor("234234234af", "13124124", "2", "Sensor Name")
```
and with a description:
```python
conn.addSensor("234234234af", "13124124", "2", "Sensor Name", "Temperature Sensor in room 1.21")
```
####Adding a Reading
```void :: addReading(string: sensorId, string: reading, string: timestamp)```

To add a reading you call
```python
conn.addReading("234234234af", "1234.12", "1397235431")
```
```234234234af``` is the id of the sensor for which you are adding a reading.

```1234.12``` is the reading you are adding for that sensor.

```1397235431``` is the timestamp for the data in UNIX time format.

**_Timestamps MUST be in UNIX time format otherwise your data will be displayed incorrectly on the MakeSense site_**

If you attempt to add a reading for a given sensorId for a time where there is already a reading, a ```MakeSenseDBException``` is thrown.

####Adding an Ontology
```string :: addOntology(string: name, string: description, string: axis)```
Ontology codes allow the MakeSense to automatically render your graphs on the site with proper axis labels etc.
There are a number of ontologies already available but you may want to add your own, you can do so with this method.

To add an ontology:
```python
ontologyCode = conn.addOntology("distance", "distance the thing has travelled in centimetres", "distance/cm")
```
```distance``` is the name of your ontology.

```distance the thing has travelled in centimetres``` if a brief description of your ontology.

```distance/cm``` is the axis label that will be used on the graph of any data using this ontology.

the method returns the id code for the ontology, if the ontology already exists, the code of the existing ontology is returned.  In this example, the code is now stored as a string in the ```ontologyCode``` variable. 

So you could now use this ontology in your own code e.g adding a sensor:
```python
conn.addSensor("thisisasensorid", "thisisanetworkid", ontologyCode)
```



