#
# Conditional build:
%bcond_without  gui	# build without GUI
#
%include	/usr/lib/rpm/macros.perl
Summary:	Utility for downloading files from Rapidshare
Summary(pl.UTF-8):	Program do pobierania plików z Rapidshare
Name:		slimrat
Version:	0.9.5.4
Release:	0.1
License:	MIT License
Group:		Applications
Source0:	http://slimrat.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	945d53b830696c011a54bb026283693b
URL:		http://code.google.com/p/slimrat/
Requires:	perl-base
Requires:	perl(Getopt::Long)
Requires:	perl(HTTP::Response::Encoding)
%if %{with gui}
Requires:	gtk+2
Requires:	perl(Gtk2::GladeXML)
Requires:	perl(Gtk2::SimpleList)
Suggests:	xclip
%endif
Requires:	perl(LWP::UserAgent)
Requires:	perl(Term::ANSIColor)
Requires:	perl(WWW::Mechanize)
Requires:	wget
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
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/plugins
install slimrat $RPM_BUILD_ROOT%{_bindir}
%if %{with gui}
# open function improved for modern perl >= 5.8. Always use the
# three-argument method
%{__sed} -i -e 's,"+<\$quefile","+<"\,\ "\$quefile",' slimrat-gui
install slimrat-gui $RPM_BUILD_ROOT%{_bindir}
%endif
install Plugin.pm $RPM_BUILD_ROOT%{perl_vendorlib}
install Toolbox.pm $RPM_BUILD_ROOT%{perl_vendorlib}
install slimrat.glade $RPM_BUILD_ROOT%{perl_vendorlib}
install plugins/*.pm $RPM_BUILD_ROOT%{perl_vendorlib}/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%dir %{perl_vendorlib}/plugins
%{perl_vendorlib}/Plugin.pm
%{perl_vendorlib}/Toolbox.pm
%{perl_vendorlib}/slimrat.glade
%{perl_vendorlib}/plugins/*.pm
