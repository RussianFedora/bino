Name:               bino
Version:            1.4.2
Release:            1%{?dist}
Summary:            Video Player with 3D and Multi-Display Video Support
Summary(ru):        Видеоплеер с поддержкой 3D и многомониторных конфигураций

Source:             http://download.savannah.nongnu.org/releases-noredirect/%{name}/%{name}-%{version}.tar.xz
Source1:            bino.desktop
URL:                http://bino.nongnu.org/
Group:              Applications/Multimedia
License:            GPLv2

BuildRequires:      qt4-devel
BuildRequires:      glew-devel >= 1.5.0
BuildRequires:      ffmpeg-devel >= 0.8
BuildRequires:      openal-devel
BuildRequires:      pkgconfig
BuildRequires:      autoconf automake libtool
BuildRequires:      desktop-file-utils
BuildRequires:      texinfo
BuildRequires:      libass-devel
BuildRequires:      libX11-devel
BuildRequires:      libGLEWmx
BuildRequires:      gettext

Requires(preun):    /sbin/install-info
Requires(post):     /sbin/install-info

%description
Bino is a video player with two special features:
* support for 3D videos, with a wide variety of input and output formats.
* support for multi-display video, e.g. for powerwalls, Virtual Reality
  installations and other multi-projector setups.

%description -l ru
Bino это видеоплеер с двумя специальными возможностями:
* поддержка 3D видео с широким спектром выходных и выходных форматов.
* поддержка многомониторного видео, т.е. для стен, устройств
  виртуальной реальности и других многопроекторных установок.


%prep
%setup -q

%build
#autoreconf -i
%configure --disable-silent-rules

make %{?_smp_mflags}


%install
%makeinstall

#install -D -m0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-install %{buildroot}%{_datadir}/applications/%{name}.desktop
rm -r %{buildroot}%{_docdir}/%{name}
rm -f %{buildroot}%{_infodir}/dir
rm -f %{buildroot}%{_datadir}/icons/hicolor/icon-theme.cache
%find_lang %{name}


%post
update-desktop-database -q
if [ "$1" = 1 ]; then
  /sbin/install-info --info-dir=%{_infodir} %{_infodir}/bino.info.gz || :
fi


%preun
if [ "$1" = 0 ]; then
  /sbin/install-info --delete --info-dir=%{_infodir} %{_infodir}/bino.info.gz || :
fi


%postun
update-desktop-database -q


%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING README
%doc doc/*.html doc/*.jpg doc/*.png
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_infodir}/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/mimeinfo.cache
%{_datadir}/icons/hicolor/*/apps/%{name}.png
#%{_datadir}/icons/hicolor/icon-theme.cache
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
* Tue Jan 29 2013 Vasiliy N. Glazov <vascom2@gmail.com> - 1.4.2-1.R
- update to 1.4.1

* Sat Oct 13 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 1.4.1-1.R
- update to 1.4.1

* Thu Oct 04 2012 Vasiliy N. Glazov <vascom2@gmail.com> 1.4.0-2.R
- Added gettext to BR

* Mon Jun 25 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 1.4.0-1.R
- update to 1.4.0

* Wed Jun 13 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 1.3.5-1.R
- update to 1.3.5

* Sat May 12 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 1.3.4-1.R
- update to 1.3.4

* Mon May 01 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 1.3.3-1.R
- update to 1.3.3

* Thu Mar 22 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 1.3.2-1.R
- update to 1.3.2

* Sun Mar 11 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 1.3.1-1.R
- update to 1.3.1

* Mon Jan 30 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 1.3.0-1.R
- update to 1.3.0

* Tue Nov 22 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 1.2.1-2.R
- Added description in russian language

* Thu Oct 1 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 1.2.1-1.R
- update to 1.2.1

* Thu Sep 22 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 1.2.0-1.R
- update to 1.2.0

* Sun Aug 14 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 1.1.3-1.R
- update to 1.1.3

* Wed Aug 05 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 1.1.2-1.R
- update to 1.1.2

* Wed Jul  6 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 1.1.1-2
- FFmpeg dependency >= 0.7

* Thu Jun  21 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 1.1.1-1
- update to 1.1.1

* Fri Mar  4 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.9.1-1
- update to 0.9.1

* Mon Feb 14 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.8.1-0.1.gita37be3e28681
- last snapsot
- initial build
