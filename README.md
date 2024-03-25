# Puterthon
Brython ported to run as a Puter app, along with some Puter specific modules.

In order to make this function, you will also need to download a release of Brython for the
deployment from [Brython Repo](https://github.com/brython-dev/brython) and unzip the release
into the app directory before deployment in Puter.  You cannot use the CDN version of Brython
if local modules such as `puter.py` are to be used, as it will only check the CDN when using
the Python `import` statement.
