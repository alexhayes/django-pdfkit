============
Installation
============

Prerequisites
-------------

You need to install wkhtmltopdf_.

The versions in Debian/Ubuntu repositories (installed using ``apt-get install wkhtmltopdf``)
have reduced functionality and you will most likely want to install one of the
stable binaries provided at http://wkhtmltopdf.org/downloads.html which provide
increased functionality (headless, patched Qt, better rendering support).

Installation of the pre-compiled binaries on Ubuntu is as simple as;

.. code-block:: bash

    wget http://download.gna.org/wkhtmltopdf/0.12/0.12.3/wkhtmltox-0.12.3_linux-generic-amd64.tar.xz
    tar -xf wkhtmltox-0.12.3_linux-generic-amd64.tar.xz
    sudo cp -r wkhtmltox/* /usr/


pdfkit_ will automatically look for the ``wkhtmltohtml`` binary on your path
however if it's not on your path you can :ref:`set it <wkhtmltopdf-bin>`.

Install
-------

You can install django-pdfkit either via the Python Package Index (PyPI)
or from github.

To install using pip;

.. code-block:: bash

    $ pip install django-pdfkit

From github;

.. code-block:: bash

    $ pip install git+https://github.com/alexhayes/django-pdfkit.git


.. _wkhtmltopdf: http://wkhtmltopdf.org/
.. _pdfkit: https://pypi.python.org/pypi/pdfkit
