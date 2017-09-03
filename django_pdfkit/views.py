# -*- coding: utf-8 -*-
"""
    django_pdfkit.views
    ~~~~~~~~~~~~~~~~~~~

    Django view that converts HTML to PDF using webkit - via pdfkit and wkhtmltopdf.
"""
from __future__ import absolute_import, print_function, unicode_literals

import os

from os.path import basename, splitext

import pdfkit

from django.conf import settings
from django.http import HttpResponse
from django.template import loader
from django.test import override_settings
from django.views.generic import TemplateView


class PDFView(TemplateView):
    #: Set to change the filename of the PDF.
    filename = None

    #: Set to default the PDF display to inline.
    inline = False

    #: Set pdfkit options dict.
    pdfkit_options = None

    #: Set to false if you don't want render html
    html = True

    def get(self, request, *args, **kwargs):
        """
        Return a HTTPResponse either of a PDF file or HTML.

        :rtype: HttpResponse
        """
        if self.html is True:
            # Output HTML
            content = self.render_html(*args, **kwargs)
            return HttpResponse(content)

        else:
            # Output PDF
            content = self.render_pdf(*args, **kwargs)

            response = HttpResponse(content, content_type='application/pdf')

            if (not self.inline or 'download' in request.GET) and 'inline' not in request.GET:
                response['Content-Disposition'] = 'attachment; filename=%s' % self.get_filename()

            response['Content-Length'] = len(content)

            return response

    def render_pdf(self, *args, **kwargs):
        """
        Render the PDF and returns as bytes.

        :rtype: bytes
        """
        html = self.render_html(*args, **kwargs)

        options = self.get_pdfkit_options()
        if 'debug' in self.request.GET and settings.DEBUG:
            options['debug-javascript'] = 1

        kwargs = {}
        wkhtmltopdf_bin = os.environ.get('WKHTMLTOPDF_BIN')
        if wkhtmltopdf_bin:
            kwargs['configuration'] = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_bin)

        pdf = pdfkit.from_string(html, False, options, **kwargs)

        return pdf

    def get_pdfkit_options(self):
        """
        Returns ``self.pdfkit_options`` if set otherwise a default dict of options to supply to pdfkit.

        :rtype: dict
        """
        options = {'page-size': 'A4', 'encoding': 'UTF-8'}
        if self.pdfkit_options is not None:
            options.update(self.pdfkit_options)
        return options

    def get_filename(self):
        """
        Return ``self.filename`` if set otherwise return the template basename with a ``.pdf`` extension.

        :rtype: str
        """
        if self.filename is None:
            name = splitext(basename(self.template_name))[0]
            return '{}.pdf'.format(name)

        return self.filename

    def render_html(self, *args, **kwargs):
        """
        Renders the template.

        :rtype: str
        """
        static_url = '%s://%s%s' % (self.request.scheme, self.request.get_host(), settings.STATIC_URL)
        media_url = '%s://%s%s' % (self.request.scheme, self.request.get_host(), settings.MEDIA_URL)

        with override_settings(STATIC_URL=static_url, MEDIA_URL=media_url):
            template = loader.get_template(self.template_name)
            context = self.get_context_data(**kwargs)
            html = template.render(context)
            return html
