# tutorials2
# tutorials
pyramid_tutorial

Install
-------
Python 2.6 or 2.7 and header files
----------------------------------
On Debian or Ubuntu:
$ sudo apt-get install python2.7-d

Install virtualenv
==================
$ virtualenv . --no-site-packages

virtualenv's bin/python
=======================
After installing the virtualenv package, and creating your virtualenv
directory, you should have a Python executable inside the ``bin/``
directory.  Try to run it::

  $ bin/python
  Python 2.7.2+ (default, Oct  4 2011, 20:06:09) 
  [GCC 4.6.1] on linux2
  Type "help", "copyright", "credits" or "license" for more information.
  >>>
  
  Install Pyramid
===============

There's also ``bin/pip``, which you'll use to install Pyramid into
your new virtualenv::

  $ bin/pip install pyramid==1.4.5
  Downloading/unpacking pyramid==1.4.5
    Downloading pyramid-1.4.5.tar.gz (2.4Mb): 2.4Mb downloaded
  ...
  Successfully installed pyramid Chameleon Mako WebOb repoze.lru zope.interface zope.deprecation venusian translationstring PasteDeploy MarkupSafe
  Cleaning up...
  
  Run our  Pyramid-tutorial web app
=============================
  $ bin/python ex1_hello/hello.py
Starting server in PID 2533.
Starting HTTP server on http://0.0.0.0:6543
Now you can open http://0.0.0.0:6543 in your browser,
and you should see "Wellcom to the table of content finder".
