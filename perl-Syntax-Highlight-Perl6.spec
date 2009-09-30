%define upstream_name    Syntax-Highlight-Perl6
%define upstream_version 0.76

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

License:    GPL+ or Artistic
Group:      Development/Perl
Summary:    Perl 6 Syntax Highlighter
Source0:    http://www.cpan.org/modules/by-module/Syntax/%{upstream_name}-%{upstream_version}.tar.gz
Url:        http://search.cpan.org/dist/%{upstream_name}

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Moose)
BuildRequires: perl(Readonly)
BuildRequires: perl(Term::ANSIColor)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(YAML::Syck)
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}
Provides:   perl(STD)

%description
'Syntax::Highlight::Perl6' parses Perl 6 source code using an embedded
STD.pm. It matches parse tree nodes to colors then returns them in
different output formats. It can be used to create web pages with colorful
source code samples in its simple and snippet html modes, or it can be used
as a learning tool in examining STD.pm's output using the JavaScript node
viewer in its full html mode. Or you can use its parse tree Perl 5 records
to build your next great idea.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/bin/hilitep6
/usr/share/man/man1/*
