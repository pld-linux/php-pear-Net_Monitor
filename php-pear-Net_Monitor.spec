%define		status		beta
%define		pearname	Net_Monitor
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - remote service monitor
Summary(pl.UTF-8):	%{pearname} - monitoring zdalnych usług
Name:		php-pear-%{pearname}
Version:	0.3.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	732ee641648110ff01a950955b101283
URL:		http://pear.php.net/package/Net_Monitor/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.654
Requires:	php-pear
Requires:	php-pear-PEAR-core >= 1:1.0.0
Suggests:	php-pear-HTTP_Request >= 1.2.4
Suggests:	php-pear-Mail >= 1.0.0
Suggests:	php-pear-Net_DNS >= 0.0.3
Suggests:	php-pear-Net_FTP >= 1.3.0-0.RC1
Suggests:	php-pear-Net_Growl
Suggests:	php-pear-Net_SMS >= 0.0.1
Suggests:	php-pear-Net_SMTP >= 1.2.2
Obsoletes:	php-pear-Net_Monitor-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq_pear HTTP/Request.* Mail.* Net/DNS.* Net/FTP.* Net/SMS.* Net/SMTP.* Net/Grow.*

%description
A unified interface for checking the availability services on external
servers and sending meaningful alerts through a variety of media if a
service becomes unavailable.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Zunifikowany interfejs do sprawdzania dostępności usług na zdalnych
serwerach oraz wysyłania komunikatów poprzez różnego rodzaju media w
przypadku braku dostępności danej usługi.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

mv .%{php_pear_dir}/data/Net_Monitor/* .
mv docs/%{pearname}/* .
mv doc/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%post -p <lua>
%pear_package_print_optionalpackages

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt install.log optional-packages.txt
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Net/Monitor.php
%{php_pear_dir}/Net/Monitor
