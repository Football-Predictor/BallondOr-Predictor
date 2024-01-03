# Ballon d'Or Predictor

## Setup

### Virtual Environment (Optional but Recommended)

A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated Python virtual environments for them. This is one of the most important tools that most of the Python developers use.

#### Installation

If you haven't installed the virtual environment yet, you can do so by running:

```sh
pip install virtualenv
```
#### Creating a Virtual Environment
```sh
virtualenv venv
```
This will create a new folder named venv in your project directory.

#### Activating the Virtual Environment
Before you can start installing or using packages in your virtual environment you’ll need to activate it. Activating a virtual environment will put the virtual environment-specific python and pip executables into your shell’s PATH.

- On macOS and Linux:
```sh
source venv/bin/activate
```
- On Windows:
```sh
.\venv\Scripts\activate
```

#### Installing Dependencies
```sh
pip install -r requirements.txt
```
This command will download all the necessary packages needed for this project.


Data Pulled: 03/05/2023 <br>
See how to contribute: [Contribution Guide](CONTRIBUTING.md)
