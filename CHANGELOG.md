Upcoming
------

**Backwards incompatible** for anything using multipart emails.

* `template_name` is now always plaintext.
* `text_template_name` has been replaced with `html_template_name` that points
  to an HTML template.

v1.0.0
------

**Backwards incompatible.**

* Remove hardly-used `get_manager_emails` method. If you need this, feel free to
  duplicate it from the previous version.
* Improve docs.
* Change how email headers are passed into `send()`. Now accepts `headers`
  dictionary rather than using the unused `kwargs`.
* Remove psql dependency for tests.
* Change many defaults from `()` to `None` in signature of `send`.

v0.3.0
------

* Add unit tests (100% coverage).
* Add and test support for Django 1.4.x and Python 3.

v0.2.0
------

* Remove implicit inclusion of the current site in send context
* Change argument name `extra_context` to `context`.

v0.1.2
------
* Use Django's `six` module to deal with unicode and strings and bytes.

v0.1.1
------
* Fixed typo in python3 compatibility

v0.1.0
------
* Initial release
