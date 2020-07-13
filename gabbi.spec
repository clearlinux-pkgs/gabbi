#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gabbi
Version  : 1.49.0
Release  : 73
URL      : https://files.pythonhosted.org/packages/63/d5/f74cb383df4397e96a7803fe5e2e7a3f39fbc51588d0a307d9179d1de9ac/gabbi-1.49.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/63/d5/f74cb383df4397e96a7803fe5e2e7a3f39fbc51588d0a307d9179d1de9ac/gabbi-1.49.0.tar.gz
Summary  : Declarative HTTP testing library
Group    : Development/Tools
License  : Apache-2.0
Requires: gabbi-bin = %{version}-%{release}
Requires: gabbi-license = %{version}-%{release}
Requires: gabbi-python = %{version}-%{release}
Requires: gabbi-python3 = %{version}-%{release}
Requires: PyYAML
Requires: certifi
Requires: colorama
Requires: jsonpath-rw-ext
Requires: pbr
Requires: six
Requires: testtools
Requires: urllib3
Requires: wsgi_intercept
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3
BuildRequires : certifi
BuildRequires : colorama
BuildRequires : jsonpath-rw-ext
BuildRequires : pbr
BuildRequires : pytest
BuildRequires : six
BuildRequires : testtools
BuildRequires : urllib3

%description
.. image:: https://travis-ci.org/cdent/gabbi.svg?branch=master
    :target: https://travis-ci.org/cdent/gabbi
.. image:: https://readthedocs.org/projects/gabbi/badge/?version=latest
    :target: https://gabbi.readthedocs.io/en/latest/
    :alt: Documentation Status

Gabbi
=====

`Release Notes`_

Gabbi is a tool for running HTTP tests where requests and responses
are represented in a declarative YAML-based form. The simplest test
looks like this::

    tests:
    - name: A test
      GET: /api/resources/id

See the docs_ for more details on the many features and formats for
setting request headers and bodies and evaluating responses.

Gabbi is tested with Python 2.7, 3.5, 3.6, 3.7 and pypy.

Tests can be run using `unittest`_ style test runners, `pytest`_
or from the command line with a `gabbi-run`_ script.

There is a `gabbi-demo`_ repository which provides a tutorial via
its commit history. The demo builds a simple API using gabbi to
facilitate test driven development.

.. _Release Notes: https://gabbi.readthedocs.io/en/latest/release.html
.. _docs: https://gabbi.readthedocs.io/
.. _gabbi-demo: https://github.com/cdent/gabbi-demo
.. _unittest: https://gabbi.readthedocs.io/en/latest/example.html#loader
.. _pytest: http://pytest.org/
.. _loader docs: https://gabbi.readthedocs.io/en/latest/example.html#pytest
.. _gabbi-run: https://gabbi.readthedocs.io/en/latest/runner.html

Purpose
-------

Gabbi works to bridge the gap between human readable YAML files that
represent HTTP requests and expected responses and the obscured realm of
Python-based, object-oriented unit tests in the style of the unittest
module and its derivatives.

Each YAML file represents an ordered list of HTTP requests along with
the expected responses. This allows a single file to represent a
process in the API being tested. For example:

* Create a resource.
* Retrieve a resource.
* Delete a resource.
* Retrieve a resource again to confirm it is gone.

At the same time it is still possible to ask gabbi to run just one
request. If it is in a sequence of tests, those tests prior to it in
the YAML file will be run (in order). In any single process any test
will only be run once. Concurrency is handled such that one file
runs in one process.

These features mean that it is possible to create tests that are
useful for both humans (as tools for improving and developing APIs)
and automated CI systems.

Testing and Developing Gabbi
----------------------------

To get started, after cloning the `repository`_, you should install the
development dependencies::

    $ pip install -r requirements-dev.txt

If you prefer to keep things isolated you can create a virtual
environment::

    $ virtualenv gabbi-venv
    $ . gabbi-venv/bin/activate
    $ pip install -r requirements-dev.txt

Gabbi is set up to be developed and tested using `tox`_ (installed via
``requirements-dev.txt``). To run the built-in tests (the YAML files
are in the directories ``gabbi/tests/gabbits_*`` and loaded by the file
``gabbi/test_*.py``), you call ``tox``::

    tox -epep8,py27,py34

If you have the dependencies installed (or a warmed up
virtualenv) you can run the tests by hand and exit on the first
failure::

    python -m subunit.run discover -f gabbi | subunit2pyunit

Testing can be limited to individual modules by specifying them
after the tox invocation::

    tox -epep8,py27,py34 -- test_driver test_handlers

If you wish to avoid running tests that connect to internet hosts,
set ``GABBI_SKIP_NETWORK`` to ``True``.

.. _tox: https://tox.readthedocs.io/
.. _repository: https://github.com/cdent/gabbi

%package bin
Summary: bin components for the gabbi package.
Group: Binaries
Requires: gabbi-license = %{version}-%{release}

%description bin
bin components for the gabbi package.


%package license
Summary: license components for the gabbi package.
Group: Default

%description license
license components for the gabbi package.


%package python
Summary: python components for the gabbi package.
Group: Default
Requires: gabbi-python3 = %{version}-%{release}

%description python
python components for the gabbi package.


%package python3
Summary: python3 components for the gabbi package.
Group: Default
Requires: python3-core
Provides: pypi(gabbi)

%description python3
python3 components for the gabbi package.


%prep
%setup -q -n gabbi-1.49.0
cd %{_builddir}/gabbi-1.49.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582925340
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test --verbose py2 ||:
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gabbi
cp %{_builddir}/gabbi-1.49.0/LICENSE %{buildroot}/usr/share/package-licenses/gabbi/25d94c813f78abc84a940a03bd9456307b85fb5c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gabbi-run

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gabbi/25d94c813f78abc84a940a03bd9456307b85fb5c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
