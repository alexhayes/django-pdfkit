from __future__ import absolute_import

import os

try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse

TESTS_ROOT = os.path.dirname(os.path.abspath(__file__))
TESTS_TEMPLATE_DIR = os.path.join(TESTS_ROOT, 'templates')


def test_pdf(client):
    """
    Test that a PDF is downloaded.
    """
    urls = [
        reverse('pdf'),
        '%s?download' % reverse('pdf-inline'),
    ]
    for url in urls:
        response = client.get(url)

        assert response.status_code == 200

        assert response.has_header('content-disposition')
        assert response.has_header('content-length')
        assert response.has_header('content-type')

        assert response['content-disposition'] == 'attachment; filename=basic.pdf'
        assert int(response['content-length']) > 0
        assert response['content-type'] == 'application/pdf'


def test_pdf_inline(client):
    """
    Test that a PDF is inline.
    """
    urls = [
        '%s?inline' % reverse('pdf'),
        reverse('pdf-inline'),
    ]
    for url in urls:
        response = client.get(url)

        assert response.status_code == 200

        assert not response.has_header('content-disposition')
        assert response.has_header('content-length')
        assert response.has_header('content-type')

        assert int(response['content-length']) > 0
        assert response['content-type'] == 'application/pdf'


def test_pdf_filename(client):
    """
    Test setting a filename works.
    """
    response = client.get(reverse('pdf-filename'))

    assert response.status_code == 200

    assert response.has_header('content-disposition')
    assert response.has_header('content-length')
    assert response.has_header('content-type')

    assert response['content-disposition'] == 'attachment; filename=foo.pdf'
    assert int(response['content-length']) > 0
    assert response['content-type'] == 'application/pdf'


def test_html(client):
    """
    Test that the query string parameter ?html outputs HTML.
    """
    response = client.get('%s?html' % reverse('pdf'))
    with open(os.path.join(TESTS_TEMPLATE_DIR, 'basic.html'), 'rb') as basic_file:
        expected = basic_file.read()
    assert response.content == expected
