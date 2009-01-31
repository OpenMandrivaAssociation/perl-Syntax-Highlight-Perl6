
%define realname   Syntax-Highlight-Perl6
%define version    0.039
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Perl 6 Syntax Highlighter
Source:     http://www.cpan.org/modules/by-module/Syntax/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Moose)
BuildRequires: perl(Readonly)
BuildRequires: perl(Term::ANSIColor)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(YAML::Syck)

BuildArch: noarch

Provides: perl(STD)

%description
'Syntax::Highlight::Perl6' parses Perl 6 source code using an embedded
STD.pm. It matches parse tree nodes to colors then returns them in
different output formats. It can be used to create web pages with colorful
source code samples in its simple and snippet html modes, or it can be used
as a learning tool in examining STD.pm's output using the JavaScript node
viewer in its full html mode. Or you can use its parse tree Perl 5 records
to build your next great idea.

The available output formats are:

* *
      HTML (snippet,simple and full)

%prep
%setup -q -n %{realname}-%{version} 

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
/usr/share/man/man1/hilitep6.1.lzma

