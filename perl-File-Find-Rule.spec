#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	File
%define		pnam	Find-Rule
Summary:	File::Find::Rule - alternative interface to File::Find
Summary(pl.UTF-8):	File::Find::Rule - alternatywny interfejs dla modułu File::Find
Name:		perl-File-Find-Rule
Version:	0.32
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/File/RCLAMP/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1b43810c6b8fd4ee5cee8046e1e05ff4
URL:		http://search.cpan.org/dist/File-Find-Rule/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Number-Compare
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-Text-Glob >= 0.07
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::Find::Rule Perl module is a friendlier interface to File::Find.
It allows you to build rules which specify the desired files and
directories.

%description -l pl.UTF-8
Moduł Perla File::Find::Rule stanowi bardziej przyjazny interfejs do
modułu File::Find. Umożliwia on tworzenie reguł określających wymagane
pliki i katalogi.

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

# get rid of pod documentation
%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/File/Find/Rule/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%attr(755,root,root) %{_bindir}/findrule
%dir %{perl_vendorlib}/File/Find
%{perl_vendorlib}/File/Find/Rule.pm
%{_mandir}/man1/findrule.1p*
%{_mandir}/man3/File::Find::Rule*.3pm*
