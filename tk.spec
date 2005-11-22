Summary:	Tk GUI toolkit for Tcl, with shared libraries
Summary(de):	Tk GUI-Toolkit für Tcl mit gemeinsam genutzten Libraries
Summary(fr):	Boite à outil d'interfaçage graphique Tk pour Tcl avec librairies partagées
Summary(pl):	Tk GUI narzêdzia dla Tcl wraz z bibliotekami dynamicznymi
Summary(ru):	Tk GUI toolkit ÄÌÑ Tcl
Summary(tr):	Tk, Tcl için grafik kullanýcý arabirimi araç takýmýdýr
Summary(uk):	Tk GUI toolkit ÄÌÑ Tcl
Name:		tk
%define major	8.5
Version:	%{major}
%define	rel	a3
Release:	0.%{rel}.1
License:	BSD
Group:		Development/Languages/Tcl
Source0:	http://dl.sourceforge.net/tcl/%{name}%{version}%{rel}-src.tar.gz
# Source0-md5:	99c19b0547f637667f1101754cee2e8a
Patch0:		%{name}-ieee.patch
Patch1:		%{name}-manlnk.patch
Patch2:		%{name}-pil.patch
Patch4:		%{name}-opt_flags_pass_fix.patch
Patch6:		%{name}-soname_fix.patch
Patch7:		%{name}-norpath.patch
# http://www.tclsource.org/?page=tk
Patch8:		%{name}-aa-cairo.patch
Patch9:		%{name}-unix-scrollbars.patch
Patch10:	%{name}-unix-3d-borders.patch
Patch11:	%{name}-lib64.patch
Icon:		tk.gif
URL:		http://www.tcl.tk/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	tcl-devel >= %{version}
Requires:	tcl >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ulibdir	/usr/lib

%define		specflags	-fno-strict-aliasing

%description
Tk is a X Window widget set designed to work closely with the Tcl
scripting language. It allows you to write simple programs with full
featured GUI's in only a little more time then it takes to write a
text based interface. Tcl/Tk applications can also be run on Windows
and Macintosh platforms.

%description -l de
Tk ist ein Widget-Satz für X-Window für den Einsatz mit der Script
Sprache Tcl. Sie können einfache Programme mit voll funktionsfähigen
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
Tk ¤Ï Tcl ¥¹¥¯¥ê¥×¥È¸À¸ì¤ÈÌ©ÀÜ¤ËÆ°ºî¤¹¤ë¤è¤¦¤Ë¥Ç¥¶¥¤¥ó¤µ¤ì¤¿ X Window
System ¤Î¥¦¥£¥¸¥§¥Ã¥È¥»¥Ã¥È¤Ç¤¹¡£ ¥Æ¥­¥¹¥È¥Ù¡¼¥¹¤Î¥¤¥ó¥¿¡¼¥Õ¥§¡¼¥¹¤ò
ºÎÍÑ¤·¤Æ¤ë¤Î¤Ç¡¢¤¢¤é¤æ¤ëÆÃÄ§¤ò¤â¤Ã¤¿ GUI
¤ò¾¯¤Ê¤¤»þ´Ö¤Ç¡¢´ÊÃ±¤Ê¥×¥í¥°¥é ¥à¤Ç½ñ¤¯¤³¤È¤¬¤Ç¤­¤Þ¤¹¡£ Tcl/Tk
¥¢¥×¥ê¥±¡¼¥·¥ç¥ó¤Ï Windows ¤ä Macintosh
¤Î¥×¥é¥Ã¥È¥Õ¥©¡¼¥à¤Ç¼Â¹Ô¤¹¤ë¤³¤È¤â¤Ç¤­¤Þ¤¹¡£

%description -l pl
Tk jest zbiorem kontrolek X Window, przeznaczonym do pracy z jêzykiem
skryptowym Tcl. Pakiet ten pozwala na pisanie prostych programów z
GUI.

