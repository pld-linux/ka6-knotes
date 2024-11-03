#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	24.05.2
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		knotes
Summary:	knotes
Name:		ka6-%{kaname}
Version:	24.05.2
Release:	2
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	1dd5add4693cad4b9a6eefea73527735
Patch0:		kmimemessage_include.patch
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6DBus-devel
BuildRequires:	Qt6Gui-devel
BuildRequires:	Qt6Network-devel
BuildRequires:	Qt6PrintSupport-devel
BuildRequires:	Qt6Test-devel
BuildRequires:	Qt6Widgets-devel
BuildRequires:	Qt6Xml-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	grantlee-qt6-devel >= 5.1
BuildRequires:	ka6-akonadi-devel >= %{kdeappsver}
BuildRequires:	ka6-akonadi-notes-devel >= %{kdeappsver}
BuildRequires:	ka6-akonadi-search-devel >= %{kdeappsver}
BuildRequires:	ka6-kcalutils-devel >= %{kdeappsver}
BuildRequires:	ka6-kmime-devel >= %{kdeappsver}
BuildRequires:	ka6-kontactinterface-devel >= %{kdeappsver}
BuildRequires:	ka6-kpimtextedit-devel >= %{kdeappsver}
BuildRequires:	ka6-libkdepim-devel >= %{kdeappsver}
BuildRequires:	ka6-pimcommon-devel >= %{kdeappsver}
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-kcmutils-devel >= %{kframever}
BuildRequires:	kf6-kcompletion-devel >= %{kframever}
BuildRequires:	kf6-kconfig-devel >= %{kframever}
BuildRequires:	kf6-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf6-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf6-kcrash-devel >= %{kframever}
BuildRequires:	kf6-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf6-kdnssd-devel >= %{kframever}
BuildRequires:	kf6-kdoctools-devel >= %{kframever}
BuildRequires:	kf6-kglobalaccel-devel >= %{kframever}
BuildRequires:	kf6-kiconthemes-devel >= %{kframever}
BuildRequires:	kf6-kitemmodels-devel >= %{kframever}
BuildRequires:	kf6-kitemviews-devel >= %{kframever}
BuildRequires:	kf6-knewstuff-devel >= %{kframever}
BuildRequires:	kf6-knotifications-devel >= %{kframever}
BuildRequires:	kf6-knotifyconfig-devel >= %{kframever}
BuildRequires:	kf6-kparts-devel >= %{kframever}
BuildRequires:	kf6-ktextwidgets-devel >= %{kframever}
BuildRequires:	kf6-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf6-kwindowsystem-devel >= %{kframever}
BuildRequires:	kf6-kxmlgui-devel >= %{kframever}
BuildRequires:	libxslt-progs
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Obsoletes:	ka5-%{kaname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KNotes is a program that lets you write the computer equivalent of
sticky notes. The notes are saved automatically when you exit the
program, and they display when you open the program. Features. Write
notes in your choice of font and background color.

%description -l pl.UTF-8
KNotes jest programem pozwalającym pisać na komputerze notatki,
odpowiedniki samoprzylepnych karteczek. Notatki są zapisywane
automatycznie przy wyjściu z programu i wyświetlane przy otwieraniu
programu. Właściwości: pisz notatki wybraną czcionką i kolorem tła.

%prep
%setup -q -n %{kaname}-%{version}
%patch0 -p1

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/akonadi_notes_agent
%attr(755,root,root) %{_bindir}/knotes
%ghost %{_libdir}/libknotesprivate.so.6
%attr(755,root,root) %{_libdir}/libknotesprivate.so.*.*
%ghost %{_libdir}/libnotesharedprivate.so.6
%attr(755,root,root) %{_libdir}/libnotesharedprivate.so.*.*
%dir %{_libdir}/qt6/plugins/pim6/kcms/knotes
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kcms/knotes/kcm_knote_action.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kcms/knotes/kcm_knote_collection.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kcms/knotes/kcm_knote_display.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kcms/knotes/kcm_knote_editor.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kcms/knotes/kcm_knote_misc.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kcms/knotes/kcm_knote_network.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kcms/knotes/kcm_knote_print.so
%dir %{_libdir}/qt6/plugins/pim6/kcms/summary
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kcms/summary/kcmknotessummary.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kontact/kontact_knotesplugin.so
%{_datadir}/akonadi/agents/notesagent.desktop
%{_desktopdir}/org.kde.knotes.desktop
%{_datadir}/config.kcfg/knotesglobalconfig.kcfg
%{_datadir}/config.kcfg/notesagentsettings.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.KNotes.xml
%{_datadir}/dbus-1/interfaces/org.kde.kontact.KNotes.xml
%{_iconsdir}/hicolor/*x*/apps/knotes.png
%{_iconsdir}/hicolor/*x*/actions/*.png
%{_iconsdir}/hicolor/scalable/apps/knotes.svg
%{_datadir}/knotes
%{_datadir}/knotifications6/akonadi_notes_agent.notifyrc
%{_datadir}/metainfo/org.kde.knotes.appdata.xml
%{_datadir}/knsrcfiles/knotes_printing_theme.knsrc
%{_datadir}/qlogging-categories6/knotes.categories
%{_datadir}/qlogging-categories6/knotes.renamecategories
%dir %{_datadir}/kxmlgui5/knotes
%{_datadir}/kxmlgui5/knotes/knotes_part.rc
%{_datadir}/kxmlgui5/knotes/knotesappui.rc
%{_datadir}/kxmlgui5/knotes/knotesui.rc
