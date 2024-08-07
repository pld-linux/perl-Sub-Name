#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define	pdir	Sub
%define	pnam	Name
Summary:	Sub::Name - (re)name a sub
Summary(pl.UTF-8):	Sub::Name - nazwanie/zmiana nazwy podprogramu
Name:		perl-Sub-Name
Version:	0.27
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Sub/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c7f7c5fce6f9a3575dc3ffdd519b3911
URL:		https://metacpan.org/dist/Sub-Name
BuildRequires:	perl-ExtUtils-MakeMaker
%if %{with tests}
BuildRequires:	perl(Exporter) >= 5.57
BuildRequires:	perl-Devel-CheckBin
BuildRequires:	perl-Test-Simple >= 0.88
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module has only one function, which is also exported by default:

Assigns a new name to referenced sub. If package specification is
omitted in the name, then the current package is used. The return
value is the sub.

%description -l pl.UTF-8
Ten moduł ma tylko jedną funkcję, eksportowaną domyślnie. Przypisuje
ona nową nazwę do wskazanego podprogramu. Jeśli specyfikacja pakietu
została pominięta w nazwie, użyty jest pakiet bieżący. Wartością
zwracaną jset podprogram.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

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
%{perl_vendorarch}/Sub/Name.pm
%dir %{perl_vendorarch}/auto/Sub/Name
%attr(755,root,root) %{perl_vendorarch}/auto/Sub/Name/Name.so
%{_mandir}/man3/Sub::Name.3pm*
