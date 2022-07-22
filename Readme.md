
Python OCR : Optical Character Rendering In Python
=======================================

[![Documentation Status](https://readthedocs.org/projects/pip/badge/)](https://github.com/Poojan670/python-OCR/blob/main/Readme.md)


Got a question?
---------------

I am always happy to answer questions! Here are some good places to ask them:

- for anything you're curious about, try [gitter chat](https://gitter.im/python/typing)
- for general questions about Python typing, try [typing discussions](https://github.com/python/typing/discussions)

If you think you've found a bug:

- check our [common issues page](https://mypy.readthedocs.io/en/stable/common_issues.html)
- search our [issue tracker](https://github.com/python/mypy/issues) to see if
  it's already been reported
- consider asking on [gitter chat](https://gitter.im/python/typing)

To report a bug or request an enhancement:

- report at [our issue tracker](https://github.com/Poojan670/python-OCR/issues)
- if the issue is with a specific library or function, consider reporting it at
  [typeshed tracker](https://github.com/python/typeshed/issues) or the issue
  tracker for that library

To discuss a new type system feature:
- discuss at my  [personal email](https://mail.google.com/mail/?view=cm&source=mailto&to=[po0janhunt@gmail.com])
- there is also some historical discussion [here](https://github.com/python/typing/issues)


What is python-OCR?
-------------

python-OCR is an Optical Character Rendering Application developed in Python.

Application's GUI was developed using Tkinter

It works as an Image To Text Rendering Application, that was done using  pytesseract, python-cv and Pillow

It also works for PDF To Text Rendering, Using PyDF2

Type checkers help ensure that you're using variables and functions in your code
correctly. 

Python is a dynamic language, 
so it can be used in various aspects of programming,
starting from basic problem-solving to machine learning, 
web development and even data science


python-OCR is designed with gradual user input interface 
and reliability in mind,
so it is extremely simple to use 
and faster to communicate and gets the work done in very less time 

Here is a small example about pytessaract's import and use:

```python
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
```

See [the tessaract documentation](https://pypi.org/project/pytesseract/) for more details..

In particular, see:
- [about tkinter](https://www.tutorialspoint.com/how-to-install-tkinter-in-python)
- [PyDF2](https://pypi.org/project/PyPDF2/)


Quick start
-----------

**Install Tesseract on your respective OS**
- [Tessaract](https://github.com/UB-Mannheim/tesseract/wiki)


Create a python virtual env:

    py -m venv env


Activates virtual environment:

    env/Scripts/activate

Install the project requirements:

    pip install -r requirements.txt

Run the application

    py main.py 

**Make sure that your "tessaract.exe" relative location is set properly**

You can also try [OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF) for detailed PDF OCR


Contributing
------------

Help in testing, development, documentation and other tasks is
highly appreciated and useful to the project. There are tasks for
contributors of all experience levels.

To get started with testing and contributing to this project, see [CONTRIBUTING.md](https://license.md/).

If you need help getting started, don't hesitate to ask or mail your queries.


Development status
------------------

python-OCR is beta software, developed solely for testing and entertainment purposes in my free time


To contribute to the python-OCR project, check out https://github.com/Poojan670/python-OCR