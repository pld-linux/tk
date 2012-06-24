Summary:	Tk GUI toolkit for Tcl, with shared libraries
Summary(de):	Tk GUI-Toolkit f�r Tcl mit gemeinsam genutzten Libraries
Summary(fr):	Boite � outil d'interfa�age graphique Tk pour Tcl avec librairies partag�es
Summary(pl):	Tk GUI narz�dzia dla Tcl wraz z bibliotekami dynamicznymi
Summary(tr):	Tk, TCL i�in grafik kullan�c� arabirimi ara� tak�m�d�r
Group:		Development/Languages/Tcl
Group(de):	Entwicklung/Sprachen/Tcl
Group(pl):	Programowanie/J�zyki/Tcl
Name:		tk
Version:	8.3.3
Release:	2
License:	BSD
Group:		Development/Languages/Tcl
Group(de):	Entwicklung/Sprachen/Tcl
Group(pl):	Programowanie/J�zyki/Tcl
Source0:	ftp://ftp.scriptics.com/pub/tcl/tcl8_3/%{name}%{version}.tar.gz
Patch0:		%{name}-ieee.patch
Patch1:		%{name}-manlnk.patch
Patch2:		%{name}-pil.patch
Patch3:		%{name}-headers_fix.patch
Patch4:		%{name}-opt_flags_pass_fix.patch
Icon:		tk.gif
BuildRequires:	autoconf
BuildRequires:	tcl-devel >= 8.3.2
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tk is a X Windows widget set designed to work closely with the tcl
scripting language. It allows you to write simple programs with full
featured GUI's in only a little more time then it takes to write a
text based interface. Tcl/Tk applications can also be run on Windows
and Macintosh platforms.

%description -l de
Tk ist ein Widget-Satz f�r X-Windows f�r den Einsatz mit der Script
Sprache tcl. Sie k�nnen einfache Programme mit voll funktionsf�higen
GUIs in fast genauso schnell schreiben, wie eine zeichenorientierte
Oberfl�che. Tcl/Tk-Anwendungen k�nnen auch auf Windows und
Macintosh-Plattformen ausgef�hrt werden.

%description -l fr
Tk est un ensemble de widgets X Window cr�e pour fonctionner avec le
langage de script Tcl. Il permet d'�crire des programmes simples avec
des fonctionnalit�s enti�rement interfac�es en � peine plus de temps
qu'avec interface texte. Les applications Tcl/Tk peuvent aussi
fonctionner sur des plateformes Windows ou Macintosh.

%description -l pl
Tk jest zbiorem kontrolek X Window, przeznaczonym do pracy z j�zykiem
skryptowym tcl. Pakiet ten pozwoli Ci na pisanie prostych program�w z
GUI.

%description -l tr
Tk, tcl betimleme dili ile birlikte kullan�lmak �zere tasarlanm�� bir
X Windows aray�z eleman� k�mesidir. Tcl/Tk uygulamalar� MS-Windows ve
Macintosh ortamlar�nda da �al��t�r�labilir.

%package devel
Summary:	Tk GUI toolkit for Tcl header files and development documentation
Summary(pl):	Narz�dzia Tk GUI - pliki nag��wkowe i dokumentacja
Group:		Development/Languages/Tcl
Group(de):	Entwicklung/Sprachen/Tcl
Group(pl):	Programowanie/J�zyki/Tcl
Requires:	%{name} = %{version}
Requires:	tcl-devel
Requires:	XFree86-devel

%description devel
Tk GUI toolkit for Tcl header files and develppment documentation.

%description -l pl devel
Narz�dzia tk GUI - pliki nag��wkowe i dokumentacja.

%package demo
Summary:	Tk GUI toolkit for Tcl - demo programs
Summary(pl):	Narz�dzia Tk GUI - programy demostracjne
Group:		Development/Languages/Tcl
Group(de):	Entwicklung/Sprachen/Tcl
Group(pl):	Programowanie/J�zyki/Tcl
Requires:	%{name} = %{version}

%description demo
Tk GUI toolkit for Tcl - demo programs.

%description demo -l pl
Narz�dzia Tk GUI - programy demostracjne.

%prep
%setup -q -n %{name}%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
cd unix
autoconf
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

ln -sf libtk8.3.so $RPM_BUILD_ROOT%{_libdir}/libtk.so
mv -f $RPM_BUILD_ROOT%{_bindir}/wish8.3 $RPM_BUILD_ROOT%{_bindir}/wish

install ../generic/tkInt.h $RPM_BUILD_ROOT%{_includedir}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%dir %{_libdir}/tk8.3
%{_libdir}/tk8.3/*.tcl
%{_libdir}/tk8.3/tclIndex
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%attr(755,root,root) %{_libdir}/tkConfig.sh
%{_libdir}/libtkstub8.3.a
%{_mandir}/man3/*
%{_mandir}/mann/*

%files demo
%defattr(644,root,root,755)
%{_libdir}/tk8.3/demos
