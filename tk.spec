Summary:	Tk GUI toolkit for Tcl, with shared libraries
Summary(de.UTF-8):	Tk GUI-Toolkit für Tcl mit gemeinsam genutzten Libraries
Summary(fr.UTF-8):	Boite à outil d'interfaçage graphique Tk pour Tcl avec librairies partagées
Summary(pl.UTF-8):	Tk GUI narzędzia dla Tcl wraz z bibliotekami dynamicznymi
Summary(ru.UTF-8):	Tk GUI toolkit для Tcl
Summary(tr.UTF-8):	Tk, Tcl için grafik kullanıcı arabirimi araç takımıdır
Summary(uk.UTF-8):	Tk GUI toolkit для Tcl
Name:		tk
%define		major	8.6
%define		minor	16
%define	tcl_ver	%{version}
Version:	%{major}.%{minor}
Release:	1
License:	BSD
Group:		Development/Languages/Tcl
Source0:	https://downloads.sourceforge.net/tcl/%{name}%{version}-src.tar.gz
# Source0-md5:	a7aad6cf52aa4687506a377a9a885a83
Patch0:		%{name}-manlnk.patch
Patch1:		%{name}-opt_flags_pass_fix.patch
Patch2:		%{name}-norpath.patch
Patch3:		%{name}-no_tcl_stub.patch
Patch4:		%{name}-soname_fix.patch
URL:		https://www.tcl-lang.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	pkgconfig
BuildRequires:	tcl-devel >= %{tcl_ver}
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel
Requires:	tcl >= %{tcl_ver}
Provides:	tile = 0.8.2
Obsoletes:	tile < 0.8.2-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ulibdir	%{_prefix}/lib
%define		specflags	-fno-strict-aliasing

%description
Tk is a X Window widget set designed to work closely with the Tcl
scripting language. It allows you to write simple programs with full
featured GUI's in only a little more time then it takes to write a
text based interface. Tcl/Tk applications can also be run on Windows
and Macintosh platforms.

%description -l de.UTF-8
Tk ist ein Widget-Satz für X-Window für den Einsatz mit der Script
Sprache Tcl. Sie können einfache Programme mit voll funktionsfähigen
GUIs in fast genauso schnell schreiben, wie eine zeichenorientierte
Oberfläche. Tcl/Tk-Anwendungen können auch auf Windows und
Macintosh-Plattformen ausgeführt werden.

%description -l fr.UTF-8
Tk est un ensemble de widgets X Window crée pour fonctionner avec le
langage de script Tcl. Il permet d'écrire des programmes simples avec
des fonctionnalités entiérement interfacées en à peine plus de temps
qu'avec interface texte. Les applications Tcl/Tk peuvent aussi
fonctionner sur des plateformes Windows ou Macintosh.

%description -l ja.UTF-8
Tk は Tcl スクリプト言語と密接に動作するようにデザインされた X Window
System のウィジェットセットです。 テキストベースのインターフェースを
採用してるので、あらゆる特徴をもった GUI
を少ない時間で、簡単なプログラ ムで書くことができます。 Tcl/Tk
アプリケーションは Windows や Macintosh
のプラットフォームで実行することもできます。

%description -l pl.UTF-8
Tk jest zbiorem kontrolek X Window, przeznaczonym do pracy z językiem
skryptowym Tcl. Pakiet ten pozwala na pisanie prostych programów z
GUI.

%description -l ru.UTF-8
Tk - это набор экранных примитивов для X Window, предназначенный для
работы с интерпретерируемым языком Tcl. Он позволяет писать
полноценные программы с графическим интерфейсом практически за то же
время, что и программы текстового режима. Программы на Tcl/Tk также
могут работать под Windows и Macintosh.

%description -l tr.UTF-8
Tk, Tcl betimleme dili ile birlikte kullanılmak üzere tasarlanmış bir
X Window arayüz elemanı kümesidir. Tcl/Tk uygulamaları MS-Windows ve
Macintosh ortamlarında da çalıştırılabilir.

%description -l uk.UTF-8
Tk - це набір екранних примітивів для X Window, призначений для роботи
з інтерпретованою мовою Tcl. Він дозволяє писати повноцінні програми з
графічним інтерфейсом практично за той же час, що і програми
текстового режиму. Програми на Tcl/Tk також можуть працювати під
Windoze та Macintosh.

%package devel
Summary:	Tk GUI toolkit for Tcl header files and development documentation
Summary(pl.UTF-8):	Narzędzia Tk GUI - pliki nagłówkowe i dokumentacja
Group:		Development/Languages/Tcl
Requires:	%{name} = %{version}-%{release}
Requires:	tcl-devel >= %{tcl_ver}
Requires:	xorg-lib-libXScrnSaver-devel
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXft-devel

%description devel
Tk GUI toolkit for Tcl header files and development documentation.

%description devel -l pl.UTF-8
Narzędzia Tk GUI - pliki nagłówkowe i dokumentacja.

%package demo
Summary:	Tk GUI toolkit for Tcl - demo programs
Summary(pl.UTF-8):	Narzędzia Tk GUI - programy demonstracyjne
Group:		Development/Languages/Tcl
Requires:	%{name} = %{version}-%{release}

%description demo
Tk GUI toolkit for Tcl - demo programs.

