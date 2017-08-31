Name:           pianobar
Version:        2016.06.02
Release:        3%{?dist}
Summary:        Console-based client for Pandora

License:        MIT
URL:            http://6xq.net/pianobar/
Source0:        https://6xq.net/pianobar/%{name}-%{version}.tar.bz2

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
%autosetup
touch configure


%build
make %{?_smp_mflags} V=1


%install
%make_install PREFIX=%{_prefix}


%files
%doc ChangeLog README.md
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2016.06.02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 24 2017 Richard Shaw <hobbes1069@gmail.com> - 2016.06.02-2
- Use configure so linker flags are utilized.

* Thu Jul 21 2016 Richard Shaw <hobbes1069@gmail.com> - 2016.06.02-1
- Update to latest upstream release.

* Fri Feb  1 2013 Richard Shaw <hobbes1069@gmail.com> - 2013.09.15-1
- Initial packaging.
