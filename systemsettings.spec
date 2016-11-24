%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define libname %mklibname systemsettingsview 3
%define plasmaver %(echo %{version} |cut -d. -f1-3)

Name: systemsettings
Version: 5.8.4
Release: 1
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Summary: KDE Frameworks 5 Systemsettings framework
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5KHtml)
BuildRequires: cmake(KF5KDELibs4Support)
BuildRequires: cmake(KF5KCMUtils)
Requires: %{libname} = %{EVRD}
Requires: kde-cli-tools

%description
KDE Plasma 5 system settings panel.

%libpackage systemsettingsview 3

%define devname %mklibname systemsettingsview -d
%package -n %{devname}
Summary: Development files for developing KDE Plasma 5 System Settings plugins
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}
Provides: systemsettings-devel = %{EVRD}

%description -n %{devname}
Development files for developing KDE Plasma 5 System Settings plugins.

%prep
%setup -qn %{name}-%{plasmaver}
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang systemsettings || touch systemsettings.lang

%files -f systemsettings.lang
%{_bindir}/systemsettings5
%{_datadir}/systemsettings
%{_datadir}/kservicetypes5/systemsettingscategory.desktop
%{_datadir}/kservicetypes5/systemsettingsexternalapp.desktop
%{_datadir}/kservicetypes5/systemsettingsview.desktop
%{_datadir}/kxmlgui5/systemsettings
%{_datadir}/kservices5/*
%{_datadir}/applications/kdesystemsettings.desktop
%{_datadir}/applications/systemsettings.desktop
%{_libdir}/qt5/plugins/*_mode.so
%doc %{_docdir}/HTML/*/systemsettings

%files -n %{devname}
%{_includedir}/systemsettingsview
%{_libdir}/libsystemsettingsview.so
