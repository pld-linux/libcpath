Summary:	Library to support cross-platform C path functions
Summary(pl.UTF-8):	Biblioteka wspierająca wieloplatformowe funkcje obsługi ścieżek w C
Name:		libcpath
Version:	20150101
Release:	1
License:	LGPL v3+
Group:		Libraries
Source0:	https://github.com/libyal/libcpath/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	3f2d6b40bf36cea61aec4f31a8ac82e2
Patch0:		%{name}-system-libs.patch
URL:		https://github.com/libyal/libcpath/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.18.1
BuildRequires:	libcerror-devel >= 20120425
BuildRequires:	libclocale-devel >= 20120425
BuildRequires:	libcsplit-devel >= 20120701
BuildRequires:	libcstring-devel >= 20120425
BuildRequires:	libuna-devel >= 20120425
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Requires:	libcerror >= 20120425
Requires:	libclocale >= 20120425
Requires:	libcsplit >= 20120701
Requires:	libcstring >= 20120425
Requires:	libuna >= 20120425
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
Requires:	libcerror-devel >= 20120425
Requires:	libclocale-devel >= 20120425
Requires:	libcsplit-devel >= 20120701
Requires:	libcstring-devel >= 20120425
Requires:	libuna-devel >= 20120425

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
%patch0 -p1

%build
%{__gettextize}
%{__sed} -i -e 's/ po\/Makefile.in//' configure.ac
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
