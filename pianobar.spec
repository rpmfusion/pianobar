Name:           pianobar
Version:        2017.08.30
Release:        4%{?dist}
Summary:        Console-based client for Pandora

License:        MIT
URL:            https://6xq.net/pianobar/
Source0:        %url/%{name}-%{version}.tar.bz2
Patch0:         ffmpeg35_buildfix.patch

BuildRequires:  gnutls-devel
BuildRequires:  libao-devel
BuildRequires:  libcurl-devel
BuildRequires:  libmad-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  json-c-devel
BuildRequires:  faad2-devel
BuildRequires:  ffmpeg-devel
BuildRequires:  libmad-devel


%description
pianobar is a free/open-source, console-based client for the personalized online
radio Pandora.

Features
* play and manage (create, add more music, delete, rename, ...) stations
* rate songs and explain why they have been selected
* upcoming songs/song history
* customize keybindings and text output
* remote control and eventcmd interface (send tracks to last.fm, for example)
* proxy support for listeners outside the USA


%prep
%autosetup -p1
touch configure
chmod a+x configure

%build
%configure
%make_build V=1


%install
%make_install PREFIX=%{_prefix}


%files
%doc ChangeLog README.md
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Thu Mar 08 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 2017.08.30-4
- Rebuilt for new ffmpeg snapshot

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 2017.08.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Leigh Scott <leigh123linux@googlemail.com> - 2017.08.30-2
- Rebuilt for ffmpeg-3.5 git

* Tue Oct 17 2017 Leigh Scott <leigh123linux@googlemail.com> - 2017.08.30-1
- Update to latest upstream release.
- Fix debuginfo issue (actually call configure)

* Fri Sep 01 2017 Leigh Scott <leigh123linux@googlemail.com> - 2016.06.02-4
- Disable debuginfo

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2016.06.02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 24 2017 Richard Shaw <hobbes1069@gmail.com> - 2016.06.02-2
- Use configure so linker flags are utilized.

* Thu Jul 21 2016 Richard Shaw <hobbes1069@gmail.com> - 2016.06.02-1
- Update to latest upstream release.

* Fri Feb  1 2013 Richard Shaw <hobbes1069@gmail.com> - 2013.09.15-1
- Initial packaging.
