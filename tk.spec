# TODO:
# - s/minor/major/ (I think it was the idea)???
%define minor 8.4
Summary:	Tk GUI toolkit for Tcl, with shared libraries
Summary(de):	Tk GUI-Toolkit für Tcl mit gemeinsam genutzten Libraries
Summary(fr):	Boite à outil d'interfaçage graphique Tk pour Tcl avec librairies partagées
Summary(pl):	Tk GUI narzêdzia dla Tcl wraz z bibliotekami dynamicznymi
Summary(ru):	Tk GUI toolkit ÄÌÑ Tcl
Summary(tr):	Tk, TCL için grafik kullanýcý arabirimi araç takýmýdýr
Summary(uk):	Tk GUI toolkit ÄÌÑ Tcl
Name:		tk
Version:	%{minor}.3
Release:	0.1
License:	BSD
Group:		Development/Languages/Tcl
Source0:	http://dl.sourceforge.net/tcl/%{name}%{version}-src.tar.gz
# Source0-md5:	e3ec11e314c9541b84e0415fbe9d947e
Patch0:		%{name}-ieee.patch
Patch1:		%{name}-manlnk.patch
Patch2:		%{name}-pil.patch
Patch3:		%{name}-headers_fix.patch
Patch4:		%{name}-opt_flags_pass_fix.patch
Patch5:		%{name}-ac253.patch
Patch6:		%{name}-soname_fix.patch
Icon:		tk.gif
URL:		http://www.tcl.tk/
BuildRequires:	autoconf
BuildRequires:	tcl-devel >= %{version}
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tk is a X Windows widget set designed to work closely with the tcl
scripting language. It allows you to write simple programs with full
featured GUI's in only a little more time then it takes to write a
text based interface. Tcl/Tk applications can also be run on Windows
and Macintosh platforms.

%description -l de
Tk ist ein Widget-Satz für X-Windows für den Einsatz mit der Script
Sprache tcl. Sie können einfache Programme mit voll funktionsfähigen
GUIs in fast genauso schnell schreiben, wie eine zeichenorientierte
Oberfläche. Tcl/Tk-Anwendungen können auch auf Windows und
Macintosh-Plattformen ausgeführt werden.

%description -l fr
Tk est un ensemble de widgets X Window crée pour fonctionner avec le
langage de script Tcl. Il permet d'écrire des programmes simples avec
des fonctionnalités entiérement interfacées en à peine plus de temps
qu'avec interface texte. Les applications Tcl/Tk peuvent aussi
fonctionner sur des plateformes Windows ou Macintosh.

%description -l ja
Tk ¤Ï tcl ¥¹¥¯¥ê¥×¥È¸À¸ì¤ÈÌ©ÀÜ¤ËÆ°ºî¤¹¤ë¤è¤¦¤Ë¥Ç¥¶¥¤¥ó¤µ¤ì¤¿ X Window
System ¤Î¥¦¥£¥¸¥§¥Ã¥È¥»¥Ã¥È¤Ç¤¹¡£ ¥Æ¥­¥¹¥È¥Ù¡¼¥¹¤Î¥¤¥ó¥¿¡¼¥Õ¥§¡¼¥¹¤ò
ºÎÍÑ¤·¤Æ¤ë¤Î¤Ç¡¢¤¢¤é¤æ¤ëÆÃÄ§¤ò¤â¤Ã¤¿ GUI
¤ò¾¯¤Ê¤¤»þ´Ö¤Ç¡¢´ÊÃ±¤Ê¥×¥í¥°¥é ¥à¤Ç½ñ¤¯¤³¤È¤¬¤Ç¤­¤Þ¤¹¡£Tcl/Tk
¥¢¥×¥ê¥±¡¼¥·¥ç¥ó¤Ï Windows ¤ä Macintosh
¤Î¥×¥é¥Ã¥È¥Õ¥©¡¼¥à¤Ç¼Â¹Ô¤¹¤ë¤³¤È¤â¤Ç¤­¤Þ¤¹¡£

%description -l pl
Tk jest zbiorem kontrolek X Window, przeznaczonym do pracy z jêzykiem
skryptowym tcl. Pakiet ten pozwala na pisanie prostych programów z
GUI.

%description -l ru
Tk - ÜÔÏ ÎÁÂÏÒ ÜËÒÁÎÎÙÈ ÐÒÉÍÉÔÉ×Ï× ÄÌÑ X Windows, ÐÒÅÄÎÁÚÎÁÞÅÎÎÙÊ ÄÌÑ
ÒÁÂÏÔÙ Ó ÉÎÔÅÒÐÒÅÔÅÒÉÒÕÅÍÙÍ ÑÚÙËÏÍ tcl. ïÎ ÐÏÚ×ÏÌÑÅÔ ÐÉÓÁÔØ
ÐÏÌÎÏÃÅÎÎÙÅ ÐÒÏÇÒÁÍÍÙ Ó ÇÒÁÆÉÞÅÓËÉÍ ÉÎÔÅÒÆÅÊÓÏÍ ÐÒÁËÔÉÞÅÓËÉ ÚÁ ÔÏ ÖÅ
×ÒÅÍÑ, ÞÔÏ É ÐÒÏÇÒÁÍÍÙ ÔÅËÓÔÏ×ÏÇÏ ÒÅÖÉÍÁ. ðÒÏÇÒÁÍÍÙ ÎÁ Tcl/Tk ÔÁËÖÅ
ÍÏÇÕÔ ÒÁÂÏÔÁÔØ ÐÏÄ Windows É Macintosh.

