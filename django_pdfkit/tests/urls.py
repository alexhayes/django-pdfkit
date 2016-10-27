# -*- coding: utf-8 -*-
from django.conf.urls import url

from django_pdfkit.views import PDFView

urlpatterns = [  # pylint: disable=invalid-name
    url(r'^pdf/', PDFView.as_view(template_name='basic.html'), name='pdf'),
    url(r'^pdf-inline/', PDFView.as_view(inline=True, template_name='basic.html'), name='pdf-inline'),
    url(r'^pdf-filename/', PDFView.as_view(filename='foo.pdf', template_name='basic.html'), name='pdf-filename'),
]
