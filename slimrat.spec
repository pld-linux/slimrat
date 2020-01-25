#
# Conditional build:
%bcond_without  gui	# build without GUI
#
Summary:	Utility for downloading files from Rapidshare
Summary(pl.UTF-8):	Program do pobierania plików z Rapidshare
Name:		slimrat
Version:	1.0
Release:	0.2
License:	MIT License
Group:		Applications
Source0:	http://slimrat.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	2a052075e8bf3966ec003ed4d8d194f7
Patch0:		%{name}-FindBin.patch
URL:		http://code.google.com/p/slimrat/
Requires:	aview
Requires:	ImageMagick
Requires:	perl-base
Requires:	perl(Getopt::Long)
Requires:	perl(HTTP::Response::Encoding)
%if %{with gui}
Requires:	gtk+2
Requires:	perl(Gtk2::GladeXML)
Requires:	perl(Gtk2::SimpleList)
Suggests:	perl-Spiffy
Suggests:	xclip
%endif
Requires:	perl(LWP::UserAgent)
Requires:	perl(Term::ANSIColor)
Requires:	perl(WWW::Mechanize)
Requires:	tesseract
Requires:	wget
Obsoletes:	perl-Clipboard
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Command line and GUI utility for downloading files from Rapidshare
(Free) on Linux. Written in perl, uses wget and GTK GUI.

%description -l pl.UTF-8
Program do pobierania plików z Rapidshare (Free), wersja konsolowa i
GUI dla Linuksa. Aplikacja napisana w perlu, korzysta z wget i GTK
GUI.

%prep
%setup -q
%patch0 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_datadir}/slimrat
install -d $RPM_BUILD_ROOT%{_datadir}/slimrat/Clipboard
install -d $RPM_BUILD_ROOT%{_datadir}/slimrat/plugins
install -d $RPM_BUILD_ROOT%{_sysconfdir}
install src/slimrat $RPM_BUILD_ROOT%{_bindir}
install slimrat.conf $RPM_BUILD_ROOT%{_sysconfdir}
%if %{with gui}
# open function improved for modern perl >= 5.8. Always use the
# three-argument method
%{__sed} -i -e 's,"+<\$quefile","+<"\,\ "\$quefile",' src/slimrat-gui
install src/slimrat-gui $RPM_BUILD_ROOT%{_bindir}
install src/slimrat.glade $RPM_BUILD_ROOT%{_datadir}/slimrat
%endif
install src/*.pm $RPM_BUILD_ROOT%{_datadir}/slimrat
install src/Clipboard/*.pm $RPM_BUILD_ROOT%{_datadir}/slimrat/Clipboard
install src/plugins/*.pm $RPM_BUILD_ROOT%{_datadir}/slimrat/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README proxies queue
%attr(755,root,root) %{_bindir}/slimrat
%{?with_gui:%attr(755,root,root) %{_bindir}/slimrat-gui}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/slimrat.conf
%dir %{_datadir}/slimrat
%dir %{_datadir}/slimrat/Clipboard
%dir %{_datadir}/slimrat/plugins
%{?with_gui:%{_datadir}/slimrat/slimrat.glade}
%{_datadir}/slimrat/*.pm
%{_datadir}/slimrat/Clipboard/*.pm
%{_datadir}/slimrat/plugins/*.pm