%description -l ru
Tk - ÜÔÏ ÎÁÂÏÒ ÜËÒÁÎÎÙÈ ÐÒÉÍÉÔÉ×Ï× ÄÌÑ X Window, ÐÒÅÄÎÁÚÎÁÞÅÎÎÙÊ ÄÌÑ
ÒÁÂÏÔÙ Ó ÉÎÔÅÒÐÒÅÔÅÒÉÒÕÅÍÙÍ ÑÚÙËÏÍ Tcl. ïÎ ÐÏÚ×ÏÌÑÅÔ ÐÉÓÁÔØ
ÐÏÌÎÏÃÅÎÎÙÅ ÐÒÏÇÒÁÍÍÙ Ó ÇÒÁÆÉÞÅÓËÉÍ ÉÎÔÅÒÆÅÊÓÏÍ ÐÒÁËÔÉÞÅÓËÉ ÚÁ ÔÏ ÖÅ
×ÒÅÍÑ, ÞÔÏ É ÐÒÏÇÒÁÍÍÙ ÔÅËÓÔÏ×ÏÇÏ ÒÅÖÉÍÁ. ðÒÏÇÒÁÍÍÙ ÎÁ Tcl/Tk ÔÁËÖÅ
ÍÏÇÕÔ ÒÁÂÏÔÁÔØ ÐÏÄ Windows É Macintosh.

%description -l tr
Tk, Tcl betimleme dili ile birlikte kullanýlmak üzere tasarlanmýþ bir
X Window arayüz elemaný kümesidir. Tcl/Tk uygulamalarý MS-Windows ve
Macintosh ortamlarýnda da çalýþtýrýlabilir.

%description -l uk
Tk - ÃÅ ÎÁÂ¦Ò ÅËÒÁÎÎÉÈ ÐÒÉÍ¦ÔÉ×¦× ÄÌÑ X Window, ÐÒÉÚÎÁÞÅÎÉÊ ÄÌÑ
ÒÏÂÏÔÉ Ú ¦ÎÔÅÒÐÒÅÔÏ×ÁÎÏÀ ÍÏ×ÏÀ Tcl. ÷¦Î ÄÏÚ×ÏÌÑ¤ ÐÉÓÁÔÉ ÐÏ×ÎÏÃ¦ÎÎ¦
ÐÒÏÇÒÁÍÉ Ú ÇÒÁÆ¦ÞÎÉÍ ¦ÎÔÅÒÆÅÊÓÏÍ ÐÒÁËÔÉÞÎÏ ÚÁ ÔÏÊ ÖÅ ÞÁÓ, ÝÏ ¦
ÐÒÏÇÒÁÍÉ ÔÅËÓÔÏ×ÏÇÏ ÒÅÖÉÍÕ. ðÒÏÇÒÁÍÉ ÎÁ Tcl/Tk ÔÁËÏÖ ÍÏÖÕÔØ ÐÒÁÃÀ×ÁÔÉ
Ð¦Ä Windoze ÔÁ Macintosh.

%package devel
Summary:	Tk GUI toolkit for Tcl header files and development documentation
Summary(pl):	Narzêdzia Tk GUI - pliki nag³ówkowe i dokumentacja
Group:		Development/Languages/Tcl
Requires:	%{name} = %{version}-%{release}
Requires:	XFree86-devel
Requires:	tcl-devel >= %{version}

%description devel
Tk GUI toolkit for Tcl header files and development documentation.

%description devel -l pl
Narzêdzia Tk GUI - pliki nag³ówkowe i dokumentacja.

%package demo
Summary:	Tk GUI toolkit for Tcl - demo programs
Summary(pl):	Narzêdzia Tk GUI - programy demonstracyjne
Group:		Development/Languages/Tcl
Requires:	%{name} = %{version}-%{release}

%description demo
Tk GUI toolkit for Tcl - demo programs.

%description demo -l pl
Narzêdzia Tk GUI - programy demonstracyjne.

