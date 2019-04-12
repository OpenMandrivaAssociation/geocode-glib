%define url_ver %(echo %{version}|cut -d. -f1,2)

%define api	1.0
%define major	0
%define libname %mklibname %{name} %{major}
%define girname %mklibname %{name}-gir %{api}
%define devname %mklibname -d %{name}

%define _disable_rebuild_configure 1

Summary:	A convenience library for the Yahoo! Place Finder APIs
Name:		geocode-glib
Version:	3.26.1
Release:	1
Group:		Networking/Other
License:	LGPLv2
Url:		http://geoclue.freedesktop.org/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/geocode-glib/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(json-glib-1.0) >= 0.13.1
BuildRequires:	pkgconfig(libsoup-2.4)
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
Summary:	A convenience library for the Yahoo! Place Finder APIs
Requires:	%{name} = %{version}-%{release}

%description -n %{libname}
Geocode-glib allows you to do geocoding (going from a place name,
to a longitude/latitude pair) and reverse geocoding (finding a place
name from coordinates) using Yahoo! Place Finder API.

This library should be used in place of Geoclue's D-Bus API for
geocoding and reverse geocoding.

%package -n %{girname}
Group:		Networking/Other
Summary:	A convenience library for the Yahoo! Place Finder APIs

%description -n %{girname}
This package contains GObjectIntrospection data for geocode-glib.

%package -n %{devname}
Group:		Networking/Other
Summary:	A convenience library for the Yahoo! Place Finder APIs
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the development files for geocode-glib.

%prep
%setup -q

%build
%meson \

%meson_build

%install
%meson_install

%files
%{_datadir}/icons/gnome/scalable/places/*.svg

%files -n %{libname}
%{_libdir}/libgeocode-glib.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/GeocodeGlib-%{api}.typelib

%files -n %{devname}
%exclude %{_libexecdir}/installed-tests/*
%{_includedir}/geocode-glib-%{api}
%{_libdir}/libgeocode-glib.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/GeocodeGlib-%{api}.gir
#{_datadir}/gtk-doc/html/%{name}-%{api}
%doc %{_datadir}/gtk-doc/html/%{name}/*

