#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	File
%define		pnam	Find-Rule
Summary:	File::Find::Rule - alternative interface to File::Find
Summary(pl):	File::Find::Rule - alternatywny interfejs dla modu³u File::Find
Name:		perl-File-Find-Rule
Version:	0.28
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b12a6f02cb316ca62bd2411564606d1f
BuildRequires:	perl-Module-Build >= 0.20
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Number-Compare
BuildRequires:	perl(Test::More)
BuildRequires:	perl-Text-Glob
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::Find::Rule Perl module is a friendlier interface to File::Find.
It allows you to build rules which specify the desired files and
directories.

%description -l pl
Modu³ Perla File::Find::Rule stanowi bardziej przyjazny interfejs do
modu³u File::Find. Umo¿liwia on tworzenie regu³ okre¶laj±cych wymagane
pliki i katalogi.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	installdirs=vendor \
	perl="%{__perl}" \
	destdir=$RPM_BUILD_ROOT
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

# get rid of pod documentation
rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/File/Find/Rule/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%attr(755,root,root) %{_bindir}/findrule
%{perl_vendorlib}/File/Find
%{_mandir}/man1/*
%{_mandir}/man3/*
