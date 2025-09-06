%define url_ver %(echo %{version}|cut -d. -f1,2)

%define api	1.0
%define major	0
%define libname %mklibname %{name}
%define libname2 %mklibname %{name}-2
%define girname %mklibname %{name}-gir %{api}
%define girname2 %mklibname %{name}-gir 2.0
%define devname %mklibname -d %{name}
%define devname2 %mklibname -d %{name}-2

%define _disable_rebuild_configure 1

Summary:	A convenience library for the Yahoo! Place Finder APIs
Name:		geocode-glib
Version:	3.26.4
Release:	11
Group:		Networking/Other
License:	LGPLv2
Url:		https://geoclue.freedesktop.org/
Source0:	https://ftp.gnome.org/pub/GNOME/sources/geocode-glib/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(json-glib-1.0) >= 0.13.1
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(libsoup-3.0)
BuildRequires:	pkgconfig(geoip)
BuildRequires:  meson
BuildRequires:  gtk-doc

%description
geocode-glib is a convenience library for the Yahoo! Place Finder
APIs, as described at:
http://developer.yahoo.com/geo/placefinder/

The Place Finder web service allows to do geocoding (finding longitude
and latitude from an address), and reverse geocoding (finding an address
from coordinates).

%package -n %{libname}
Group:		Networking/Other
Summary:	A convenience library for the Yahoo! Place Finder APIs for old libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes: %{libname}0 <= %{version}-%{release}

%description -n %{libname}
Geocode-glib allows you to do geocoding (going from a place name,
to a longitude/latitude pair) and reverse geocoding (finding a place
name from coordinates) using Yahoo! Place Finder API.

This library should be used in place of Geoclue's D-Bus API for
geocoding and reverse geocoding.

This version is built against old libraries.

%package -n %{libname2}
Group:		Networking/Other
Summary:	A convenience library for the Yahoo! Place Finder APIs
Requires:	%{name} = %{version}-%{release}

%description -n %{libname2}
Geocode-glib allows you to do geocoding (going from a place name,
to a longitude/latitude pair) and reverse geocoding (finding a place
name from coordinates) using Yahoo! Place Finder API.

This library should be used in place of Geoclue's D-Bus API for
geocoding and reverse geocoding.

%package -n %{girname}
Group:		Networking/Other
Summary:	A convenience library for the Yahoo! Place Finder APIs for use with old libraries

%description -n %{girname}
This package contains GObjectIntrospection data for geocode-glib.

This version uses old libraries.

%package -n %{girname2}
Group:		Networking/Other
Summary:	A convenience library for the Yahoo! Place Finder APIs

%description -n %{girname2}
This package contains GObjectIntrospection data for geocode-glib.

%package -n %{devname}
Group:		Networking/Other
Summary:	A convenience library for the Yahoo! Place Finder APIs using old libraries
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the development files for geocode-glib.

This version links to old libraries.

%package -n %{devname2}
Group:		Networking/Other
Summary:	A convenience library for the Yahoo! Place Finder APIs
Requires:	%{libname2} = %{version}-%{release}
Requires:	%{girname2} = %{version}-%{release}

%description -n %{devname2}
This package contains the development files for geocode-glib.

%prep
%autosetup -p1

%build
%define _vpath_builddir %{_vendor}-%{_target_os}-build-soup2
%meson -Denable-installed-tests=false -Dsoup2=true
%meson_build

%define _vpath_builddir %{_vendor}-%{_target_os}-build-soup3
%meson -Denable-installed-tests=false -Dsoup2=false
%meson_build

%install
%define _vpath_builddir %{_vendor}-%{_target_os}-build-soup2
%meson_install

%define _vpath_builddir %{_vendor}-%{_target_os}-build-soup3
%meson_install

%files
%{_iconsdir}/hicolor/scalable/places/

%files -n %{libname}
%{_libdir}/libgeocode-glib.so.%{major}*

%files -n %{libname2}
%{_libdir}/libgeocode-glib-2.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/GeocodeGlib-%{api}.typelib

%files -n %{girname2}
%{_libdir}/girepository-1.0/GeocodeGlib-2.0.typelib

%files -n %{devname}
%{_includedir}/geocode-glib-%{api}
%{_libdir}/libgeocode-glib.so
%{_libdir}/pkgconfig/geocode-glib-1.0.pc
%{_datadir}/gir-1.0/GeocodeGlib-%{api}.gir
%doc %{_datadir}/gtk-doc/html/%{name}

%files -n %{devname2}
%{_includedir}/geocode-glib-2.0
%{_libdir}/libgeocode-glib-2.so
%{_libdir}/pkgconfig/geocode-glib-2.0.pc
%doc %{_datadir}/gtk-doc/html/%{name}-2
%{_datadir}/gir-1.0/GeocodeGlib-2.0.gir
