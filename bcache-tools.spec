Summary:	Userspace tools for bcache
Summary(pl.UTF-8):	Narzędzia przestrzeni użytkownika do bcache
Name:		bcache-tools
Version:	1.0.4
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	https://github.com/g2p/bcache-tools/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	1d510401744326ae7c813dc1eb927642
URL:		http://bcache.evilpiepirate.org/
BuildRequires:	libblkid-devel
BuildRequires:	libuuid-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These are the userspace tools required for bcache.

Bcache is a patch for the Linux kernel to use SSDs to cache other
block devices.

%description -l pl.UTF-8
Ten pakiet zawiera narzędzia przestrzeni użytkownika wymagane przez
mechanizm bcache.

Bcache to łata na jądro Linuksa, pozwalająca wykorzystywać dyski SSD
jako pamięć podręczną dla innych urządzeń blokowych.

%prep
%setup -q

%build
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},/lib/udev/rules.d,%{_datadir}/initramfs-tools/hooks,/lib/dracut/modules.d,%{_mandir}/man8}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/bcache-super-show
%attr(755,root,root) %{_sbindir}/make-bcache
%attr(755,root,root) /lib/udev/bcache-register
%attr(755,root,root) /lib/udev/probe-bcache
/lib/udev/rules.d/69-bcache.rules
%{_mandir}/man8/bcache-super-show.8*
%{_mandir}/man8/make-bcache.8*
%{_mandir}/man8/probe-bcache.8*
# dracut subpackage?
%dir /lib/dracut/modules.d/90bcache
%attr(755,root,root) /lib/dracut/modules.d/90bcache/module-setup.sh
# initramfs-tools subpackage?
%attr(755,root,root) %{_datadir}/initramfs-tools/hooks/bcache
