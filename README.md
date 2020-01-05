# pyLearn-GUI
Learn to make GUI applications using Python

## Intro
I am learning PyQt5 to create various GUI applications using Python in Windows 10. I use Visual Studio Code as my Text Editor for programming and development. This repo contains "Hello World" type GUI applications.

## Initialize
To start developing applications in Python, following steps are required.  
* **Python** must be installed. To install Python, visit [Python's Official Website][python]. This project is developed in Python 3.8.1. Make sure path of Python is added to environment variables.
* A text editor or IDE is required to develop application. [Visual Studio Code][vscode] and [Sublime Text][sublime] are great text editors for programming. [PyCharm][pycharm] by JetBrains is the best IDE for Python programming. I am using Visual Studio Code.  
* **Virtual Environment** is recommended, but not necessary. When developing Python applications, it is a good practice to install new packages particular to project in a virtual environment to keep those packages separate.
    * Create a virtual environment "pygui-env" in current directory by execting following command in Terminal/Powershell/Command Prompt. pugui-env directory is created containing a new virtual environment.  
        ```powershell
        python -m venv pygui-env
        ```  
        ![pygui-env virtual environment directory](/docs/images/virtual_env.png)  
    * Activate "pygui-env" virtual environment. After activating, you will notice "pygui-env" at the beginning of each line.  
        ![Execute command pygui-env\Scripts\activate](/docs/images/activate_env.png)  
    * To deactivate virtual environment, execute following command.  
        ![Execute command deactivate](/docs/images/deactivate_env.png)  
    **Note:** Make sure virtual environment is active while installing packages and running python programs particular to this project.  
* Install [PyQt5][pyqt5]. Apps are created using PyQt5 v5.14.0. To install the latest version, execute the following command on powershell/command prompt/terminal:  
    ```powershell
    pip install PyQt5
    ```  
## Contents
1. [**Hello World** - My First GUI App](/hello_world)


[python]: https://www.python.org/
[vscode]: https://code.visualstudio.com/
[sublime]: https://www.sublimetext.com/
[pycharm]: https://www.jetbrains.com/pycharm/
[pyqt5]: https://www.riverbankcomputing.com/software/pyqt/download5