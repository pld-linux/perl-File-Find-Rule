#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	File
%define		pnam	Find-Rule
Summary:	File::Find::Rule - alternative interface to File::Find
Summary(pl):	File::Find::Rule - alternatywny interfejs dla modu�u File::Find
Name:		perl-File-Find-Rule
Version:	0.04
Release:	3
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-Text-Glob
%endif
BuildRequires:	rpm-perlprov >= 3.0.3-26
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
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_sitelib}/File/Find
%{_mandir}/man3/*
