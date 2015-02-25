#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	A library for generating Enhanced Metafiles
Summary(pl.UTF-8):	Biblioteka do generowania plików w formacie Enhanced Metafile
Name:		libEMF
Version:	1.0.7
Release:	2
License:	LGPL v2.1+ (library), GPL v2+ (utility)
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libemf/%{name}-%{version}.tar.gz
# Source0-md5:	f1011f5cc254aa228be78704fe5f9960
Patch0:		%{name}-am.patch
Patch1:		%{name}-limits.patch
URL:		http://libemf.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libstdc++-devel >= 5:3.0
BuildRequires:	libtool >= 2:1.5
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
License:	LGPL v2.1+
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
License:	LGPL v2.1+
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
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
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
%attr(755,root,root) %{_bindir}/printemf
%attr(755,root,root) %{_libdir}/libEMF.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libEMF.so.1

%files devel
%defattr(644,root,root,755)
%doc doc/html
%attr(755,root,root) %{_libdir}/libEMF.so
%{_libdir}/libEMF.la
%{_includedir}/libEMF

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libEMF.a
%endif
