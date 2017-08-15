# Release 0.3.1 - Tue 15 Aug 2017 10:47:25 AEST

- Fixed package version number.

# Release 0.3.0 - Tue 15 Aug 2017 10:37:42 AEST

- Fix pylint 'no-else-return' linting issue.
- Change location of wkhtmltox - the old location seems to have disappeared.
- Fixes #7 - Added Django 1.11 and Python 3.6 support.
- Added args and kwargs to classview functions (#5)
- Added args and kwargs to classview functions which get passed through to get_context_data.
- Set the MEDIA_URL setting just like STATIC_URL is set.
- Now using dict rather than RequestContext for future Django support.

# Release 0.2.1 - Friday 28 October  14:13:32 AEDT 2016

- Fixed munge of django_pdfkit/__init__.py (#4)

# Release 0.2.0 - Friday 28 October 13:43:46 AEDT 2016

- Codecov integration (#3)
- Travis CI integration (#2)
- Now using WKHTMLTOPDF_BIN over class setting wkhtmltopdf_bin (#1)
- Added git-tools

# Release 0.1.0 - Thu Oct 27 16:50:04 EST 2016

- Initial release

