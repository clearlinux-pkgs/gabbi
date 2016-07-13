#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gabbi
Version  : 1.24.0
Release  : 47
URL      : http://pypi.debian.net/gabbi/gabbi-1.24.0.tar.gz
Source0  : http://pypi.debian.net/gabbi/gabbi-1.24.0.tar.gz
Summary  : Declarative HTTP testing library
Group    : Development/Tools
License  : Apache-2.0
Requires: gabbi-bin
Requires: gabbi-python
BuildRequires : Babel-python
BuildRequires : Jinja2
BuildRequires : PyYAML
BuildRequires : Pygments
BuildRequires : Sphinx-python
BuildRequires : coverage-python
BuildRequires : docutils-python
BuildRequires : extras
BuildRequires : fixtures-python
BuildRequires : flake8-python
BuildRequires : gabbi
BuildRequires : hacking
BuildRequires : httplib2
BuildRequires : jsonpath-rw
BuildRequires : jsonpath-rw-ext-python
BuildRequires : linecache2-python
BuildRequires : markupsafe-python
BuildRequires : mccabe-python
BuildRequires : pbr
BuildRequires : pep8
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : ply-python
BuildRequires : py-python
BuildRequires : pycodestyle-python
BuildRequires : pyflakes-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-mimeparse
BuildRequires : python-mock
BuildRequires : python-mock-python
BuildRequires : python-subunit
BuildRequires : python3-dev
BuildRequires : pytz-python
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : testrepository
BuildRequires : testresources
BuildRequires : testscenarios
BuildRequires : testtools
BuildRequires : tox
BuildRequires : traceback2
BuildRequires : unittest2
BuildRequires : urllib3-python
BuildRequires : virtualenv
BuildRequires : wsgi_intercept
BuildRequires : wsgiref

%description
Some of the tests in this collection will attempt to connect to
google over the internet to validate some behaviors using real
socket connections. If this is not desirable (for example behind
firewalls or in packaging situations) set GABBI_SKIP_NETWORK to
true in the environment running the tests.

%package bin
Summary: bin components for the gabbi package.
Group: Binaries

%description bin
bin components for the gabbi package.


%package python
Summary: python components for the gabbi package.
Group: Default
Requires: jsonpath-rw-ext-python
Requires: six-python
Requires: urllib3-python

%description python
python components for the gabbi package.


%prep
%setup -q -n gabbi-1.24.0

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test --verbose py2 ||:
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gabbi-run

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
