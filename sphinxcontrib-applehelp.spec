#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x102C2C17498D6B9E (i.tkomiya@gmail.com)
#
Name     : sphinxcontrib-applehelp
Version  : 1.0.1
Release  : 8
URL      : https://files.pythonhosted.org/packages/1b/71/8bafa145e48131049dd4f731d6f6eeefe0c34c3017392adbec70171ad407/sphinxcontrib-applehelp-1.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/1b/71/8bafa145e48131049dd4f731d6f6eeefe0c34c3017392adbec70171ad407/sphinxcontrib-applehelp-1.0.1.tar.gz
Source1  : https://files.pythonhosted.org/packages/1b/71/8bafa145e48131049dd4f731d6f6eeefe0c34c3017392adbec70171ad407/sphinxcontrib-applehelp-1.0.1.tar.gz.asc
Summary  : No summary provided
Group    : Development/Tools
License  : BSD-2-Clause
Requires: sphinxcontrib-applehelp-license = %{version}-%{release}
Requires: sphinxcontrib-applehelp-python = %{version}-%{release}
Requires: sphinxcontrib-applehelp-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
sphinxcontrib-applehelp is a sphinx extension which outputs Apple help books

Home-page: http://sphinx-doc.org/
Author: Georg Brandl
Author-email: georg@python.org
License: BSD
Download-URL: https://pypi.org/project/sphinxcontrib-applehelp/
Description: 
        sphinxcontrib-applehelp is a sphinx extension which outputs Apple help books
        
Platform: any
Classifier: Development Status :: 5 - Production/Stable
Classifier: Environment :: Console
Classifier: Environment :: Web Environment
Classifier: Intended Audience :: Developers
Classifier: Intended Audience :: Education
Classifier: License :: OSI Approved :: BSD License
Classifier: Operating System :: OS Independent
Classifier: Programming Language :: Python
Classifier: Programming Language :: Python :: 3
Classifier: Programming Language :: Python :: 3.5
Classifier: Programming Language :: Python :: 3.6
Classifier: Programming Language :: Python :: 3.7
Classifier: Framework :: Sphinx
Classifier: Framework :: Sphinx :: Extension
Classifier: Topic :: Documentation
Classifier: Topic :: Documentation :: Sphinx
Classifier: Topic :: Text Processing
Classifier: Topic :: Utilities
Requires-Python: >=3.5
Provides-Extra: test

%package license
Summary: license components for the sphinxcontrib-applehelp package.
Group: Default

%description license
license components for the sphinxcontrib-applehelp package.


%package python
Summary: python components for the sphinxcontrib-applehelp package.
Group: Default
Requires: sphinxcontrib-applehelp-python3 = %{version}-%{release}

%description python
python components for the sphinxcontrib-applehelp package.


%package python3
Summary: python3 components for the sphinxcontrib-applehelp package.
Group: Default
Requires: python3-core
Provides: pypi(sphinxcontrib-applehelp)

%description python3
python3 components for the sphinxcontrib-applehelp package.


%prep
%setup -q -n sphinxcontrib-applehelp-1.0.1
cd %{_builddir}/sphinxcontrib-applehelp-1.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582920211
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sphinxcontrib-applehelp
cp %{_builddir}/sphinxcontrib-applehelp-1.0.1/LICENSE %{buildroot}/usr/share/package-licenses/sphinxcontrib-applehelp/50d2292390ae54694468ea4c35b53bb06a646e77
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sphinxcontrib-applehelp/50d2292390ae54694468ea4c35b53bb06a646e77

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
