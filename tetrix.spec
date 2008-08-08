#
Summary:	A curses-based clone of Tetris.
Summary(pl.UTF-8):	Klon gry Tetris typu roguelike.
Name:		tetrix
Version:	2.2
Release:	0.1
License:	GPL v. 2
Group:		Applications/Games
Source0:	http://www.catb.org/~esr/tetrix/%{name}-%{version}.tar.gz
# Source0-md5:	141390f40c9c03a9b54455e257e0eafc
Patch0:		%{name}-buildfix.patch
Patch1:		%{name}-scoresfile.patch
URL:		http://www.catb.org/~esr/tetrix/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tetrix is a UNIX-hosted, curses-based clone of Tetris.

%description -l pl.UTF-8
Tetrix jest uniksowym klonem gry Tetris. Interface gry jest oparty o
bibliotekę curses.

%prep
%setup -q

%patch0 -p1
%patch1 -p1

%build
%{__make} tetrix \
	CFLAGS=-I/usr/include/ncurses

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
%attr(2755,root,games) %{_bindir}/tetrix
%{_mandir}/man6/*
%attr(660,root,games) %config(noreplace) %verify(not md5 mtime size) /var/games/tetrix.scores
