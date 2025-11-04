%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
%define plasmaver %(echo %{version} |cut -d. -f1-3)
#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Name: systemsettings
Version: 6.5.1
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/systemsettings/-/archive/%{gitbranch}/systemsettings-%{gitbranchd}.tar.bz2#/systemsettings-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/systemsettings-%{version}.tar.xz
%endif
Summary: KDE Frameworks 6 Systemsettings framework
URL: https://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6QuickWidgets)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(PlasmaActivities)
BuildRequires: cmake(PlasmaActivitiesStats)
BuildRequires: cmake(KF6Package)
BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6Kirigami2)
BuildRequires: cmake(KF6Runner)
BuildRequires: cmake(KF6Auth)
BuildRequires: cmake(KF6ItemModels)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Service)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(LibKWorkspace) >= 5.27.80
Requires: kde-cli-tools >= 6.0
Requires: kirigami-addons
BuildSystem: cmake
BuildOption: -DBUILD_QCH:BOOL=ON
BuildOption: -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
# Renamed after 6.0 2025-05-03
%rename plasma6-systemsettings

# For the map widget used for timezone selection in Date & Time
Requires:	qml(QtLocation)

%patchlist

%description
KDE Plasma 6 system settings panel.

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/systemsettings.categories
%{_bindir}/systemsettings
%{_datadir}/systemsettings
%{_datadir}/metainfo/org.kde.systemsettings.metainfo.xml
%{_datadir}/kglobalaccel/systemsettings.desktop
%{_datadir}/applications/*.desktop
%{_qtdir}/plugins/kf6/krunner/krunner_systemsettings.so
%{_datadir}/zsh/site-functions/_systemsettings
