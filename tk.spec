Summary:	Tk GUI toolkit for Tcl, with shared libraries
Summary(de):	Tk GUI-Toolkit f�r Tcl mit gemeinsam genutzten Libraries
Summary(fr):	Boite � outil d'interfa�age graphique Tk pour Tcl avec librairies partag�es
Summary(pl):	Tk GUI narz�dzia dla Tcl wraz z bibliotekami dynamicznymi
Summary(ru):	Tk GUI toolkit ��� Tcl
Summary(tr):	Tk, Tcl i�in grafik kullan�c� arabirimi ara� tak�m�d�r
Summary(uk):	Tk GUI toolkit ��� Tcl
Name:		tk
%define major	8.4
Version:	%{major}.7
Release:	1
License:	BSD
Group:		Development/Languages/Tcl
Source0:	http://dl.sourceforge.net/tcl/%{name}%{version}-src.tar.gz
# Source0-md5:	b86b0db1c28723e6d3139e88250353a6
Patch0:		%{name}-ieee.patch
Patch1:		%{name}-manlnk.patch
Patch2:		%{name}-pil.patch
Patch3:		%{name}-headers_fix.patch
Patch4:		%{name}-opt_flags_pass_fix.patch
Patch5:		%{name}-ac253.patch
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

%description
Tk is a X Window widget set designed to work closely with the Tcl
scripting language. It allows you to write simple programs with full
featured GUI's in only a little more time then it takes to write a
text based interface. Tcl/Tk applications can also be run on Windows
and Macintosh platforms.

%description -l de
Tk ist ein Widget-Satz f�r X-Window f�r den Einsatz mit der Script
Sprache Tcl. Sie k�nnen einfache Programme mit voll funktionsf�higen
GUIs in fast genauso schnell schreiben, wie eine zeichenorientierte
Oberfl�che. Tcl/Tk-Anwendungen k�nnen auch auf Windows und
Macintosh-Plattformen ausgef�hrt werden.

%description -l fr
Tk est un ensemble de widgets X Window cr�e pour fonctionner avec le
langage de script Tcl. Il permet d'�crire des programmes simples avec
des fonctionnalit�s enti�rement interfac�es en � peine plus de temps
qu'avec interface texte. Les applications Tcl/Tk peuvent aussi
fonctionner sur des plateformes Windows ou Macintosh.

%description -l ja
Tk �� Tcl ������ץȸ����̩�ܤ�ư���褦�˥ǥ����󤵤줿 X Window
System �Υ��������åȥ��åȤǤ��� �ƥ����ȥ١����Υ��󥿡��ե�������
���Ѥ��Ƥ�Τǡ���������ħ���ä� GUI
�򾯤ʤ����֤ǡ���ñ�ʥץ����� ��ǽ񤯤��Ȥ��Ǥ��ޤ��� Tcl/Tk
���ץꥱ�������� Windows �� Macintosh
�Υץ�åȥե�����Ǽ¹Ԥ��뤳�Ȥ�Ǥ��ޤ���

%description -l pl
Tk jest zbiorem kontrolek X Window, przeznaczonym do pracy z j�zykiem
skryptowym Tcl. Pakiet ten pozwala na pisanie prostych program�w z
GUI.

%description -l ru
Tk - ��� ����� �������� ���������� ��� X Window, ��������������� ���
������ � ������������������ ������ Tcl. �� ��������� ������
����������� ��������� � ����������� ����������� ����������� �� �� ��
�����, ��� � ��������� ���������� ������. ��������� �� Tcl/Tk �����
����� �������� ��� Windows � Macintosh.

%description -l tr
Tk, Tcl betimleme dili ile birlikte kullan�lmak �zere tasarlanm�� bir
X Window aray�z eleman� k�mesidir. Tcl/Tk uygulamalar� MS-Windows ve
Macintosh ortamlar�nda da �al��t�r�labilir.

%description -l uk
Tk - �� ��¦� �������� ���ͦ��צ� ��� X Window, ����������� ���
������ � ��������������� ����� Tcl. ��� ������Ѥ ������ �����æ�Φ
�������� � ���Ʀ���� ����������� ��������� �� ��� �� ���, �� �
�������� ���������� ������. �������� �� Tcl/Tk ����� ������ ���������
Ц� Windoze �� Macintosh.

%package devel
Summary:	Tk GUI toolkit for Tcl header files and development documentation
Summary(pl):	Narz�dzia Tk GUI - pliki nag��wkowe i dokumentacja
Group:		Development/Languages/Tcl
Requires:	%{name} = %{version}-%{release}
Requires:	XFree86-devel
Requires:	tcl-devel >= %{version}

%description devel
Tk GUI toolkit for Tcl header files and development documentation.

%description devel -l pl
Narz�dzia Tk GUI - pliki nag��wkowe i dokumentacja.

%package demo
Summary:	Tk GUI toolkit for Tcl - demo programs
Summary(pl):	Narz�dzia Tk GUI - programy demonstracyjne
Group:		Development/Languages/Tcl
Requires:	%{name} = %{version}-%{release}

%description demo
Tk GUI toolkit for Tcl - demo programs.

%description demo -l pl
Narz�dzia Tk GUI - programy demonstracyjne.

%prep
%setup -q -n %{name}%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
#%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11

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
install -d $RPM_BUILD_ROOT{%{_mandir},%{_ulibdir}}

%{__make} -C unix install \
	INSTALL_ROOT=$RPM_BUILD_ROOT \
	MAN_INSTALL_DIR=$RPM_BUILD_ROOT%{_mandir}

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
%lang(eo) %{_ulibdir}/tk%{major}/msgs/eo.msg
%lang(es) %{_ulibdir}/tk%{major}/msgs/es.msg
%lang(fr) %{_ulibdir}/tk%{major}/msgs/fr.msg
%lang(it) %{_ulibdir}/tk%{major}/msgs/it.msg
%lang(nl) %{_ulibdir}/tk%{major}/msgs/nl.msg
%lang(pl) %{_ulibdir}/tk%{major}/msgs/pl.msg
%lang(ru) %{_ulibdir}/tk%{major}/msgs/ru.msg
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
