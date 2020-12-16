from setuptools import setup, find_packages

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="task-list",
    version="0.0.1",
    packages=find_packages(),
    install_requires=required,
    url="https://github.com/codurance/task-list",
    description="Task List Kata",
    entry_points={
        "console_scripts": [
            "task_list = task_list.__main__:main",
        ]
    },
)
