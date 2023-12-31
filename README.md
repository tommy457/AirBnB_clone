# AirBnB clone - The console

## Description

### Welcome to the AirBnB clone project!
This team project is part of the ALX Full-Stack Software Engineer program.

This is the first step towards building my first full web application: the AirBnB clone.
This first step is very important because we will use what we build during this project with all other following projects: 
HTML/CSS templating, database storage, API, front-end integration… 

## Usage

The console works both in interactive mode and non-interactive mode.
It prints a prompt **(hbnb)** and waits for the user for input.

Command | Example
------- | -------
Run the console | ```./console.py```
Quit the console | ```(hbnb) quit```
Display the help for a command | ```(hbnb) help <command>```
Create an object (prints its id)| ```(hbnb) create <class>```
Show an object | ```(hbnb) show <class> <id>``` or ```(hbnb) <class>.show(<id>)```
Destroy an object | ```(hbnb) destroy <class> <id>``` or ```(hbnb) <class>.destroy(<id>)```
Show all objects, or all instances of a class | ```(hbnb) all``` or ```(hbnb) all <class>```
Update an attribute of an object | ```(hbnb) update <class> <id> <attribute name> "<attribute value>"``` or ```(hbnb) <class>.update(<id>, <attribute name>, "<attribute value>")```

Non-interactive mode example

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
```

## Tests

All the code is tested with the **unittest** module.
