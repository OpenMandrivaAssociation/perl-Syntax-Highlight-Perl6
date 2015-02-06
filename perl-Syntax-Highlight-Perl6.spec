%define upstream_name    Syntax-Highlight-Perl6
%define upstream_version 0.88

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

License:	GPL+ or Artistic
Group:		Development/Perl
Summary:	Perl 6 Syntax Highlighter
Source0:	http://www.cpan.org/modules/by-module/Syntax/%{upstream_name}-%{upstream_version}.tar.gz
Url:		http://search.cpan.org/dist/%{upstream_name}

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::ShareDir)
BuildRequires:	perl(File::ShareDir::Install)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Readonly)
BuildRequires:	perl(Term::ANSIColor)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(YAML::Syck)
BuildRequires:	perl(YAML::XS)
BuildRequires:	perl-STD
BuildArch:	noarch
Provides:	perl(STD)

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/*
%{_bindir}/hilitep6
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.880.0-2mdv2011.0
+ Revision: 657837
- rebuild for updated spec-helper

* Thu Feb 03 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.880.0-1
+ Revision: 635624
- update to new version 0.88

* Sat Aug 28 2010 Jérôme Quelin <jquelin@mandriva.org> 0.840.0-1mdv2011.0
+ Revision: 573859
- adding missing buildrequires:
- update to 0.84

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.810.0-1mdv2011.0
+ Revision: 552635
- update to 0.81

* Fri Mar 26 2010 Jérôme Quelin <jquelin@mandriva.org> 0.800.0-1mdv2010.1
+ Revision: 527739
- update to 0.80

* Thu Feb 25 2010 Jérôme Quelin <jquelin@mandriva.org> 0.790.0-1mdv2010.1
+ Revision: 510975
- update to 0.79

* Sun Jan 10 2010 Jérôme Quelin <jquelin@mandriva.org> 0.780.0-1mdv2010.1
+ Revision: 488852
- update to 0.78

* Mon Dec 14 2009 Jérôme Quelin <jquelin@mandriva.org> 0.770.0-1mdv2010.1
+ Revision: 478528
- adding missing buildrequires:
- update to 0.77

* Wed Sep 30 2009 Jérôme Quelin <jquelin@mandriva.org> 0.760.0-1mdv2010.0
+ Revision: 451153
- update to 0.76

* Sun Sep 20 2009 Jérôme Quelin <jquelin@mandriva.org> 0.750.0-1mdv2010.0
+ Revision: 444838
- update to 0.75

* Fri Sep 18 2009 Jérôme Quelin <jquelin@mandriva.org> 0.740.0-1mdv2010.0
+ Revision: 444315
- update to 0.74

* Wed Sep 09 2009 Jérôme Quelin <jquelin@mandriva.org> 0.730.0-1mdv2010.0
+ Revision: 435704
- update to 0.73

* Thu Aug 20 2009 Jérôme Quelin <jquelin@mandriva.org> 0.720.0-1mdv2010.0
+ Revision: 418631
- update to 0.72

* Sun Aug 16 2009 Jérôme Quelin <jquelin@mandriva.org> 0.710.0-1mdv2010.0
+ Revision: 416985
- update to 0.71

* Tue Aug 11 2009 Jérôme Quelin <jquelin@mandriva.org> 0.690.0-1mdv2010.0
+ Revision: 414983
- update to 0.69

* Thu Aug 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.670.0-1mdv2010.0
+ Revision: 410634
- update to 0.67

* Thu Jul 23 2009 Jérôme Quelin <jquelin@mandriva.org> 0.650.0-1mdv2010.0
+ Revision: 398940
- update to 0.65

* Mon Jul 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.640.0-1mdv2010.0
+ Revision: 392716
- update to 0.64

* Sat May 30 2009 Jérôme Quelin <jquelin@mandriva.org> 0.580.0-1mdv2010.0
+ Revision: 381273
- really use %%perl_convert_version
- update to 0.58
- using %%perl_convert_version
- sanitized license tag
- cleaned description field

* Thu May 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.57-1mdv2010.0
+ Revision: 378238
- update to new version 0.57

* Wed May 20 2009 Jérôme Quelin <jquelin@mandriva.org> 0.56-1mdv2010.0
+ Revision: 378033
- update to new version 0.56

* Tue May 12 2009 Jérôme Quelin <jquelin@mandriva.org> 0.55-1mdv2010.0
+ Revision: 374886
- update to new version 0.55

* Mon May 11 2009 Jérôme Quelin <jquelin@mandriva.org> 0.54-1mdv2010.0
+ Revision: 374141
- updating list of provided files
- update to new version 0.54

* Wed May 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.52-1mdv2010.0
+ Revision: 372637
- update to new version 0.52

* Wed May 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.51-1mdv2010.0
+ Revision: 372380
- update to new version 0.51

* Tue May 05 2009 Jérôme Quelin <jquelin@mandriva.org> 0.50-1mdv2010.0
+ Revision: 372113
- update to new version 0.50

* Sun May 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.49-1mdv2010.0
+ Revision: 371353
- update to new version 0.49

* Fri May 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.48-1mdv2010.0
+ Revision: 369789
- update to new version 0.48

* Thu Feb 05 2009 Jérôme Quelin <jquelin@mandriva.org> 0.040-1mdv2009.1
+ Revision: 337755
- update to new version 0.040

* Sat Jan 31 2009 Jérôme Quelin <jquelin@mandriva.org> 0.039-1mdv2009.1
+ Revision: 335707
- update to new version 0.039

* Thu Jan 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.038-1mdv2009.1
+ Revision: 335171
- update to new version 0.038

* Mon Jan 26 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.035-1mdv2009.1
+ Revision: 333642
- update to new version 0.035

* Sun Jan 18 2009 Jérôme Quelin <jquelin@mandriva.org> 0.034-1mdv2009.1
+ Revision: 330874
- update to new version 0.034

* Wed Jan 14 2009 Jérôme Quelin <jquelin@mandriva.org> 0.033-1mdv2009.1
+ Revision: 329395
- update to new version 0.033

* Tue Jan 13 2009 Jérôme Quelin <jquelin@mandriva.org> 0.032-2mdv2009.1
+ Revision: 329139
- and for once, i didn't forget to bump mkrel
- adding provided module not detected (of course, it's a .pmc)

* Tue Jan 13 2009 Jérôme Quelin <jquelin@mandriva.org> 0.032-1mdv2009.1
+ Revision: 329115
- missing build require
- import perl-Syntax-Highlight-Perl6


* Tue Jan 13 2009 cpan2dist 0.032-1mdv
- initial mdv release, generated with cpan2dist

