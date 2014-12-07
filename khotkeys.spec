%define major 5
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define plasmaver %(echo %{version} |cut -d. -f1-3)

Name: khotkeys
Version: 5.1.1
Release: 2
Source0: ftp://ftp.kde.org/pub/kde/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
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
BuildRequires: ninja

%description
KDE Plasma 5 Hotkey support

%libpackage khotkeysprivate 5

%prep
%setup -qn %{name}-%{plasmaver}
%apply_patches

%cmake -G Ninja

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install %{?_smp_mflags}
%find_lang khotkeys

%files -f khotkeys.lang
%{_libdir}/cmake/KHotKeysDBusInterface
%{_libdir}/plugins/kcm_hotkeys.so
%{_libdir}/plugins/kded_khotkeys.so
%{_datadir}/dbus-1/interfaces/org.kde.khotkeys.xml
%{_datadir}/khotkeys
%{_datadir}/kservices5/kded/*
%{_datadir}/kservices5/khotkeys.desktop
%doc %{_docdir}/HTML/en/kcontrol/khotkeys
