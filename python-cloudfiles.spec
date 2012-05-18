%define name python-cloudfiles
%define version 1.7.10
%define unmangled_version 1.7.10
%define unmangled_version 1.7.10
%define release 1

Summary: CloudFiles client library for Python
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRequires:  python-devel python-setuptools python-sphinx make
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Rackspace <please_report_on_github@rackspace.com>
Url: https://github.com/rackspace/python-cloudfiles

%description
UNKNOWN

%prep
%setup -n %{name}-%{unmangled_version} -n %{name}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
