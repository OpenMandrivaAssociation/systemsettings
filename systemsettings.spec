%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
%define plasmaver %(echo %{version} |cut -d. -f1-3)

Name: systemsettings
Version: 5.27.12
Release: 1
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Summary: KDE Frameworks 5 Systemsettings framework
URL: https://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5QuickWidgets)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5KHtml)
BuildRequires: cmake(KF5KDELibs4Support)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(KF5Activities)
BuildRequires: cmake(KF5ActivitiesStats)
BuildRequires: cmake(KF5Package)
BuildRequires: cmake(KF5Declarative)
BuildRequires: cmake(KF5Kirigami2)
BuildRequires: cmake(LibKWorkspace) < 5.27.50
BuildRequires: cmake(KF5Runner)
BuildRequires: kdeclarative
Requires: kde-cli-tools
Requires: khtml
Requires: kdeclarative
Requires: kirigami2 >= %{version}
Conflicts: systemd-kcm < 1.2.1-5
Obsoletes: %{mklibname systemsettingsview 3} < 5.24.0
Obsoletes: %{mklibname -d systemsettingsview} < 5.24.0

%description
KDE Plasma 5 system settings panel.

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang systemsettings || touch systemsettings.lang

%files -f systemsettings.lang
%{_libdir}/libsystemsettingsview.so.*
%{_datadir}/qlogging-categories5/systemsettings.categories
%{_bindir}/systemsettings
%{_bindir}/systemsettings5
%{_datadir}/systemsettings
%{_datadir}/metainfo/org.kde.systemsettings.metainfo.xml
%{_datadir}/kglobalaccel/systemsettings.desktop
%{_datadir}/kservicetypes5/*.desktop
%{_datadir}/kxmlgui5/systemsettings
%{_datadir}/kpackage
%{_datadir}/applications/*.desktop
%{_libdir}/qt5/plugins/systemsettingsview
%{_libdir}/qt5/plugins/kf5/krunner/krunner_systemsettings.so
%{_datadir}/zsh/site-functions/_systemsettings
%doc %{_docdir}/HTML/*/systemsettings
