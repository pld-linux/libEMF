Summary:	A library for generating Enhanced Metafiles
Summary(pl):	Biblioteka do generowania plików w formacie Enhanced Metafile
Name:		libEMF
Version:	1.0
Release:	1
License:	LGPL/GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/libemf/%{name}-%{version}.tar.gz
Patch0:		%{name}-gcc3.patch
URL:		http://libemf.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libEMF is a library for generating Enhanced Metafiles on systems which
don't natively support the ECMA-234 Graphics Device Interface
(GDI). The library is intended to be used as a driver for other
graphics programs such as Grace or gnuplot. Therefore, it implements a
very limited subset of the GDI.

%description -l pl
libEMF to biblioteka do generowania plików w formacie Enhanced
Metafile na systemach nie obs³uguj±cych natywnie systemu graficznego
ECMA-234 GDI. Biblioteka ma s³u¿yæ jako sterownik dla innych programów
graficznych, takich jak Grace czy gnuplot. Z tego powodu ma
zaimplementowany bardzo ograniczony podzbiór GDI.

%package devel
Summary:	libEMF header files
Summary(pl):	Pliki nag³ówkowe libEMF
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	libstdc++-devel

%description devel
libEMF header files.

%description devel -l pl
Pliki nag³ówkowe libEMF.

%package static
Summary:	libEMF static library
Summary(pl):	Statyczna biblioteka libEMF
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
libEMF static library.

%description static -l pl
Statyczna biblioteka libEMF.

%prep
%setup -q
%patch -p1

%build
# supplied libtool is broken (no C++ libraries support)
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-editing

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

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

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
