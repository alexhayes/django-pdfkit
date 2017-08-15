# -*- coding: utf-8 -*-
"""Django view that converts HTML to PDF using webkit."""
# :copyright: (c) 2016 Alex Hayes,
#                 All rights reserved.
# :license:   MIT License, see LICENSE for more details.
from __future__ import absolute_import, print_function, unicode_literals
from collections import namedtuple

VersionInfo = namedtuple(
    'VersionInfo', ('major', 'minor', 'micro', 'releaselevel', 'serial'),
)

VERSION = VersionInfo(0, 3, 1, '', '')
__version__ = '{0.major}.{0.minor}.{0.micro}{0.releaselevel}'.format(VERSION)
__author__ = 'Alex Hayes'
__contact__ = 'alex@alution.com'
__homepage__ = 'http://github.com/alexhayes/django-pdfkit'
__docformat__ = 'restructuredtext'

# -eof meta-

from django_pdfkit.views import PDFView  # pylint: disable=wrong-import-position
