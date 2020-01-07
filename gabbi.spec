#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gabbi
Version  : 1.49.0
Release  : 71
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

%description python3
python3 components for the gabbi package.


%prep
%setup -q -n gabbi-1.49.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1569351343
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
cp LICENSE %{buildroot}/usr/share/package-licenses/gabbi/LICENSE
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
/usr/share/package-licenses/gabbi/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