%description demo -l pl.UTF-8
Narzędzia Tk GUI - programy demonstracyjne.

%prep
%setup -q -n %{name}%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1

%build
cd unix
%{__autoconf}
TCL_BIN_DIR=%{_libdir}
%configure \
%if "%{_lib}" == "lib64"
	--enable-64bit \
%endif
	--disable-rpath \
	--enable-shared \
	--disable-symbols \
	--disable-threads \
	--enable-xft

%{__make}

%{__sed} -i \
	-e 's#%{_builddir}/%{name}%{version}/unix#%{_libdir}#' \
	-e 's#%{_builddir}/%{name}%{version}#%{_includedir}/%{name}-private#' \
	tkConfig.sh

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir},%{_ulibdir}}

%{__make} -C unix install \
	INSTALL_ROOT=$RPM_BUILD_ROOT \
	MAN_INSTALL_DIR=$RPM_BUILD_ROOT%{_mandir}

install -d $RPM_BUILD_ROOT%{_includedir}/%{name}-private/{generic/ttk,unix}
find generic unix -name "*.h" -exec cp -p '{}' $RPM_BUILD_ROOT%{_includedir}/%{name}-private/'{}' ';'
for h in $RPM_BUILD_ROOT%{_includedir}/*.h; do
	rh=$(basename "$h")
	if [ -f "$RPM_BUILD_ROOT%{_includedir}/%{name}-private/generic/$rh" ]; then
		ln -sf "../../$rh" $RPM_BUILD_ROOT%{_includedir}/%{name}-private/generic
	fi
done

ln -sf libtk%{major}.so.0.0 $RPM_BUILD_ROOT%{_libdir}/libtk.so
ln -sf libtk%{major}.so.0.0 $RPM_BUILD_ROOT%{_libdir}/libtk%{major}.so
ln -sf libtk%{major}.so.0.0 $RPM_BUILD_ROOT%{_libdir}/libtk%{major}.so.0
%{__mv} $RPM_BUILD_ROOT%{_bindir}/wish%{major} $RPM_BUILD_ROOT%{_bindir}/wish

if [ "%{_libdir}" != "%{_ulibdir}" ] ; then
	%{__mv} $RPM_BUILD_ROOT%{_libdir}/tkConfig.sh $RPM_BUILD_ROOT%{_ulibdir}
	%{__mv} $RPM_BUILD_ROOT%{_libdir}/tk%{major}/pkgIndex.tcl $RPM_BUILD_ROOT%{_ulibdir}/tk%{major}
fi

install generic/tkInt.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/wish
%attr(755,root,root) %{_libdir}/libtk%{major}.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libtk%{major}.so.0
%dir %{_ulibdir}/tk%{major}
%{_ulibdir}/tk%{major}/*.tcl
%{_ulibdir}/tk%{major}/tclIndex
%{_ulibdir}/tk%{major}/tkAppInit.c
%{_ulibdir}/tk%{major}/images
%dir %{_ulibdir}/tk%{major}/msgs
%lang(cs) %{_ulibdir}/tk%{major}/msgs/cs.msg
%lang(da) %{_ulibdir}/tk%{major}/msgs/da.msg
%lang(de) %{_ulibdir}/tk%{major}/msgs/de.msg
%lang(el) %{_ulibdir}/tk%{major}/msgs/el.msg
%{_ulibdir}/tk%{major}/msgs/en.msg
%lang(en_GB) %{_ulibdir}/tk%{major}/msgs/en_gb.msg
%lang(eo) %{_ulibdir}/tk%{major}/msgs/eo.msg
%lang(es) %{_ulibdir}/tk%{major}/msgs/es.msg
%lang(fi) %{_ulibdir}/tk%{major}/msgs/fi.msg
%lang(fr) %{_ulibdir}/tk%{major}/msgs/fr.msg
%lang(hu) %{_ulibdir}/tk%{major}/msgs/hu.msg
%lang(it) %{_ulibdir}/tk%{major}/msgs/it.msg
%lang(nl) %{_ulibdir}/tk%{major}/msgs/nl.msg
%lang(pl) %{_ulibdir}/tk%{major}/msgs/pl.msg
%lang(pt) %{_ulibdir}/tk%{major}/msgs/pt.msg
%lang(ru) %{_ulibdir}/tk%{major}/msgs/ru.msg
%lang(sv) %{_ulibdir}/tk%{major}/msgs/sv.msg
%lang(zh_CN) %{_ulibdir}/tk%{major}/msgs/zh_cn.msg
%{_ulibdir}/tk%{major}/ttk
%{_mandir}/man1/wish.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_ulibdir}/tkConfig.sh
%attr(755,root,root) %{_libdir}/libtk%{major}.so
%attr(755,root,root) %{_libdir}/libtk.so
%{_libdir}/libtkstub%{major}.a
%{_pkgconfigdir}/tk.pc
%{_includedir}/tk*.h
%{_includedir}/tk-private
%{_mandir}/man3/FindPhoto.3*
%{_mandir}/man3/FontId.3*
%{_mandir}/man3/MeasureChar.3*
%{_mandir}/man3/Tk_*.3*
%{_mandir}/man3/Ttk_*.3*
%{_mandir}/mann/*.n*

%files demo
%defattr(644,root,root,755)
%{_ulibdir}/tk%{major}/demos
