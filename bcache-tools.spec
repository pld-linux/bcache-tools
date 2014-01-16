Summary:	Userspace tools for bcache
Summary(pl.UTF-8):	Narzędzia przestrzeni użytkownika do bcache
Name:		bcache-tools
Version:	1.0.5
Release:	2
License:	GPL v2
Group:		Applications/System
Source0:	https://github.com/g2p/bcache-tools/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	5f013fa499d1923a5bf282b59fbcf7ba
URL:		http://bcache.evilpiepirate.org/
BuildRequires:	libblkid-devel
BuildRequires:	libuuid-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
Requires:	uname(release) >= 3.10
Requires:	util-linux >= 2.24
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dracutlibdir	%{_prefix}/lib/dracut

%description
These are the userspace tools required for bcache.

Bcache is a patch for the Linux kernel to use SSDs to cache other
block devices.

%description -l pl.UTF-8
Ten pakiet zawiera narzędzia przestrzeni użytkownika wymagane przez
mechanizm bcache.

Bcache to łata na jądro Linuksa, pozwalająca wykorzystywać dyski SSD
jako pamięć podręczną dla innych urządzeń blokowych.

%package -n dracut-bcache
Summary:	bcache support for Dracut
Summary(pl.UTF-8):	Obsługa bcache dla Dracuta
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	dracut >= 0.31

%description -n dracut-bcache
bcache support for Dracut.

%description -n dracut-bcache -l pl.UTF-8
Obsługa bcache dla Dracuta.

%prep
%setup -q

%build
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},/lib/udev/rules.d,%{_mandir}/man8}

%{__make} install \
	DRACUTLIBDIR=%{dracutlibdir} \
	DESTDIR=$RPM_BUILD_ROOT

# not supported in pld
# initramfs-tools subpackage?
%{__rm} $RPM_BUILD_ROOT%{_datadir}/initramfs-tools/hooks/bcache

# not supported in pld
%{__rm} $RPM_BUILD_ROOT%{_prefix}/lib/initcpio/install/bcache

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

%files -n dracut-bcache
%defattr(644,root,root,755)
%dir %{dracutlibdir}/modules.d/90bcache
%attr(755,root,root) %{dracutlibdir}/modules.d/90bcache/module-setup.sh
