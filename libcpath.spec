# see m4/${libname}.m4 />= for required version of particular library
%define		libcerror_ver	20120425
%define		libclocale_ver	20120425
%define		libcsplit_ver	20120701
%define		libuna_ver	20230702
Summary:	Library to support cross-platform C path functions
Summary(pl.UTF-8):	Biblioteka wspierająca wieloplatformowe funkcje obsługi ścieżek w C
Name:		libcpath
Version:	20240414
Release:	1
License:	LGPL v3+
Group:		Libraries
#Source0Download: https://github.com/libyal/libcpath/releases
Source0:	https://github.com/libyal/libcpath/releases/download/%{version}/%{name}-alpha-%{version}.tar.gz
# Source0-md5:	5e2f1641504802425968b5d2e894a19d
URL:		https://github.com/libyal/libcpath/
BuildRequires:	autoconf >= 2.71
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.21
BuildRequires:	libcerror-devel >= %{libcerror_ver}
BuildRequires:	libclocale-devel >= %{libclocale_ver}
BuildRequires:	libcsplit-devel >= %{libcsplit_ver}
BuildRequires:	libuna-devel >= %{libuna_ver}
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
Requires:	libcerror >= %{libcerror_ver}
Requires:	libclocale >= %{libclocale_ver}
Requires:	libcsplit >= %{libcsplit_ver}
Requires:	libuna >= %{libuna_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libcpath is a library to support cross-platform C path functions.

%description -l pl.UTF-8
libcpath to biblioteka wspierająca wieloplatformowe funkcje obsługi
ścieżek w C.

%package devel
Summary:	Header files for libcpath library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libcpath
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libcerror-devel >= %{libcerror_ver}
Requires:	libclocale-devel >= %{libclocale_ver}
Requires:	libcsplit-devel >= %{libcsplit_ver}
Requires:	libuna-devel >= %{libuna_ver}

%description devel
Header files for libcpath library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libcpath.

%package static
Summary:	Static libcpath library
Summary(pl.UTF-8):	Statyczna biblioteka libcpath
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libcpath library.

%description static -l pl.UTF-8
Statyczna biblioteka libcpath.

%prep
%setup -q

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libcpath.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libcpath.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcpath.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcpath.so
%{_includedir}/libcpath
%{_includedir}/libcpath.h
%{_pkgconfigdir}/libcpath.pc
%{_mandir}/man3/libcpath.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libcpath.a
