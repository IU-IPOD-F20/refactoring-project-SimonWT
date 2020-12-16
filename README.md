### Students
* Yaroslav Yudinskikh
* Rinat Mullakhmetov

# Refactoring Project

## Intstallation & Running
### Requirements
* python 3
* pip 3
* docker
### Install
``python3 setup.py install``

### Run Application
``python3 test_list``

### Run Tests
``RINAT NAPISHI ZDES``

#### Build app
``docker build -t dp .``
#### Run app
``docker run dp:latest``
## Refactoring Results
### Changes
#### "Objectize"
First thing that came in mind was to objectize app. Devide initial app.py to different objects. 
By division we got tree main categories of classes Task, Command and App with TaskList.

>/task_list/app.py

>/task_list/command/

>/task_list/task/
#### Composite
Further we found out that some commands consists of two words and have similar one in the begin of command string.
> add project <project name>

and 

> add task <project name> <task description>

It looks like this command have tree like structure with root `add` and leafs `task` and `project`. This fact pushed us to use Composite pattern.

So we have one common interface of the command and two realization of it. Composite and Leaf. 

Composite - used to composite leafs and other composites down to the tree and navigate user command input to defined leaf, which will execute business logic. It stores childs in Dict, where key is a command name of a child and value is the child.

Leaf - is an endpoint of the command tree, which takes arguments and perform some business logic.

It means that our application have the "root", which is Composite and stores other commands like children and pass user to required leafs.

[reference](https://refactoring.guru/design-patterns/composite)

##### Example
> `add project <project name> `

* `add` - is Composite which stores in root with key "add"
* `project <project name>` - is a Leaf, which stores in Composite above by key "project", and perform adding project to the app.
#### Strategy

We have Leafs, which should perform some business logic. So by using Strategy pattern we created realization of Leaf for each user tasks: 
- add
  - task
  - project
- show
- help
- ... 

#### Front-Controller
To perform required command we need to pass the user input to the controller, which will pass user input to root command and then pass execution line to required command.
>/task_list/controller.py

[reference](https://en.wikipedia.org/wiki/Front_controller)
#### Singletone
We use Singletone for Console object, to avoid creating several instances for input and output stream for out app.

Also we make object TaskList, which contain projects and tasks, Signletone.

[reference](https://refactoring.guru/design-patterns/singleton)
## Tests

## CI