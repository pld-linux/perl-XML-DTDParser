#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	DTDParser
Summary:	XML::DTDParser - quick and dirty DTD parser
Summary(pl):	XML::DTDParser - szybko i brzydko napisany parser DTD
Name:		perl-XML-DTDParser
Version:	1.7
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	11929b44fe75012fd4f991c412855081
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module parses a DTD file and creates a data structure containing
info about all tags, their allowed parameters, children, parents,
optionality etc. etc. etc.

%description -l pl
Ten modu³ analizuje plik DTD i tworzy strukturê danych zawieraj±c±
informacje o wszystkich znacznikach, ich dozwolonych parametrach,
potomkach, rodzicach, opcjonalno¶ci itp. itd.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/XML/DTDParser.pm
%{_mandir}/man3/*
