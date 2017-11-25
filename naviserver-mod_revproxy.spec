#
# spec file for package naviserver revproxy module
#

Summary:        NaviServer revproxy module
Name:           naviserver-mod_revproxy
Version:        0.9
Release:        0
License:        MPL-1.1
Group:          Productivity/Networking/Web/Servers
Url:            http://bitbucket.org/naviserver/revproxy
BuildRequires:  make
BuildRequires:  naviserver
BuildRequires:  naviserver-devel
Requires:       nsf
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This is a NaviServer module that implements a reverse proxy for
NaviServer based on the ns_connchan command. The modules provides
NaviServer filter procs, which can be registered for all or selected
urls via wildcards, that will redirect the incoming requests to some
backend service.

%prep
%setup -q %{name}-%{version}

%build

%install
mkdir -p %buildroot/var/lib/naviserver/tcl/revproxy
make DESTDIR=%buildroot install NAVISERVER=/var/lib/naviserver

%clean
rm -rf %buildroot

%files
%defattr(-,nsadmin,nsadmin,-)
/var/lib/naviserver/tcl/revproxy

%changelog

