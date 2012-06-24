
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define		pdir	File
%define		pnam	Find-Rule
Summary:	File::Find::Rule - alternative interface to File::Find
Summary(pl):	File::Find::Rule - alternatywny interfejs dla modu�u File::Find
Name:		perl-File-Find-Rule
Version:	0.24
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f011b99c15277afc3d8f9b37ed237d10
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-Module-Build >= 0.20
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
Modu� Perla File::Find::Rule stanowi bardziej przyjazny interfejs do
modu�u File::Find. Umo�liwia on tworzenie regu� okre�laj�cych wymagane
pliki i katalogi.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	installdirs=vendor \
	destdir=$RPM_BUILD_ROOT
./Build
%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/File/Find
%{_mandir}/man3/*
