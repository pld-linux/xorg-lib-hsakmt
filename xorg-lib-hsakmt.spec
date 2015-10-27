Summary:	The HSAKMT library
Summary(pl.UTF-8):	Biblioteka HSAKMT
Name:		xorg-lib-hsakmt
Version:	1.0.0
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/hsakmt-%{version}.tar.bz2
# Source0-md5:	193263468586279ce1f7b1ecfd85ae5e
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
hsakmt is a thunk library that provides a userspace interface to
amdkfd (AMD's HSA Linux kernel driver). It is the HSA equivalent of
libdrm.

%description -l pl.UTF-8
hsakmt to biblioteka funkcji pośredniczących udostępniająca interfejs
przestrzeni użytkownika do amdkfd (sterownik jądra Linuksa do AMD
HSA). Jest to odpowiednik libdrm dla architektury HSA.

%package devel
Summary:	Header files for hsakmt library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki hsakmt
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
DMX (Distributed Multihead X) extension library.

This package contains the header files needed to develop programs that
use hsakmt.

%description devel -l pl.UTF-8
Biblioteka rozszerzenia DMX (Distributed Multihead X).

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki hsakmt.

%package static
Summary:	Static hsakmt library
Summary(pl.UTF-8):	Biblioteka statyczna hsakmt
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
DMX (Distributed Multihead X) extension library.

This package contains the static hsakmt library.

%description static -l pl.UTF-8
Biblioteka rozszerzenia DMX (Distributed Multihead X).

Pakiet zawiera statyczną bibliotekę hsakmt.

%prep
%setup -q -n hsakmt-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
CFLAGS="%{rpmcflags} -std=c99 -D_XOPEN_SOURCE=700"
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libhsakmt-1.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README
%attr(755,root,root) %{_libdir}/libhsakmt-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libhsakmt-1.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhsakmt-1.so
%{_includedir}/hsakmt-1
%{_pkgconfigdir}/hsakmt-1.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libhsakmt-1.a
