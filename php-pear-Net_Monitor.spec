%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	Monitor
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - remote service monitor
Summary(pl):	%{_pearname} - monitoring zdalnych us³ug
Name:		php-pear-%{_pearname}
Version:	0.0.6
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	35e632b9e26d537ba503661f50c917c7
Patch0:		%{name}-path_fix.patch
URL:		http://pear.php.net/package/Net_Monitor/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A unified interface for checking the availability services on external
servers and sending meaningful alerts through a variety of media if a
service becomes unavailable.

In PEAR status of this package is: %{_status}.

%description -l pl
Zunifikowany interfejs do sprawdzania dostêpno¶ci us³ug na zdalnych
serwerach oraz wysy³ania komunikatów poprzez ró¿nego rodzaju media w
przypadku braku dostêpno¶ci danej us³ugi.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c
cd %{_pearname}-%{version}/%{_pearname}-%{version}
%patch0 -p0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/{Alert,Service}

cd %{_pearname}-%{version}/%{_pearname}-%{version}
install %{_subclass}.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_subclass}/Alert/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Alert
install %{_subclass}/Service/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Service

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/%{_pearname}-%{version}/examples
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
