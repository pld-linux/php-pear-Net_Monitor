%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	Monitor
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - remote service monitor
Summary(pl.UTF-8):	%{_pearname} - monitoring zdalnych usług
Name:		php-pear-%{_pearname}
Version:	0.2.4
Release:	3
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	5c629937bf594d5ee9bce146c65f09b9
URL:		http://pear.php.net/package/Net_Monitor/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-PEAR-core >= 1:1.0.0
Suggests:	php-pear-HTTP_Request >= 1.2.4
Suggests:	php-pear-Mail >= 1.0.0
Suggests:	php-pear-Net_DNS >= 0.0.3
Suggests:	php-pear-Net_FTP >= 1.3.0-0.RC1
Suggests:	php-pear-Net_SMS >= 0.0.1
Suggests:	php-pear-Net_SMTP >= 1.2.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	pear(HTTP/Request.*) pear(Mail.*) pear(Net/DNS.*) pear(Net/FTP.*) pear(Net/SMS.*) pear(Net/SMTP.*)

%description
A unified interface for checking the availability services on external
servers and sending meaningful alerts through a variety of media if a
service becomes unavailable.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Zunifikowany interfejs do sprawdzania dostępności usług na zdalnych
serwerach oraz wysyłania komunikatów poprzez różnego rodzaju media w
przypadku braku dostępności danej usługi.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoProv:	no
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
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
