# -*- coding: utf-8 -*-
"""
    django_pdfkit.views
    ~~~~~~~~~~~~~~~~~~~

    Django view that converts HTML to PDF using webkit - via pdfkit and wkhtmltopdf.
"""
from __future__ import absolute_import, print_function, unicode_literals

from os.path import basename, splitext

from django.conf import settings
from django.http import HttpResponse
from django.template import RequestContext
from django.template import loader
from django.test import override_settings
from django.views.generic import TemplateView
import pdfkit


class PDFView(TemplateView):
    #: Set to change the filename of the PDF.
    filename = None

    #: Set to default the PDF display to inline.
    inline = False

    #: Set pdfkit options dict.
    pdfkit_options = None

    #: Set the path to the wkhtmltopdf binary.
    wkhtmltopdf_bin = None

    def get(self, request, *args, **kwargs):
        """
        Return a HTTPResponse either of a PDF file or HTML.

        :rtype: HttpResponse
        """
        if 'html' in request.GET:
            # Output HTML
            content = self.render_html()
            return HttpResponse(content)

        else:
            # Output PDF
            content = self.render_pdf()

            response = HttpResponse(content, content_type='application/pdf')

            if (not self.inline or 'download' in request.GET) and 'inline' not in request.GET:
                response['Content-Disposition'] = 'attachment; filename=%s' % self.get_filename()

            response['Content-Length'] = len(content)

            return response

    def render_pdf(self):
        """
        Render the PDF and returns as bytes.

        :rtype: bytes
        """
        html = self.render_html()

        options = self.get_pdfkit_options()
        if 'debug' in self.request.GET and settings.DEBUG:
            options['debug-javascript'] = 1

        kwargs = {}
        if self.wkhtmltopdf_bin:
            kwargs['configuration'] = pdfkit.configuration(wkhtmltopdf=settings.WKHTMLTOPDF_BIN)

        pdf = pdfkit.from_string(html, False, options, **kwargs)

        return pdf

    def get_pdfkit_options(self):
        """
        Returns ``self.pdfkit_options`` if set otherwise a default dict of options to supply to pdfkit.

        :rtype: dict
        """
        if self.pdfkit_options is not None:
            return self.pdfkit_options
        else:
            return {
                'page-size': 'A4',
                'encoding': 'UTF-8',
            }

    def get_filename(self):
        """
        Return ``self.filename`` if set otherwise return the template basename with a ``.pdf`` extension.

        :rtype: str
        """
        if self.filename is None:
            name = splitext(basename(self.template_name))[0]
            return '{}.pdf'.format(name)
        else:
            return self.filename

    def render_html(self):
        """
        Renders the template.

        :rtype: str
        """
        static_url = '%s://%s%s' % (self.request.scheme, self.request.get_host(), settings.STATIC_URL)
        with override_settings(STATIC_URL=static_url):
            template = loader.get_template(self.template_name)
            context = self.get_context_data(**{})
            request_context = RequestContext(self.request, context)
            html = template.render(request_context)
            return html
