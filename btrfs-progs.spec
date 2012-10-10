Name:           btrfs-progs
Version:        0.19.20120817git043a639
Release:        2%{?dist}
Summary:        Userspace programs for btrfs

Group:          System Environment/Base
License:        GPLv2
URL:            http://btrfs.wiki.kernel.org/index.php/Main_Page
Source0:	%{name}-%{version}.tar.bz2
Patch0: btrfs-progs-fix-labels.patch
Patch1: btrfs-progs-valgrind.patch
Patch2: btrfs-progs-build-fixes.patch
Patch3: Btrfs-progs-add-btrfs-device-ready-command.patch
Patch4: Btrfs-progs-detect-if-the-disk-we-are-formatting-is-.patch
Patch5: Btrfs-progs-only-enforce-a-maximum-size-if-we-specif.patch
Patch6: btrfs-init-dev-list.patch
Patch7: btrfs-progs-correct-uninitialized-fsid-variable.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  e2fsprogs-devel, libuuid-devel, zlib-devel, libacl-devel, libblkid-devel

%define _root_sbindir /sbin

%description
The btrfs-progs package provides all the userpsace programs needed to create,
check, modify and correct any inconsistencies in the btrfs filesystem.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
make CFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make mandir=%{_mandir} bindir=%{_sbindir} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING INSTALL
%{_sbindir}/btrfsctl
%{_sbindir}/btrfsck
%{_sbindir}/mkfs.btrfs
%{_sbindir}/btrfs-debug-tree
%{_sbindir}/btrfs-image
%{_sbindir}/btrfs-show
%{_sbindir}/btrfs-vol
%{_sbindir}/btrfs-convert
%{_sbindir}/btrfstune
%{_sbindir}/btrfs
%{_sbindir}/btrfs-map-logical
%{_sbindir}/btrfs-zero-log
%{_sbindir}/btrfs-restore
%{_sbindir}/btrfs-find-root
%{_mandir}/man8/btrfs-image.8.gz
%{_mandir}/man8/btrfs-show.8.gz
%{_mandir}/man8/btrfsck.8.gz
%{_mandir}/man8/btrfsctl.8.gz
%{_mandir}/man8/mkfs.btrfs.8.gz
%{_mandir}/man8/btrfs.8.gz

%changelog
* Wed Oct 10 2012 Richard W.M. Jones <rjones@redhat.com> 0.19.20120817git043a639-2
- Add upstream patch to correct uninitialized fsid variable
  (possible fix for RHBZ#863978).

* Fri Aug 17 2012 Josef Bacik <josef@toxicpanda.com> 0.19.20120817git043a639-1
- update to latest btrfs-progs

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 25 2012 Josef Bacik <josef@toxicpanda.com> 0.19-19
- make btrfs filesystem show <uuid> actually work (rhbz# 816293)

* Wed Apr 11 2012 Josef Bacik <josef@toxicpanda.com> 0.19-18
- updated to latest btrfs-progs

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Aug 05 2011 Josef Bacik <josef@toxicpanda.com> 0.19-16
- fix build-everything patch to actually build everything

* Fri Aug 05 2011 Josef Bacik <josef@toxicpanda.com> 0.19-15
- actually build btrfs-zero-log

* Thu Aug 04 2011 Josef Bacik <josef@toxicpanda.com> 0.19-14
- bring btrfs-progs uptodate with upstream

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Aug 20 2010 Adam Tkac <atkac redhat com> 0.19-12
- rebuild to ensure F14 has bigger NVR than F13

* Wed Mar 24 2010 Josef Bacik <josef@toxicpanda.com> 0.19-11
- bring btrfs-progs uptodate with upstream, add btrfs command and other
  features.

* Thu Mar 11 2010 Josef Bacik <josef@toxicpanda.com> 0.19-10
- fix dso linking issue and bring btrfs-progs uptodate with upstream

* Tue Feb 2 2010 Josef Bacik <josef@toxicpanda.com> 0.19-9
- fix btrfsck so it builds on newer glibcs

* Tue Feb 2 2010 Josef Bacik <josef@toxicpanda.com> 0.19-8
- fix btrfsctl to return 0 on success and 1 on failure

* Tue Aug 25 2009 Josef Bacik <josef@toxicpanda.com> 0.19-7
- add btrfs-progs-valgrind.patch to fix memory leaks and segfaults

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Josef Bacik <josef@toxicpanda.com> 0.19-5
- add e2fsprogs-devel back to BuildRequires since its needed for the converter

* Wed Jul 15 2009 Josef Bacik <josef@toxicpanda.com> 0.19-4
- change BuildRequires for e2fsprogs-devel to libuuid-devel

* Fri Jun 19 2009 Josef Bacik <josef@toxicpanda.com> 0.19-3
- added man pages to the files list and made sure they were installed properly

* Fri Jun 19 2009 Josef Bacik <josef@toxicpanda.com> 0.19-2
- add a patch for the Makefile to make it build everything again

* Fri Jun 19 2009 Josef Bacik <josef@toxicpanda.com> 0.19-1
- update to v0.19 of btrfs-progs for new format

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

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
