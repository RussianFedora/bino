Summary:            Video Player with 3D and Multi-Display Video Support
Name:               bino
Version:            0.9.1
Release:            1%{?dist}

Source:             http://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.xz
Source1:            bino.desktop
URL:                http://bino.nongnu.org/
Group:              Applications/Multimedia
License:            GPLv2

BuildRequires:      qt4-devel
BuildRequires:      glew-devel >= 1.5.0
BuildRequires:      ffmpeg-devel
BuildRequires:      openal-devel
BuildRequires:      pkgconfig
BuildRequires:      autoconf automake libtool
BuildRequires:      desktop-file-utils
BuildRequires:      texinfo

Requires(preun):    /sbin/install-info
Requires(post):     /sbin/install-info

%description
Bino is a video player with two special features:
* support for 3D videos, with a wide variety of input and output formats.
* support for multi-display video, e.g. for powerwalls, Virtual Reality
  installations and other multi-projector setups.


%prep
%setup -q

%build
autoreconf -i
export LDFLAGS="-lavcodec -lavutil -lGL"
%configure --disable-silent-rules

make %{?_smp_mflags}


%install
%makeinstall

install -D -m0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
rm -r %{buildroot}%{_docdir}/bino
rm -f %{buildroot}%{_infodir}/dir


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


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README
%doc doc/*.html doc/*.jpg doc/*.png
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_infodir}/%{name}*
%{_datadir}/applications/%{name}.desktop


%changelog
* Fri Mar  4 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.9.1-1
- update to 0.9.1

* Mon Feb 14 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.8.1-0.1.gita37be3e28681
- last snapsot
- initial build
