# Arduino Experiments

Python programs to terst with Arduino, using the [Lib pyFirmata](https://github.com/tino/pyFirmata).  
To use, firstgo to [Arduino page](https://www.arduino.cc/en/software) and install the Arduino Agent.   
The Arduino IDE is a good idea too, since you can use in original language, but you can use the [web IDE](https://create.arduino.cc/editor)

create the Virtual Environment as usual  
`python -m venv venv`

and intal the lib pyFirmata  
`pip install pyfirmata`

and joy

## Reference
https://realpython.com/arduino-python/  


## Simple Blink
A blink led with python with a for

## Simple Blink 2
With different sequence
![Arduino Uno sketch with breadboard ](https://files.realpython.com/media/blink_2.0a1b1975b7da.png)

## Digital Inputs
Use button to capture digital inputs
write in the terminal when click.

## Digital inputs 2
same as above but blink the led
![Arduino Uno with breadboard digital Inputs](https://files.realpython.com/media/digital_input_2.a46059238b65.png)


## read Analogic Input
read the potentiometer and print on terminal the value

## Read Analogic Input 2
same as above but control the interval between 2 leds(the scketch bellow shows just one led)
![](https://files.realpython.com/media/analog_input_2.1d0464a94dd5.png)