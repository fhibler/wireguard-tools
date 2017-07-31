%global debug_package %{nil}

Name:           wireguard-tools
Version:        0.0.20170726
Release:        1%{?dist}
Epoch:          1
URL:            https://www.wireguard.io/
Summary:        Fast, modern, secure VPN tunnel
License:        GPLv2
Group:          Applications/Internet

Source0:        https://git.zx2c4.com/WireGuard/snapshot/WireGuard-%{version}.tar.xz

%{?systemd_requires}
BuildRequires:  systemd
BuildRequires:  pkgconfig(libmnl)

Provides:       wireguard-tools = %{epoch}:%{version}-%{release}
Requires:       wireguard-dkms

%description
WireGuard is a novel VPN that runs inside the Linux Kernel and uses
state-of-the-art cryptography (the "Noise" protocol). It aims to be
faster, simpler, leaner, and more useful than IPSec, while avoiding
the massive headache. It intends to be considerably more performant
than OpenVPN. WireGuard is designed as a general purpose VPN for
running on embedded interfaces and super computers alike, fit for
many different circumstances. It runs over UDP.

This package provides the wg binary for controling WireGuard.

%prep
%setup -q -n WireGuard-%{version}

%build
cd %{_builddir}/WireGuard-%{version}/src
make tools

%install
mkdir -p %{buildroot}%{_bindir}
cd %{_builddir}/WireGuard-%{version}/src/tools
DESTDIR=%{buildroot} BINDIR=%{_bindir} MANDIR=%{_mandir} RUNSTATEDIR=/run \
    make install
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}/examples/
cp -fr %{_builddir}/WireGuard-%{version}/contrib/examples/* \
    %{buildroot}%{_defaultdocdir}/%{name}/examples/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%attr(0755, root, root) %{_bindir}/wg
%attr(0755, root, root) %{_bindir}/wg-quick
%attr(0644, root, root) %{_datarootdir}/bash-completion/completions/wg
%attr(0644, root, root) %{_datarootdir}/bash-completion/completions/wg-quick
%attr(0644, root, root) %{_unitdir}/wg-quick@.service
%attr(0644, root, root) %{_mandir}/man8/wg.8*
%attr(0644, root, root) %{_mandir}/man8/wg-quick.8*
%{_defaultdocdir}/%{name}/examples

%doc README.md
%license COPYING
%{!?_licensedir:%global license %doc}

%changelog
* Mon Jul 31 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170726-1
- Update to 0.0.20170726

* Thu Jun 29 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170629-1
- Update to 0.0.20170629

* Tue Jun 13 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170613-1
- Update to 0.0.20170613

* Mon Jun 12 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170612-1
- Update to 0.0.20170612

* Wed May 31 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170531-1
- Update to 0.0.20170531

* Wed May 17 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170517-1
- Update to 0.0.20170517

* Mon Apr 24 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170421-1
- Update to 0.0.20170421

* Mon Apr 10 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170409-1
- Update to 0.0.20170409

* Fri Mar 24 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170324-1
- Update to 0.0.20170324

* Mon Mar 20 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170320.1-1
- Update to 0.0.20170320.1

* Thu Mar 2 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170223-1
- Update to 0.0.20170223

* Thu Feb 16 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170214-1
- Update to 0.0.20170214

* Thu Jan 5 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170105-1
- Update to 0.0.20170105
- Add wg-quick, bash-completion, and systemd service

* Mon Dec 19 2016 Jason A. Donenfeld <jason@zx2c4.com> - 0.0.20161218-1
- Spec adjustments

* Wed Aug 17 2016 Joe Doss <joe@solidadmin.com> - 0.0.20160808-2
- Spec adjustments

* Mon Aug 15 2016 Joe Doss <joe@solidadmin.com> - 0.0.20160808-1
- Initial WireGuard Tools RPM
- Version 0.0.20160808
