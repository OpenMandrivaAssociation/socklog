%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

Summary:	A small and secure syslogd replacement for use with runit
Name:		socklog
Version:	2.1.0
Release:	6
License:	BSD
Group:		System/Base
URL:		http://smarden.org/socklog/
Source0:	http://smarden.org/socklog/%{name}-%{version}.tar.gz
Requires:	runit
BuildRequires:	dietlibc-devel >= 0.32
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
socklog cooperates with the runit package to create a small and secure
replacement for syslogd. socklog supports system logging through Unix domain
sockets (/dev/log) and UDP sockets (0.0.0.0:514) with the help of runit's
runsvdir, runsv, and svlogd. socklog provides a different network logging
concept, and also does log event notification. svlogd has built in log file
rotation based on file size, so there is no need for any cron jobs to rotate
the logs. socklog is small, secure, and reliable. 

%prep

%setup -q -n admin

%build

pushd %{name}-%{version}/src
    echo "diet -Os gcc -pipe" > conf-cc
    echo "diet -Os gcc -static -s" > conf-ld
    make
popd

%install
rm -rf %{buildroot}

install -d %{buildroot}/sbin/
install -d %{buildroot}%{_mandir}/man{1,8}

pushd %{name}-%{version}
    for i in `cat package/commands`; do
	install -m755 src/$i %{buildroot}/sbin/
    done
popd

install -m0644 %{name}-%{version}/man/*.1 %{buildroot}%{_mandir}/man1/
install -m0644 %{name}-%{version}/man/*.8 %{buildroot}%{_mandir}/man8/

%clean
rm -rf %{buildroot}

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


%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 2.1.0-5mdv2010.0
+ Revision: 433986
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.1.0-4mdv2009.0
+ Revision: 269331
- rebuild early 2009.0 package (before pixel changes)

* Tue Jun 10 2008 Oden Eriksson <oeriksson@mandriva.com> 2.1.0-3mdv2009.0
+ Revision: 217546
- rebuilt against dietlibc-devel-0.32

* Tue May 13 2008 Oden Eriksson <oeriksson@mandriva.com> 2.1.0-2mdv2009.0
+ Revision: 206564
- don't build it against dietlibc anymore

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 27 2007 Oden Eriksson <oeriksson@mandriva.com> 2.1.0-1mdv2008.0
+ Revision: 18586
- 2.1.0


* Sun Mar 05 2006 Oden Eriksson <oeriksson@mandriva.com> 2.0.3-1mdk
- 2.0.3 (Minor bugfixes)

* Wed Oct 19 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0.2-1mdk
- 2.0.2

* Mon Feb 07 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 2.0.0-1mdk
- 2.0.0

* Sat Aug 28 2004 Franck Villaume <fvill@freesurf.fr> 1.5.0-1mdk
- 1.5.0

* Sat Aug 09 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 1.2.0-1mdk
- initial cooker contrib

