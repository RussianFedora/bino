Name:               bino
Version:            1.6.3
Release:            2%{?dist}
Summary:            Video Player with 3D and Multi-Display Video Support
Summary(ru):        Видеоплеер с поддержкой 3D и многомониторных конфигураций

Source:             http://download.savannah.nongnu.org/releases-noredirect/%{name}/%{name}-%{version}.tar.xz
Source1:            bino.desktop
# debian patch to fix build against ffmpeg 2.9
Patch0:             ffmpeg_2.9.patch
URL:                http://bino.nongnu.org/
Group:              Applications/Multimedia
License:            GPLv2

BuildRequires:      pkgconfig(Qt5)
BuildRequires:      pkgconfig(glew) >= 1.5.0
BuildRequires:      pkgconfig(libavcodec) >= 0.8
BuildRequires:      pkgconfig(openal)
BuildRequires:      pkgconfig
BuildRequires:      autoconf
BuildRequires:      automake
BuildRequires:      libtool
BuildRequires:      desktop-file-utils
BuildRequires:      texinfo
BuildRequires:      pkgconfig(libass)
BuildRequires:      pkgconfig(x11)
BuildRequires:      libGLEWmx
BuildRequires:      gettext
BuildRequires:      libquadmath-devel

Requires:           hicolor-icon-theme

Requires(preun):    info
Requires(post):     info

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
%patch0 -p1 -b .ffmpeg

%build
#autoreconf -i
%configure --disable-silent-rules --without-equalizer --without-lirc

%make_build


%install
%make_install

desktop-file-install %{buildroot}%{_datadir}/applications/%{name}.desktop
rm -r %{buildroot}%{_docdir}/%{name}
rm -f %{buildroot}%{_infodir}/dir
%find_lang %{name}

%post
/usr/bin/update-desktop-database &> /dev/null || :
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}//bino.info.gz || :

%preun
if [ $1 = 0 ] ; then
  /sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/bino.info.gz || :
fi

%postun
/usr/bin/update-desktop-database &> /dev/null || :


%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%doc doc/*.html doc/*.jpg doc/*.png
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_infodir}/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
* Tue Jun 14 2016 Arkady L. Shane <ashejn@russianfedora.pro> - 1.6.3-2.R
- rebuilt against new ffmpeg

* Wed Jun 01 2016 Vasiliy N. Glazov <vascom2@gmail.com> - 1.6.3-1.R
- update to 1.6.3

* Tue Jan 29 2013 Vasiliy N. Glazov <vascom2@gmail.com> - 1.4.2-1.R
- update to 1.4.2

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

* Tue May 01 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 1.3.3-1.R
- update to 1.3.3

* Thu Mar 22 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 1.3.2-1.R
- update to 1.3.2

* Sun Mar 11 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 1.3.1-1.R
- update to 1.3.1

* Mon Jan 30 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 1.3.0-1.R
- update to 1.3.0

* Tue Nov 22 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 1.2.1-2.R
- Added description in russian language

* Sat Oct 1 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 1.2.1-1.R
- update to 1.2.1

* Thu Sep 22 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 1.2.0-1.R
- update to 1.2.0

* Sun Aug 14 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 1.1.3-1.R
- update to 1.1.3

* Fri Aug 05 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 1.1.2-1.R
- update to 1.1.2

* Wed Jul  6 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 1.1.1-2
- FFmpeg dependency >= 0.7

* Tue Jun  21 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 1.1.1-1
- update to 1.1.1

* Fri Mar  4 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.9.1-1
- update to 0.9.1

* Mon Feb 14 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.8.1-0.1.gita37be3e28681
- last snapsot
- initial build
