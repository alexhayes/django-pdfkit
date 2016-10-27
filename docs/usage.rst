=====
Usage
=====

Simply use the class based ``PDFView`` which is a drop in replacement for ``TemplateView``.

.. code-block:: python

    # urls.py
    from django_pdfkit import PDFView

    ...
    url(r'^my-pdf/$', PDFView.as_view(template_name='my-pdf.html'), name='my-pdf'),
    ...


Then in your browser goto ``http://localhost:8000/my-pdf/`` and it will magically
render as a PDF.

By default the PDF filename will be the same as the template file name however with
a ``.pdf`` file extension.


Query Parameter Support
-----------------------

The following query parameters can adjust the views behaviour.

- ``inline`` - don't set the ``CONTENT-DISPOSITION`` header, causing the PDF to be
  displayed inline if the browser supports it.
- ``download`` - set the ``CONTENT-DISPOSITION`` header (default).
- ``html`` - don't render as a PDF, render as HTML, useful for debugging your
  HTML output.
- ``debug`` - turn on debug mode when calling pdfkit - only works when
  ``settings.DEBUG`` is ``True``.

For example, ``http://localhost:8000/my-pdf/?inline`` - will cause the PDF to be
displayed inline.

Properties
----------

Define any of the following properties either as a kwarg to ``PDFView.as_view``
or as a property on the view.

- ``filename`` - set the downloadable filename.
- ``inline`` - default to display PDF inline, can be overridden with the
  ``download`` query string parameter.
- ``wkhtmltopdf_bin`` - set this is wkhtmltopdf is not on your path.
