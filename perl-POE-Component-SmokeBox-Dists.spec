%define upstream_name    POE-Component-SmokeBox-Dists
%define upstream_version 1.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Search for CPAN distributions by cpanid or distribution name
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/POE/POE-Component-SmokeBox-Dists-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(CPAN::DistnameInfo)
BuildRequires: perl(Capture::Tiny)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Fetch)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(IO::Zlib)
BuildRequires:	perl(POE)
BuildRequires:	perl(Sort::Versions)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(URI)
Requires:	perl(CPAN::DistnameInfo)
Requires:	perl(Sort::Versions)
BuildArch:	noarch

%description
POE::Component::SmokeBox::Dists is a the POE manpage component that
provides non-blocking CPAN distribution searches. It is a wrapper around
the File::Fetch manpage for '02packages.details.txt.gz' file retrieval, the
IO::Zlib manpage for extraction and the CPAN::DistnameInfo manpage for
parsing the packages data.

Given either author ( ie. CPAN ID ) or distribution search criteria,
expressed as a regular expression, it will return to a requesting session
all the CPAN distributions that match that pattern.

The component will retrieve the '02packages.details.txt.gz' file to the
'.smokebox' directory. If that file already exists, a newer version will
only be retrieved if the file is older than 6 hours. Specifying the 'force'
parameter overrides this behaviour.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README LICENSE
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 24 2011 Funda Wang <fwang@mandriva.org> 1.40.0-5mdv2011.0
+ Revision: 658300
- rebuild

* Sun Apr 24 2011 Funda Wang <fwang@mandriva.org> 1.40.0-4
+ Revision: 658240
- more runtime req

* Sun Apr 24 2011 Funda Wang <fwang@mandriva.org> 1.40.0-3
+ Revision: 658231
- add runtime req

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.40.0-2
+ Revision: 657809
- rebuild for updated spec-helper

* Sun Dec 26 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.40.0-1mdv2011.0
+ Revision: 625280
- update to new version 1.04

* Sat Dec 25 2010 Shlomi Fish <shlomif@mandriva.org> 1.20.0-1mdv2011.0
+ Revision: 625063
- import perl-POE-Component-SmokeBox-Dists


