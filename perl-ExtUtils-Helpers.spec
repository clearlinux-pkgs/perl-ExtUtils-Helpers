#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-ExtUtils-Helpers
Version  : 0.026
Release  : 32
URL      : http://search.cpan.org/CPAN/authors/id/L/LE/LEONT/ExtUtils-Helpers-0.026.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/L/LE/LEONT/ExtUtils-Helpers-0.026.tar.gz
Summary  : 'Various portability utilities for module builders'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-ExtUtils-Helpers-license = %{version}-%{release}
Requires: perl-ExtUtils-Helpers-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This archive contains the distribution ExtUtils-Helpers,
version 0.026:
Various portability utilities for module builders

%package dev
Summary: dev components for the perl-ExtUtils-Helpers package.
Group: Development
Provides: perl-ExtUtils-Helpers-devel = %{version}-%{release}
Requires: perl-ExtUtils-Helpers = %{version}-%{release}

%description dev
dev components for the perl-ExtUtils-Helpers package.


%package license
Summary: license components for the perl-ExtUtils-Helpers package.
Group: Default

%description license
license components for the perl-ExtUtils-Helpers package.


%package perl
Summary: perl components for the perl-ExtUtils-Helpers package.
Group: Default
Requires: perl-ExtUtils-Helpers = %{version}-%{release}

%description perl
perl components for the perl-ExtUtils-Helpers package.


%prep
%setup -q -n ExtUtils-Helpers-0.026
cd %{_builddir}/ExtUtils-Helpers-0.026

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-ExtUtils-Helpers
cp %{_builddir}/ExtUtils-Helpers-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-ExtUtils-Helpers/8e000074722981ddbd70898e7f180a523d0b9219 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/ExtUtils::Helpers.3
/usr/share/man/man3/ExtUtils::Helpers::Unix.3
/usr/share/man/man3/ExtUtils::Helpers::VMS.3
/usr/share/man/man3/ExtUtils::Helpers::Windows.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-ExtUtils-Helpers/8e000074722981ddbd70898e7f180a523d0b9219

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
