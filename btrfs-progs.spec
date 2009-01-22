Name:           btrfs-progs
Version:        0.18
Release:        3%{?dist}
Summary:        Userspace programs for btrfs

Group:          System Environment/Base
License:        GPLv2
URL:            http://btrfs.wiki.kernel.org/index.php/Main_Page
Source0:        http://www.kernel.org/pub/linux/kernel/people/mason/btrfs/%{name}-%{version}.tar.bz2
Patch0: btrfs-progs-fix-labels.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  e2fsprogs-devel, zlib-devel, libacl-devel

%define _root_sbindir /sbin

%description
The btrfs-progs package provides all the userpsace programs needed to create,
check, modify and correct any inconsistencies in the btrfs filesystem.

%prep
%setup -q
%patch0 -p1

%build
make CFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}
make CFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags} convert

%install
rm -rf $RPM_BUILD_ROOT
make bindir=%{_root_sbindir} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING INSTALL
%{_root_sbindir}/btrfsctl
%{_root_sbindir}/btrfsck
%{_root_sbindir}/mkfs.btrfs
%{_root_sbindir}/btrfs-debug-tree
%{_root_sbindir}/btrfs-image
%{_root_sbindir}/btrfs-show
%{_root_sbindir}/btrfs-vol
%{_root_sbindir}/btrfs-convert
%{_root_sbindir}/btrfstune

%changelog
* Thu Jan 22 2009 Josef Bacik <josef@toxicpanda.com> 0.18-3
- updated label patch

* Thu Jan 22 2009 Josef Bacik <josef@toxicpanda.com> 0.18-2
- add a patch to handle having /'s in labels

* Sat Jan 17 2009 Josef Bacik <josef@toxicpanda.com> 0.18-1
- updated to 0.18 because of the ioctl change in 2.6.29-rc2

* Fri Jan 16 2009 Marek Mahut <mmahut@fedoraproject.org> 0.17-4
- RHBZ#480219 btrfs-convert is missing

* Mon Jan 12 2009 Josef Bacik <josef@toxicpanda.com> 0.17-2
- fixed wrong sources upload

* Mon Jan 12 2009 Josef Bacik <josef@toxicpanda.com> 0.17
- Upstream release 0.17

* Sat Jan 10 2009 Kyle McMartin <kyle@redhat.com> 0.16.git1-1
- Upstream git sync from -g72359e8 (needed for kernel...)

* Sat Jan 10 2009 Marek Mahut <mmahut@fedoraproject.org> 0.16-1
- Upstream release 0.16

* Mon Jun 25 2008 Josef Bacik <josef@toxicpanda.com> 0.15-4
-use fedoras normal CFLAGS

* Mon Jun 23 2008 Josef Bacik <josef@toxicpanda.com> 0.15-3
-Actually defined _root_sbindir
-Fixed the make install line so it would install to the proper dir

* Mon Jun 23 2008 Josef Bacik <josef@toxicpanda.com> 0.15-2
-Removed a . at the end of the description
-Fixed the copyright to be GPLv2 since GPL doesn't work anymore

* Mon Jun 23 2008 Josef Bacik <josef@toxicpanda.com> 0.15-1
-Initial build
