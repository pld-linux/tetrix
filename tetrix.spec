#
Summary:	A curses-based clone of Tetris
Summary(pl.UTF-8):	Klon gry Tetris typu roguelike.
Name:		tetrix
Version:	2.3
Release:	1
License:	GPL v2
Group:		Applications/Games
Source0:	http://www.catb.org/~esr/tetrix/%{name}-%{version}.tar.gz
# Source0-md5:	3567667a52571ebd3c3829af66defb93
Patch0:		%{name}-build.patch
Patch1:		%{name}-scoresfile.patch
URL:		http://www.catb.org/~esr/tetrix/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tetrix is a UNIX-hosted, curses-based clone of Tetris.

%description -l pl.UTF-8
Tetrix jest uniksowym klonem gry Tetris. Interfejs gry jest oparty o
bibliotekę curses. Tetrix używa aktywnego czekania, zatem główne
przeznaczenie tego programu to testowanie zachowania komputera przy
maksymalnym obciążeniu. Jeżeli po prostu chcesz pograć w tetris w
konsoli, zainstaluj vitetris.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} tetrix \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -I/usr/include/ncurses" \
	LFLAGS="%{rpmldflags}"

%{__make} tetrix.6

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man6,/var/games}
install tetrix $RPM_BUILD_ROOT%{_bindir}
install tetrix.6 $RPM_BUILD_ROOT%{_mandir}/man6
touch $RPM_BUILD_ROOT/var/games/tetrix.scores

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/tetrix
%{_mandir}/man6/tetrix.6*
%attr(660,root,root) %config(noreplace) %verify(not md5 mtime size) /var/games/tetrix.scores