%description -l tr
Tk, tcl betimleme dili ile birlikte kullanýlmak üzere tasarlanmýþ bir
X Windows arayüz elemaný kümesidir. Tcl/Tk uygulamalarý MS-Windows ve
Macintosh ortamlarýnda da çalýþtýrýlabilir.

%description -l uk
Tk - ÃÅ ÎÁÂ¦Ò ÅËÒÁÎÎÉÈ ÐÒÉÍ¦ÔÉ×¦× ÄÌÑ X Windows, ÐÒÉÚÎÁÞÅÎÉÊ ÄÌÑ
ÒÏÂÏÔÉ Ú ¦ÎÔÅÒÐÒÅÔÏ×ÁÎÏÀ ÍÏ×ÏÀ tcl. ÷¦Î ÄÏÚ×ÏÌÑ¤ ÐÉÓÁÔÉ ÐÏ×ÎÏÃ¦ÎÎ¦
ÐÒÏÇÒÁÍÉ Ú ÇÒÁÆ¦ÞÎÉÍ ¦ÎÔÅÒÆÅÊÓÏÍ ÐÒÁËÔÉÞÎÏ ÚÁ ÔÏÊ ÖÅ ÞÁÓ, ÝÏ ¦
ÐÒÏÇÒÁÍÉ ÔÅËÓÔÏ×ÏÇÏ ÒÅÖÉÍÕ. ðÒÏÇÒÁÍÉ ÎÁ Tcl/Tk ÔÁËÏÖ ÍÏÖÕÔØ ÐÒÁÃÀ×ÁÔÉ
Ð¦Ä Windoze ÔÁ Macintosh.

%package devel
Summary:	Tk GUI toolkit for Tcl header files and development documentation
Summary(pl):	Narzêdzia Tk GUI - pliki nag³ówkowe i dokumentacja
Group:		Development/Languages/Tcl
Requires:	%{name} = %{version}
Requires:	tcl-devel
Requires:	XFree86-devel

%description devel
Tk GUI toolkit for Tcl header files and development documentation.

%description devel -l pl
Narzêdzia Tk GUI - pliki nag³ówkowe i dokumentacja.

%package demo
Summary:	Tk GUI toolkit for Tcl - demo programs
Summary(pl):	Narzêdzia Tk GUI - programy demonstracyjne
Group:		Development/Languages/Tcl
Requires:	%{name} = %{version}

%description demo
Tk GUI toolkit for Tcl - demo programs.

%description demo -l pl
Narzêdzia Tk GUI - programy demonstracyjne.

%prep
%setup -q -n %{name}%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
cd unix
%{__autoconf}
TCL_BIN_DIR=%{_libdir}
%configure \
	--disable-symbols \
	--enable-shared \
	--disable-threads \
	--enable-64bit \
	--enable-gcc

%{__make}

sed -e "s#%{_builddir}/%{name}%{version}/unix#%{_libdir}#; \
	s#%{_builddir}/%{name}%{version}#%{_includedir}#" tkConfig.sh > tkConfig.sh.new
mv -f tkConfig.sh.new tkConfig.sh

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}

cd unix
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT \
	MAN_INSTALL_DIR=$RPM_BUILD_ROOT%{_mandir}

ln -sf libtk%{minor}.so.0.0 $RPM_BUILD_ROOT%{_libdir}/libtk.so
ln -sf libtk%{minor}.so.0.0 $RPM_BUILD_ROOT%{_libdir}/libtk%{minor}.so
mv -f $RPM_BUILD_ROOT%{_bindir}/wish%{minor} $RPM_BUILD_ROOT%{_bindir}/wish

install ../generic/tkInt.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/tk%{minor}
%{_libdir}/tk%{minor}/*.tcl
%{_libdir}/tk%{minor}/tclIndex
%{_libdir}/tk%{minor}/tkAppInit.c
%dir %{_libdir}/tk%{minor}/msgs
%lang(cs) %{_libdir}/tk%{minor}/msgs/cs.msg
%lang(de) %{_libdir}/tk%{minor}/msgs/de.msg
%lang(el) %{_libdir}/tk%{minor}/msgs/el.msg
%{_libdir}/tk%{minor}/msgs/en.msg
%lang(en_GB) %{_libdir}/tk%{minor}/msgs/en_gb.msg
%lang(es) %{_libdir}/tk%{minor}/msgs/es.msg
%lang(fr) %{_libdir}/tk%{minor}/msgs/fr.msg
%lang(it) %{_libdir}/tk%{minor}/msgs/it.msg
%lang(nl) %{_libdir}/tk%{minor}/msgs/nl.msg
%lang(ru) %{_libdir}/tk%{minor}/msgs/ru.msg
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%attr(755,root,root) %{_libdir}/tkConfig.sh
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/libtkstub%{minor}.a
%{_mandir}/man3/*
%{_mandir}/mann/*

%files demo
%defattr(644,root,root,755)
%{_libdir}/tk%{minor}/demos
