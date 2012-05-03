%define major 0
%define libname %mklibname %{name} %{major}
%define girname %mklibname %{name}-gir 1.0
%define develname %mklibname -d %{name}

Summary: A convenience library for the Yahoo! Place Finder APIs
Name: geocode-glib
Version: 0.99.0
Release: 2
Group: Networking/Other
License: LGPLv2
URL: http://geoclue.freedesktop.org/
Source0: http://ftp.acc.umu.se/pub/GNOME/sources/%{name}/0.99/%{name}-%{version}.tar.bz2

BuildRequires: intltool
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(json-glib-1.0) >= 0.13.1
BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: gobject-introspection-devel >= 0.6.3
BuildRequires: gnome-doc-utils

%description
geocode-glib is a convenience library for the Yahoo! Place Finder
APIs, as described at:
http://developer.yahoo.com/geo/placefinder/

The Place Finder web service allows to do geocoding (finding longitude
and latitude from an address), and reverse geocoding (finding an address
from coordinates).

%package -n %{libname}
Group: Networking/Other
Summary: A convenience library for the Yahoo! Place Finder APIs

%description -n %{libname}
Geocode-glib allows you to do geocoding (going from a place name,
to a longitude/latitude pair) and reverse geocoding (finding a place
name from coordinates) using Yahoo! Place Finder API.

This library should be used in place of Geoclue's D-Bus API for
geocoding and reverse geocoding.

%package -n %{girname}
Group: Networking/Other
Summary: A convenience library for the Yahoo! Place Finder APIs

%description -n %{girname}
This package contains GObjectIntrospection data for geocode-glib.

%package -n %{develname}
Group: Networking/Other
Summary: A convenience library for the Yahoo! Place Finder APIs
Requires: %{libname} = %{version}-%{release}
Requires: %{girname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains the development files for geocode-glib.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files -n %{libname}
%{_libdir}/libgeocode-glib.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/GeocodeGlib-1.0.typelib

%files -n %{develname}
%{_includedir}/geocode-glib
%{_libdir}/libgeocode-glib.so
%{_libdir}/pkgconfig/geocode-glib.pc
%{_datadir}/gir-1.0/GeocodeGlib-1.0.gir
%{_datadir}/gtk-doc/html/%{name}

