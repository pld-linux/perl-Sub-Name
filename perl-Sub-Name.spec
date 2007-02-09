#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Sub
%define	pnam	Name
Summary:	Sub::Name - (re)name a sub
#Summary(pl):	
Name:		perl-Sub-Name
Version:	0.02
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Sub/Sub-Name-0.02.tar.gz
# Source0-md5:	a47e1f1fe88a0c85b7ecc0d150039616
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module has only one function, which is also exported by default:

Assigns a new name to referenced sub.  If package specification is
omitted in the name, then the current package is used.  The return
value is the sub.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
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
%{perl_vendorarch}/Sub/*.pm
%dir %{perl_vendorarch}/auto/Sub/Name
%attr(755,root,root) %{perl_vendorarch}/auto/Sub/Name/*.so
%{_mandir}/man3/*
