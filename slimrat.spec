#
# Conditional build:
%bcond_without  gui	# build without GUI
#
%include	/usr/lib/rpm/macros.perl
Summary:	Utility for downloading files from Rapidshare
Summary(pl.UTF-8):	Program do pobierania plików z Rapidshare
Name:		slimrat
Version:	1.0
Release:	0.1
License:	MIT License
Group:		Applications
Source0:	http://slimrat.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	2a052075e8bf3966ec003ed4d8d194f7
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

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/Clipboard
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/plugins
install -d $RPM_BUILD_ROOT%{_sysconfdir}
install src/slimrat $RPM_BUILD_ROOT%{_bindir}
install slimrat.conf $RPM_BUILD_ROOT%{_sysconfdir}
%if %{with gui}
# open function improved for modern perl >= 5.8. Always use the
# three-argument method
%{__sed} -i -e 's,"+<\$quefile","+<"\,\ "\$quefile",' src/slimrat-gui
install src/slimrat-gui $RPM_BUILD_ROOT%{_bindir}
install src/slimrat.glade $RPM_BUILD_ROOT%{_bindir}
%endif
install src/*.pm $RPM_BUILD_ROOT%{perl_vendorlib}
install src/Clipboard/*.pm $RPM_BUILD_ROOT%{perl_vendorlib}/Clipboard
install src/plugins/*.pm $RPM_BUILD_ROOT%{perl_vendorlib}/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README proxies queue
%attr(755,root,root) %{_bindir}/slimrat*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/slimrat.conf
%dir %{perl_vendorlib}/Clipboard
%dir %{perl_vendorlib}/plugins
%{perl_vendorlib}/*.pm
%{perl_vendorlib}/Clipboard/*.pm
%{perl_vendorlib}/plugins/*.pm
