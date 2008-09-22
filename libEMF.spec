#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	A library for generating Enhanced Metafiles
Summary(pl.UTF-8):	Biblioteka do generowania plików w formacie Enhanced Metafile
Name:		libEMF
Version:	1.0.3
Release:	1
License:	LGPL/GPL
Group:		Libraries
#Source0:	http://dl.sourceforge.net/libemf/%{name}-%{version}.tar.gz
Source0:	http://dl.sourceforge.net/pstoedit/%{name}-%{version}.tar.gz
# Source0-md5:	a4e91fd8077ce5f540f569e20e8ef7ff
Patch0:		%{name}-amd64.patch
Patch1:		%{name}-limits.patch
URL:		http://libemf.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libstdc++-devel >= 5:3.0
BuildRequires:	libtool >= 2:1.4d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libEMF is a library for generating Enhanced Metafiles on systems which
don't natively support the ECMA-234 Graphics Device Interface
(GDI). The library is intended to be used as a driver for other
graphics programs such as Grace or gnuplot. Therefore, it implements a
very limited subset of the GDI.

%description -l pl.UTF-8
libEMF to biblioteka do generowania plików w formacie Enhanced
Metafile na systemach nie obsługujących natywnie systemu graficznego
ECMA-234 GDI. Biblioteka ma służyć jako sterownik dla innych programów
graficznych, takich jak Grace czy gnuplot. Z tego powodu ma
zaimplementowany bardzo ograniczony podzbiór GDI.

%package devel
Summary:	libEMF header files
Summary(pl.UTF-8):	Pliki nagłówkowe libEMF
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
libEMF header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe libEMF.

%package static
Summary:	libEMF static library
Summary(pl.UTF-8):	Statyczna biblioteka libEMF
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
libEMF static library.

%description static -l pl.UTF-8
Statyczna biblioteka libEMF.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
# supplied libtool is broken (no C++ libraries support)
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-editing \
	%{!?with_static_libs:--disable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/html
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libEMF

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
