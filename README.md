**This is no longer maintained since I have moved on to using cookiecutter**

packageskel - A python project skeleton maker.
===

packageskel is a no frills simple python skeleton project maker. This project started out as a simple script to create a module dicrectory and deploy a skeleton setup.py. In time I added a few makefiles until it has arrrived to its current basic featureset.

- creates a setup.py and a module directory with sample hello_world class file
- deploys Makefiles for running tests and building different versions of python into a virtualenv. 

Install 
===

```pip install packageskel``` 

or install from source:

Clone this file and then do:

```python setup.py install``` 

Usage
===

RHEL/Centos/Fedora
====

Skeleton code created by packageskel provides a Makefile to build different versions of python to code and test with.This an be set in configurations.ml. 

However in order for it to build python properly we need a few libraries. Install them as follows:

```
yum -y install npm gcc sqlite-devel openssl-devel libtiff-devel openjpeg-devel \
openjpeg2-devel libjpeg-turbo-devel  zlib-devel  freetype-devel lcms-devel \
lcms2-devel libexif-devel libffi-devel
```



```packageskel mymodule```

This will create a new mymodule 

```
[jnvilo@gt72vr mymodule]$ tree
.
├── configuration.mk
├── LICENSE.txt
├── Makefile
├── make-includes
│   ├── LICENSE.txt
│   ├── Makefile
│   ├── posix-shell.mk
│   ├── post-build.mk
│   ├── python.mk
│   ├── README.md
│   ├── sort.xslt
│   ├── test
│   │   ├── python-requirements.txt
│   │   ├── result.xml.test
│   │   ├── test.xml.orig
│   │   └── version.py
│   ├── variables.mk
│   └── xml.mk
├── mymodule
│   ├── __init__.py
│   └── mymodule.py
├── README.md
├── requirements.txt
├── setup.cfg
├── setup.py
└── tests
    ├── __init__.py
    ├── mymodule_tests.py
    └── utilities.py

```

Code module is in mymodule. 


Build a custom python
===
Running: 


```make```

will download and compile the latest python in the build directory and create a symlink to it virtualenv.


Test
---

```make test```

will run all the tests in tests directory


You can also test with a specific version of Python:

    make PYTHON_VERSION=2.7.11 test
