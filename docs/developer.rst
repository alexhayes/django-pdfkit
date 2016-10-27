Developer Documentation
=======================

Contributions
-------------

Contributions are more than welcome!

To get setup do the following;

.. code-block:: bash

    mkvirtualenv --python=/usr/bin/python3.5 django-pdfkit
    git clone https://github.com/alexhayes/django-pdfkit.git
    cd django-pdfkit
    pip install -r requirements/dev.txt
    pip install Django


Running Tests
-------------

Once you've checked out you should be able to run the tests;

.. code-block:: bash

    tox

Or run all environments at once using detox;

.. code-block:: bash

    detox


Creating Documentation
----------------------

.. code-block:: bash

    cd docs
    make clean html

