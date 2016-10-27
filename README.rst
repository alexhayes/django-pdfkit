=============
Django PDFKit
=============

Django view that converts HTML to PDF using webkit - via pdfkit_ and wkhtmltopdf_.

.. image:: https://travis-ci.org/alexhayes/django-pdfkit.png?branch=master
    :target: https://travis-ci.org/alexhayes/django-pdfkit
    :alt: Build Status

.. image:: https://landscape.io/github/alexhayes/django-pdfkit/master/landscape.png
    :target: https://landscape.io/github/alexhayes/django-pdfkit/
    :alt: Code Health

.. image:: https://codecov.io/github/alexhayes/django-pdfkit/coverage.svg?branch=master
    :target: https://codecov.io/github/alexhayes/django-pdfkit?branch=master
    :alt: Code Coverage

.. image:: https://readthedocs.org/projects/django-pdfkit/badge/
    :target: http://django-pdfkit.readthedocs.org/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/pypi/v/django-pdfkit.svg
    :target: https://pypi.python.org/pypi/django-pdfkit
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/pyversions/django-pdfkit.svg
    :target: https://pypi.python.org/pypi/django-pdfkit/
    :alt: Supported Python versions

.. image:: https://img.shields.io/pypi/dd/django-pdfkit.svg
    :target: https://pypi.python.org/pypi/django-pdfkit/
    :alt: Downloads


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


Install
-------

.. code-block:: bash

    pip install django-pdfkit


Usage
-----

Simply use the class based ``PDFView`` which is a drop in replacement for ``TemplateView``.

.. code-block:: python

    # urls.py
    from django_pdfkit import PDFView

    ...
    url(r'^my-pdf/$', PDFView.as_view(template_name='my-pdf.html'), name='my-pdf'),
    ...


Then in your browser goto ``http://localhost:8000/my-pdf/`` and it will magically
render as a PDF.

See the docs_ for more information.


Author
------

Alex Hayes <alex@alution.com>

.. _docs: http://django-pdfkit.readthedocs.org/en/latest/
.. _pdfkit: https://pypi.python.org/pypi/pdfkit
.. _wkhtmltopdf: http://wkhtmltopdf.org/
