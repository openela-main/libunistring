# This spec file has been automatically updated
Version:	0.9.9
Release: 3%{?dist}
Name: libunistring
Group: System Environment/Libraries
Summary: GNU Unicode string library
License: GPLv2+ or LGPLv3+
Url: http://www.gnu.org/software/libunistring/
Source0: http://ftp.gnu.org/gnu/libunistring/%{name}-%{version}.tar.xz
Patch0:  fseterr-update-20180815.patch
Requires(post): info
Requires(preun): info
Provides: bundled(gnulib)

%description
This portable C library implements Unicode string types in three flavours:
(UTF-8, UTF-16, UTF-32), together with functions for character processing
(names, classifications, properties) and functions for string processing
(iteration, formatted output, width, word breaks, line breaks, normalization,
case folding and regular expressions).

%package devel
Group: Development/Libraries
Summary: GNU Unicode string library - development files
Requires: %{name} = %{version}-%{release}

%description devel
Development files for programs using libunistring.

%prep
%setup -q
%patch0 -p1 -b .fseterr-update

%build
%configure --disable-static --disable-rpath
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir
rm -f $RPM_BUILD_ROOT/%{_libdir}/%{name}.la
# Move staged docs so not picked up by %%doc in main package
mv $RPM_BUILD_ROOT%{_datadir}/doc/%{name} __doc

%files
%defattr(-,root,root,-)
%license COPYING COPYING.LIB
%doc AUTHORS NEWS README
%{_libdir}/%{name}.so.*

%files devel
%defattr(-,root,root,-)
%doc HACKING DEPENDENCIES THANKS ChangeLog
%doc __doc/*
%{_infodir}/%{name}.info*
%{_libdir}/%{name}.so
%{_includedir}/unistring
%{_includedir}/*.h

%ldconfig_scriptlets

%post devel
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir || :

%preun devel
if [ $1 = 0 ]; then
   /sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir || :
fi

%changelog
* Fri Aug 17 2018 Mike FABIAN <mfabian@redhat.com> - 0.9.9-3
- Fix invalid license tag
- Resolves: rhbz#1611728

* Wed Aug 15 2018 Mike FABIAN <mfabian@redhat.com> - 0.9.9-2
- update fseterr from current gnulib to make it build on RHEL-8
- Resolves: rhbz#1611728

* Thu Mar 01 2018 Daiki Ueno <dueno@redhat.com> - 0.9.9-1
- Update to upstream 0.9.9 release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.8-2
- Switch to %%ldconfig_scriptlets

* Sat Dec  2 2017 Daiki Ueno <dueno@redhat.com> - 0.9.8-1
- Update to 0.9.8

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 17 2017 Daiki Ueno <dueno@redhat.com> - 0.9.7-1
- Update to 0.9.7
- Update license to "GPLv2+ or LGPLv2+"

* Wed Feb 01 2017 Stephen Gallagher <sgallagh@redhat.com> - 0.9.4-4
- Add missing %%license macro

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Sep 02 2014 Pádraig Brady <pbrady@redhat.com> - 0.9.4-1
- Latest upstream

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 29 2013 Pádraig Brady <P@draigBrady.com> 0.9.3-9
- Adjust to avoid duplicate docs caused by %%doc macro changes in Fedora 20

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 26 2012 Akira TAGOH <tagoh@redhat.com> - 0.9.3-5
- Fix a typo in %%preun. (#737638)

* Tue May 15 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.9.3-4
- Add bundled(gnulib) provides

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun May 23 2010 Pádraig Brady <P@draigBrady.com> 0.9.3-1
- Update to 0.9.3

* Thu Nov 19 2009 Pádraig Brady <P@draigBrady.com> 0.9.1-3
- Remove glibc-devel and texinfo build deps

* Thu Nov 19 2009 Pádraig Brady <P@draigBrady.com> 0.9.1-2
- Changes as per initial review by panemade@gmail.com

* Tue Nov 17 2009 Pádraig Brady <P@draigBrady.com> 0.9.1-1
- Initial version
