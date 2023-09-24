%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define git 20230924

Name: plasma6-systemsettings
Version: 5.240.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/systemsettings/-/archive/master/systemsettings-master.tar.bz2#/systemsettings-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
%endif
Summary: KDE Frameworks 6 Systemsettings framework
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6QuickWidgets)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6Activities)
BuildRequires: cmake(KF6ActivitiesStats)
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
BuildRequires: plasma6-xdg-desktop-portal-kde
Requires: plasma6-kde-cli-tools

%description
KDE Plasma 6 system settings panel.

%prep
%autosetup -p1 -n systemsettings-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang systemsettings --all-name --with-html

%files -f systemsettings.lang
%{_libdir}/libsystemsettingsview.so.*
%{_datadir}/qlogging-categories6/systemsettings.categories
%{_bindir}/systemsettings
%{_datadir}/systemsettings
%{_datadir}/metainfo/org.kde.systemsettings.metainfo.xml
%{_datadir}/kglobalaccel/systemsettings.desktop
%{_datadir}/applications/*.desktop
%{_qtdir}/plugins/kf6/krunner/krunner_systemsettings.so
%{_datadir}/zsh/site-functions/_systemsettings
