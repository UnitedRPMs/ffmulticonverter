Name:       ffmulticonverter
Version:    1.8.0
Release:    4%{?dist}
Summary:    GUI File Format Converter

License:    GPLv3+
URL:        https://github.com/ilstam/FF-Multi-Converter
Source0:    http://sourceforge.net/projects/ffmulticonv/files/%{name}-%{version}.tar.gz

BuildArch:  noarch

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-setuptools
BuildRequires:  python3-rpm-macros
BuildRequires:  desktop-file-utils

Requires:   python3-qt5
Requires:   ImageMagick
Requires:   unoconv
Requires:   ffmpeg


%description
Graphical application which enables you to convert audio, video, image and
document files between all popular formats using ffmpeg, unoconv, and
ImageMagick.


%prep
%autosetup


%build
python%{python3_version} setup.py build

%install
python%{python3_version} setup.py install --root=%{buildroot} --optimize=1 --skip-build


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%files
%doc ChangeLog README.txt AUTHORS TRANSLATORS
%license COPYING
%{_bindir}/%{name}
%{python3_sitelib}/%{name}-%version-py%{python3_version}.egg-info
%{python3_sitelib}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}.1.*

%changelog

* Wed Jun 10 2020 David Va <davidva AT tuta DOT io> 1.8.0-4
- Rebuilt for python3.9

* Sun Dec 29 2019 David Va <davidva AT tuta DOT io> 1.8.0-3
- Rebuilt

* Wed Jul 04 2018 David Va <davidva AT tuta DOT io> 1.8.0-2
- Rebuilt for Python3.7

* Mon Oct 02 2017 David Va <davidva AT tutanota DOT com> 1.8.0-1
- Initial release
