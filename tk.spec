Summary:	Tk GUI toolkit for Tcl, with shared libraries
Summary(de):	Tk GUI-Toolkit f�r Tcl mit gemeinsam genutzten Libraries
Summary(fr):	Boite � outil d'interfa�age graphique Tk pour Tcl avec librairies partag�es.
Summary(pl):	Tk GUI narz�dzia dla Tcl wraz z bibliotekami dynamicznymi
Summary(tr):	Tk, TCL i�in grafik kullan�c� arabirimi ara� tak�m�d�r
Group:		Development/Languages/Tcl
Group(pl):	Programowanie/J�zyki/Tcl
Name:		tk
Version:	8.0.5
Release:	1
Source0:	ftp://ftp.scriptics.com/pub/tcl/tcl8_0/%{name}%{version}.tar.gz
Patch0:		tk-ieee.patch
Patch1:		tk-nochecktcl.patch
BuildPrereq:	tcl
Copyright:	BSD
Icon:		tk.gif
Buildroot:	/tmp/%{name}-%{version}-root

%description
Tk is a X Windows widget set designed to work closely with the tcl scripting
language. It allows you to write simple programs with full featured GUI's in
only a little more time then it takes to write a text based interface.
Tcl/Tk applications can also be run on Windows and Macintosh platforms.

%description -l de
Tk ist ein Widget-Satz f�r X-Windows f�r den Einsatz mit der Script Sprache
tcl. Sie k�nnen einfache Programme mit voll funktionsf�higen GUIs in fast
genauso schnell schreiben, wie eine zeichenorientierte Oberfl�che.
Tcl/Tk-Anwendungen k�nnen auch auf Windows und Macintosh-Plattformen
ausgef�hrt werden.

%description -l fr
Tk est un ensemble de widgets X Window cr�e pour fonctionner avec le langage
de script Tcl. Il permet d'�crire des programmes simples avec des
fonctionnalit�s enti�rement interfac�es en � peine plus de temps qu'avec
interface texte. Les applications Tcl/Tk peuvent aussi fonctionner sur des
plateformes Windows ou Macintosh.

%description -l pl
Tk jest zbiorem kontrolek X Window, przeznaczonym do pracy z j�zykiem
skryptowym tcl. Pakiet ten pozwoli Ci na pisanie prostych program�w
z GUI.

%description -l tr
Tk, tcl betimleme dili ile birlikte kullan�lmak �zere tasarlanm�� bir X
Windows aray�z eleman� k�mesidir. Tcl/Tk uygulamalar� MS-Windows ve
Macintosh ortamlar�nda da �al��t�r�labilir.

%package devel
Summary:	Tk GUI toolkit for Tcl header files and development documentation
Summary(pl):	Narz�dzia Tk GUI - pliki nag��wkowe i dokumentacja
Group:		Development/Languages/Tcl
Group(pl):	Programowanie/J�zyki/Tcl
Requires:	%{name} = %{version}

%description devel
Tk GUI toolkit for Tcl header files and develppment documentation.

%description -l pl devel
Narz�dzia tk GUI - pliki nag��wkowe i dokumentacja.

%package demo
Summary:	Tk GUI toolkit for Tcl - demo programs
Summary(pl):	Narz�dzia Tk GUI - programy demostracjne
Group:		Development/Languages/Tcl
Group(pl):	Programowanie/J�zyki/Tcl
Requires:	%{name} = %{version}

%description demo
Tk GUI toolkit for Tcl - demo programs.

%description demo -l pl
Narz�dzia Tk GUI - programy demostracjne.

%prep
%setup -q -n %{name}%{version}
%patch0 -p1
%patch1 -p1 -b .nochecktcl
cd unix
autoconf

%build
cd unix
TCL_BIN_DIR=/usr/lib \
CFLAGS="$RPM_OPT_FLAGS -D_REENTRANT" LDFLAGS="-s" \
./configure \
	--prefix=/usr \
	--enable-shared \
	--enable-gcc
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr

cd unix
make INSTALL_ROOT=$RPM_BUILD_ROOT install
ln -sf libtk8.0.so $RPM_BUILD_ROOT/usr/lib/libtk.so
ln -sf wish8.0 $RPM_BUILD_ROOT/usr/bin/wish

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /usr/bin/*
%attr(755,root,root) /usr/lib/lib*.so
%dir /usr/lib/tk8.0
/usr/lib/tk8.0/*.tcl
/usr/man/man1/*

%files devel
%defattr(644,root,root,755)
/usr/include/*
/usr/lib/tkConfig.sh
/usr/man/man3/*
/usr/man/mann/*

%files demo
%defattr(-,root,root,755)
/usr/lib/tk8.0/demos

%changelog
* Tue Mar 23 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [8.0.5-1]
- added Group(pl),
- removed man group from man pages.

* Thu Oct 13 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [8.0.3-1]
- changed passing $RPM_OPT_FLAGS and added LDFLAGS,
- added demo subpackages,
- added "Requires: %%{name} = %%{version}" for devel,
- added missing files from /usr/lib/tk8.0 directory to main package,
- fixed pl translation.

* Mon Oct 05 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
- added pl translation,
- fixed man pages group,
- minor modifications of the spec file.

* Mon Aug 24 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [8.0p2-1]
- tk is now separated source package from orher tcl/tk stuff,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- fixed using $RPM_OPT_FLAGS during compile (curren tcl configure script don't
  accept passing CFLAGS in enviroment variable),
- added stripping shared libraries and wish binary,
- added devel subpackage,
- added URL,
- added package icon,
- updated Source Url to based on ftp://ftp.scriptics.com/,
- added %attr and %defattr macros in %files (allows build package from
  non-root account).

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sat May 02 1998 Cristian Gafton <gafton@redhat.com>
- fixed expect binaries exec permissions

* Thu Apr 09 1998 Erik Troan <ewt@redhat.com>
- updated to Tix 4.1.0.006
- updated version numbers of tcl/tk to relflect includsion of p2

* Wed Mar 25 1998 Cristian Gafton <gafton@redhat.com>
- updated tcl/tk to patch level 2
- updated tclX to 8.0.2

* Thu Oct 30 1997 Otto Hammersmith <otto@redhat.com>
- fixed filelist for tix... replacing path to the expect binary in scripts
  was leaving junk files around.

* Wed Oct 22 1997 Otto Hammersmith <otto@redhat.com>
- added patch to remove libieee test in configure.in for tcl and tk.
  Shoudln't be needed anymore for glibc systems, but this isn't the "proper" 
  solution for all systems
- fixed src urls

* Mon Oct 06 1997 Erik Troan <ewt@redhat.com>
- removed version numbers from descriptions

* Mon Sep 22 1997 Erik Troan <ewt@redhat.com>
- updated to tcl/tk 8.0 and related versions of packages

* Tue Jun 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc
- fixed dangling tclx/tkx symlinks
