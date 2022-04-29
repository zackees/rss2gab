# rss2gab
Takes an RSS feed and auto posts to gab

There is 100% test coverage on this codebase. So if the unit tests pass on your platform then
the system will work correctly.

# Tests

Just simply run `tox` at the command line and everything should be tested. You may need to install `tox` with `python -m pip tox`.

# Building an app

 ```
 python -m nuitka --follow-imports  --standalone --onefile --include-plugin-directory=venv/lib/python3.10/site-packages/selenium --include-package-data sites/bigleague.py -o bigleague


 python -m nuitka --follow-imports --standalone --include-plugin-directory=venv/lib/python3.10/site-packages/selenium --include-data-dir --include-package-data=selenium sites/bigleague.py
 ```