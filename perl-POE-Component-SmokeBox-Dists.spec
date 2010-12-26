%define upstream_name    POE-Component-SmokeBox-Dists
%define upstream_version 1.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Search for CPAN distributions by cpanid or distribution name
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/POE/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(CPAN::DistnameInfo)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Fetch)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Spec)
BuildRequires: perl(IO::Zlib)
BuildRequires: perl(POE)
BuildRequires: perl(Sort::Versions)
BuildRequires: perl(Test::More)
BuildRequires: perl(URI)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README LICENSE
%{_mandir}/man3/*
%perl_vendorlib/*


