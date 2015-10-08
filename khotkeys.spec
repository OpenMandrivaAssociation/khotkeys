%define major 5
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define plasmaver %(echo %{version} |cut -d. -f1-3)

Name: khotkeys
Version: 5.4.2
Release: 1
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Summary: Hotkeys support for KDE Plasma 5
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5DNSSD)
BuildRequires: cmake(KF5KDELibs4Support)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5KHtml)
BuildRequires: cmake(KF5Solid)
BuildRequires: cmake(KF5Plasma)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(LibKWorkspace)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(x11)

%description
KDE Plasma 5 Hotkey support.

%libpackage khotkeysprivate 5

%prep
%setup -qn %{name}-%{plasmaver}
%apply_patches

%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang khotkeys

%files -f khotkeys.lang
%{_libdir}/cmake/KHotKeysDBusInterface
%{_libdir}/qt5/plugins/kcm_hotkeys.so
%{_libdir}/qt5/plugins/kded_khotkeys.so
%{_datadir}/dbus-1/interfaces/org.kde.khotkeys.xml
%{_datadir}/khotkeys
%{_datadir}/kservices5/kded/*
%{_datadir}/kservices5/khotkeys.desktop
%doc %{_docdir}/HTML/en/kcontrol/khotkeys