%prep
%setup -q -n %{name}%{version}%{rel}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch4 -p1
%patch6 -p1
%patch7 -p1
#%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1

%build
cd unix
%{__autoconf}
TCL_BIN_DIR=%{_libdir}
%configure \
	--disable-symbols \
	--disable-threads \
	--enable-64bit \
	--enable-gcc \
	--enable-shared \
	--enable-xft

%{__make}

sed -i -e "s#%{_builddir}/%{name}%{version}%{rel}/unix#%{_libdir}#; \
	s#%{_builddir}/%{name}%{version}%{rel}#%{_includedir}/%{name}-private#" tkConfig.sh

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir},%{_ulibdir}}

%{__make} -C unix install \
	INSTALL_ROOT=$RPM_BUILD_ROOT \
	MAN_INSTALL_DIR=$RPM_BUILD_ROOT%{_mandir}

install -d $RPM_BUILD_ROOT%{_includedir}/%{name}-private/{generic,unix}
find generic unix -name "*.h" -exec cp -p '{}' $RPM_BUILD_ROOT%{_includedir}/%{name}-private/'{}' ';'
for h in $RPM_BUILD_ROOT%{_includedir}/*.h; do
        rh=$(basename "$h")
        if [ -f "$RPM_BUILD_ROOT%{_includedir}/%{name}-private/generic/$rh" ]; then
                ln -sf "../../$rh" $RPM_BUILD_ROOT%{_includedir}/%{name}-private/generic
        fi
done

ln -sf libtk%{major}.so.0.0 $RPM_BUILD_ROOT%{_libdir}/libtk.so
ln -sf libtk%{major}.so.0.0 $RPM_BUILD_ROOT%{_libdir}/libtk%{major}.so
mv -f $RPM_BUILD_ROOT%{_bindir}/wish%{major} $RPM_BUILD_ROOT%{_bindir}/wish

if [ "%{_libdir}" != "%{_ulibdir}" ] ; then
mv $RPM_BUILD_ROOT%{_libdir}/tk* $RPM_BUILD_ROOT%{_ulibdir}/
fi

install generic/tkInt.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_ulibdir}/tk%{major}
%{_ulibdir}/tk%{major}/*.tcl
%{_ulibdir}/tk%{major}/tclIndex
%{_ulibdir}/tk%{major}/tkAppInit.c
%{_ulibdir}/tk%{major}/prolog.ps
%{_ulibdir}/tk%{major}/images
%dir %{_ulibdir}/tk%{major}/msgs
%lang(cs) %{_ulibdir}/tk%{major}/msgs/cs.msg
%lang(de) %{_ulibdir}/tk%{major}/msgs/de.msg
%lang(el) %{_ulibdir}/tk%{major}/msgs/el.msg
%{_ulibdir}/tk%{major}/msgs/en.msg
%lang(en_GB) %{_ulibdir}/tk%{major}/msgs/en_gb.msg
%lang(es) %{_ulibdir}/tk%{major}/msgs/es_*.msg
%lang(eo) %{_ulibdir}/tk%{major}/msgs/eo.msg
%lang(es) %{_ulibdir}/tk%{major}/msgs/es.msg
%lang(fr) %{_ulibdir}/tk%{major}/msgs/fr.msg
%lang(it) %{_ulibdir}/tk%{major}/msgs/it.msg
%lang(nl) %{_ulibdir}/tk%{major}/msgs/nl.msg
%lang(pl) %{_ulibdir}/tk%{major}/msgs/pl.msg
%lang(ru) %{_ulibdir}/tk%{major}/msgs/ru.msg
%lang(sv) %{_ulibdir}/tk%{major}/msgs/sv.msg
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%attr(755,root,root) %{_ulibdir}/tkConfig.sh
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/libtkstub%{major}.a
%{_mandir}/man3/*
%{_mandir}/mann/*

%files demo
%defattr(644,root,root,755)
%{_ulibdir}/tk%{major}/demos
