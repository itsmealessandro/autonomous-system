# Explaining actuators
This container contains The OSGi system that handle all the actuators.
The actuators are listening on a specific topic of MQTT waiting to act.
When a signal is recived they modify the JSON file that simulate the environment.
## OSGi actuators
There is a Actuators Handler Jar that constantly checks for: updates, new actuators and dismissed actuators.
Each actuator is in a JAR file and everytime a new actuator is created the handler will activate it.

