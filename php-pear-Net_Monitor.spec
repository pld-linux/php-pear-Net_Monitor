%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	Monitor
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - remote service monitor
Summary(pl):	%{_pearname} - monitoring zdalnych us�ug
Name:		php-pear-%{_pearname}
Version:	0.0.7
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	634e1249be65ebb52101bebc1dfaa9e7
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
Zunifikowany interfejs do sprawdzania dost�pno�ci us�ug na zdalnych
serwerach oraz wysy�ania komunikat�w poprzez r�nego rodzaju media w
przypadku braku dost�pno�ci danej us�ugi.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/{Alert,Service}

cd %{_pearname}-%{version}
install %{_subclass}.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_subclass}/Alert/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Alert
install %{_subclass}/Service/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Service

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/examples
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
