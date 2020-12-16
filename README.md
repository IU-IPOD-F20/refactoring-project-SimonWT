### Students
* Yaroslav Yudinskikh
* Rinat Mullakhmetov

# Refactoring Project

## Intstallation & Running
### Requirements
* python 3
* pip 3
* docker
## Environment
Recommend you to run in docker container (You need pre-installed docker client).

All python dependencies in ``requirements.txt``.

### Build docker
```console
docker build -t dp .
```

### Test automatically

```console
docker run dp:latest
```

### Test by hands
```console
docker run -it --rm --entrypoint /bin/bash dp:latest
behave /app/features
python task_list
```

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

![Commands](./images/app_command.png?raw=true "Commands")
#### Strategy

We have Leafs, which should perform some business logic. So by using Strategy pattern we created realization of Leaf for each user tasks: 
- add
  - task
  - project
- show
- help
- ... 

![App Commands](./images/command.png?raw=true "App Commands")

#### Front-Controller
To perform required command we need to pass the user input to the controller, which will pass user input to root command and then pass execution line to required command.
>/task_list/controller.py

[reference](https://en.wikipedia.org/wiki/Front_controller)
#### Singletone
We use Singletone for Console object, to avoid creating several instances for input and output stream for out app.

Also we make object TaskList, which contain projects and tasks, Signletone.

### Final UML

![App](./images/app.png?raw=true "App")

[reference](https://refactoring.guru/design-patterns/singleton)
## Tests
1) Save unittests in ```./tests``` for `regression testing` already executed test cases which are re-executed to ensure existing functionalities work fine.

2) Behavior-driven development (BDD) tests in ```./feature```. Basic scenarios are covered here.

3) There is an opportunity to test app by hands in isolated environment (using docker)

## CI
1) Run docker container and tests there
2) Run black formater
3) Run flake8 linter

```yaml
on: [push]

jobs:
  behave_tests:
    runs-on: ubuntu-latest
    steps:
    - name: Hello world action step
      uses: IU-IPOD-F20/refactoring-project-SimonWT@master
  black:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
      - uses: psf/black@stable
  flake8-lint:
    runs-on: ubuntu-latest
    name: Lint
    steps:
      - name: Check out source repository
        uses: actions/checkout@v2
      - name: Set up Python environment
        uses: actions/setup-python@v1
        with:
          python-version: "3.7"
      - name: flake8 Lint
        uses: py-actions/flake8@v1
```