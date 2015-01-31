PyTest
======



1 DESCRIPTION
-------------

A **keyword** driven open-source automation testing framework for acceptance testing and acceptance test-driven development (_ATDD_). The source code is in the _Python_ language and simple to understand.

2 INSTALLATION
--------------

###2.1 Selenium

If you have pip on your system, you can simply install or upgrade the Python bindings:

		pip install -U selenium


Alternately, you can download the source distribution from PyPI (e.g. selenium-2.44.tar.gz), unarchive it, and run:

		python setup.py install


__Note:__ both of the methods described above install selenium as a system-wide package That will require administrative/root access to ther machine. You may consider using a virtualenv to create isolated Python environments instead.

###2.2 PyTest

To use Pytest, clone the github repo to your local machine:

		git clone https://github.com/gauravmittal1995/pytest.git


Your ready to use PyTest

3 CONFIGURATION
---------------

Before you can run PyTest, you will need to set up the configuration file. For this copy the contents of __config_sample.py__ into __config.py__:

		cp config_sample.py config.py


Now set up the configuration based on your system and network and your done.

4 RUNNING
---------

To run the tests, use the __pytestrun.py__ file. We have an example file in the __example__ folder called __testfile.py__. To run it simply use the following command:

        python pytestrun.py example/testfile.pyt


5 STATUS
--------

This project is in very early development. Docs and Examples will added later.

6 LICENSE
---------

This project uses the MIT Open-Source License. See the [__LICENSE__] [1] file for more information.

[1]: https://github.com/gauravmittal1995/pytest/blob/master/LICENSE "LICENSE"  
