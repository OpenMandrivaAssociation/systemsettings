%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define libname %mklibname systemsettingsview 3

Name: systemsettings
Version: 5.0.95
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz
Summary: KDE Frameworks 5 Systemsettings framework
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5KHtml)
BuildRequires: cmake(KF5KDELibs4Support)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: ninja
Requires: %{libname} = %{EVRD}

%description
KDE Plasma 5 system settings panel

%libpackage systemsettingsview 3

%define devname %mklibname systemsettingsview -d
%package -n %{devname}
Summary: Development files for developing KDE Plasma 5 System Settings plugins
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}
Provides: systemsettings-devel = %{EVRD}

%description -n %{devname}
Development files for developing KDE Plasma 5 System Settings plugins

%prep
%setup -q
%cmake -G Ninja

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install %{?_smp_mflags}
%find_lang systemsettings

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
%{_libdir}/plugins/*_mode.so
%doc %{_docdir}/HTML/en/systemsettings

%files -n %{devname}
%{_includedir}/systemsettingsview
%{_libdir}/libsystemsettingsview.so
