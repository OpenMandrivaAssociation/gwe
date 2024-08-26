%global uuid    com.leinardi.%{name}

# don't require because it uses Ayatana Appindicator
%global __requires_exclude  ^typelib\\(AppIndicator3\\).*$

Name:           gwe
Version:        0.15.9
Release:        1
Summary:        GreenWithEnvy ia a system utility designed to provide information of NVIDIA card.
License:        GPLv3+
URL:            https://gitlab.com/leinardi/gwe
Source0:        https://gitlab.com/leinardi/gwe/-/archive/%{version}/%{name}-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  meson
BuildRequires:  pkgconfig(python)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)

Requires:       dbus
Requires:       hicolor-icon-theme
Requires:       python-matplotlib-gtk
Requires:       python%{pyver}dist(pygobject)
Requires:       python%{pyver}dist(injector)
Requires:       python%{pyver}dist(peewee)
Requires:       python%{pyver}dist(py3nvml)
Requires:       python%{pyver}dist(pyxdg)
Requires:       python%{pyver}dist(requests)
Requires:       python%{pyver}dist(rx)
Requires:       python%{pyver}dist(python-xlib)

Provides:       greenwithenvy

# Only on Gnome-shell, still not ready for Cooker. Import pending (angry).
Recommends:     (gnome-shell-extension-appindicator if gnome-shell)

%description
GWE (GreenWithEnvy) is a GTK system utility designed to provide information, control the fans
and overclock your NVIDIA video card and graphics processor.

This packages requires NVIDIA proprietary drivers installed in system.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING.txt
%doc CHANGELOG.md README.md RELEASING.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/symbolic/*/*.svg
%{_metainfodir}/*.xml
%{python_sitelib}/%{name}/
