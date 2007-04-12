%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

Summary:	A small and secure syslogd replacement for use with runit
Name:		socklog
Version:	2.0.3
Release:	%mkrel 1
License:	BSD
Group:		System/Base
URL:		http://smarden.org/socklog/
Source0:	http://smarden.org/socklog/%{name}-%{version}.tar.bz2
Requires:	runit
BuildRequires:	dietlibc-devel >= 0.20
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
socklog cooperates with the runit package to create a small and
secure replacement for syslogd. socklog supports system logging
through Unix domain sockets (/dev/log) and UDP sockets
(0.0.0.0:514) with the help of runit's runsvdir, runsv, and
svlogd. socklog provides a different network logging concept, and
also does log event notification. svlogd has built in log file
rotation based on file size, so there is no need for any cron jobs
to rotate the logs. socklog is small, secure, and reliable. 

%prep

%setup -q -n admin

%build
# OE: This is quite different from the ordinary to some...
# It makes rpmlint crazy, but what does _it_ know about the real world?
pushd %{name}-%{version}/src
    echo "diet -Os gcc -pipe" > conf-cc
    echo "diet -Os gcc -static -s" > conf-ld
    make
popd

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

install -d %{buildroot}/sbin/
install -d %{buildroot}%{_mandir}/man{1,8}

pushd %{name}-%{version}
    for i in `cat package/commands`; do
	install -m755 src/$i %{buildroot}/sbin/
    done
popd

install -m755 %{name}-%{version}/man/*.1 %{buildroot}%{_mandir}/man1/
install -m755 %{name}-%{version}/man/*.8 %{buildroot}%{_mandir}/man8/

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{name}-%{version}/package/CHANGES
%doc %{name}-%{version}/package/README
%doc %{name}-%{version}/doc/benefits.html
%doc %{name}-%{version}/doc/configuration.html
%doc %{name}-%{version}/doc/examples.html
%doc %{name}-%{version}/doc/index.html
%doc %{name}-%{version}/doc/install.html
%doc %{name}-%{version}/doc/network.html
%doc %{name}-%{version}/doc/notify.html
%doc %{name}-%{version}/doc/readme.solaris.html
%doc %{name}-%{version}/doc/upgrade.html
%doc %{name}-%{version}/doc/usedietlibc.html
%attr(0755,root,root) /sbin/socklog-conf
%attr(0755,root,root) /sbin/socklog
%attr(0755,root,root) /sbin/socklog-check
%attr(0755,root,root) /sbin/tryto
%attr(0755,root,root) /sbin/uncat
%attr(0644,root,root) %{_mandir}/man1/tryto.1*
%attr(0644,root,root) %{_mandir}/man1/uncat.1*
%attr(0644,root,root) %{_mandir}/man8/socklog-conf.8*
%attr(0644,root,root) %{_mandir}/man8/socklog.8*
%attr(0644,root,root) %{_mandir}/man8/socklog-check.8*

