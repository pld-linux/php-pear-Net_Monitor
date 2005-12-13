%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	Monitor
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - remote service monitor
Summary(pl):	%{_pearname} - monitoring zdalnych us³ug
Name:		php-pear-%{_pearname}
Version:	0.2.3
Release:	3
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	d8caf1cf2a3a4390bf6123989ddba22b
URL:		http://pear.php.net/package/Net_Monitor/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-PEAR >= 1:1.0.0
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

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc docs/%{_pearname}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
