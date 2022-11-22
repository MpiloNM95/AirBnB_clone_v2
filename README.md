# 0x00. AirBnB clone - The console
## Introduction
This is the first part of the AirBnB clone project for ALX Africa in this case we need to create the consolethat will be used for testing and manage objects of our project.
## How to start the console ##
for start the console you can do it on an interactive mode using ```./console.py``` or on an non-interactivemode using ```echo "command" | ./console.py```(where command is the command that will be passed)
### First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

* put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
* create the first abstracted storage engine of the project: File storage.
* create all unittests to validate all our classes and storage engine
## Resources:books:
* [cmd module](https://docs.python.org/3.8/library/cmd.html)
* [uuid module](https://docs.python.org/3.8/library/uuid.html)
* [datetime](https://docs.python.org/3.8/library/datetime.html)
* [unittest module](https://docs.python.org/3.8/library/unittest.html#module-unittest)
* [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
* [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)
