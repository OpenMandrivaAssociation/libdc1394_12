%define oname libdc1394
%define major 12
%define libname %mklibname dc1394_ %{major}
%define develname %mklibname dc1394_ %major -d

Summary:	Library for 1394 Digital Camera Specification
Name:		libdc1394_12
Version:	1.2.1
Release:	14
License:	GPLv2+
Group:		System/Libraries
URL:		http://sourceforge.net/projects/libdc1394/
Source0:	%{oname}-%{version}.tar.bz2
Patch0:		libdc1394-0.9.5-lib64.patch
Patch1:		libdc1394-1.2.1-clk_tck-deprecated.patch
Patch2:		libdc1394-1.2.1-videodev.h.patch
Patch3:		libdc1394-automake-1.13.patch
BuildRequires: 	pkgconfig(libraw1394)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xv)
BuildRequires:	pkgconfig(libv4l1)

%description
libdc1394 is a library that is intended to provide a high level programming
interface for application developers who wish to control IEEE 1394 based
cameras that conform to the 1394-based Digital Camera Specification (found at
http://www.1394ta.org/).

%if %{_lib} != lib
%package -n 	%{libname}
Summary:	Dynamic library from libdc1394
Group:		System/Libraries

%description -n %{libname}
libdc1394 is a library that is intended to provide a high level programming
interface for application developers who wish to control IEEE 1394 based
cameras that conform to the 1394-based Digital Camera Specification (found at
http://www.1394ta.org/).
%endif

%package -n 	%{develname}
Summary: 	Development components for libdc1394
Group: 		Development/C
Requires: 	%{libname} = %{version}-%{release}
Provides: 	libdc1394_12-devel = %{version}-%{release}
Conflicts:	%mklibname -d dc1394

%description -n %{develname}
libdc1394 is a library that is intended to provide a high level programming
interface for application developers who wish to control IEEE 1394 based
cameras that conform to the 1394-based Digital Camera Specification (found at
http://www.1394ta.org/).

This archive contains the header-files for libdc1394 development

%prep
%setup -q -n %{oname}-%{version}
%patch0 -p1 -b .lib64
%patch1 -p1 -b .clk_tck
%patch2 -p0 -b .v4l
%patch3 -p1 -b .am113~
autoreconf -fi

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%if %{_lib} == lib
%files
%else
%files -n %{libname}
%endif
%doc AUTHORS ChangeLog NEWS README 
%{_libdir}/libdc1394_control.so.%{major}*

%files -n %{develname}
%{_bindir}/dc1394_vloopback
%{_includedir}/libdc1394
%{_libdir}/*.so


%changelog
* Mon May 02 2011 Funda Wang <fwang@mandriva.org> 1.2.1-12mdv2011.0
+ Revision: 662435
- fix build with latest kernel

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Sat Feb 05 2011 Funda Wang <fwang@mandriva.org> 1.2.1-11
+ Revision: 636026
- rebuild
- tighten BR

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-10mdv2011.0
+ Revision: 602536
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-9mdv2010.1
+ Revision: 520763
- rebuilt for 2010.1

* Tue Sep 22 2009 Götz Waschk <waschk@mandriva.org> 1.2.1-8mdv2010.0
+ Revision: 447467
- rebuild

* Tue Sep 22 2009 Götz Waschk <waschk@mandriva.org> 1.2.1-7mdv2010.0
+ Revision: 447446
- add conflict with 2.x version of libdc1394
- fix build
- branch 1.x version for ptlib

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 1.2.1-5mdv2008.1
+ Revision: 150549
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Aug 31 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-4mdv2008.0
+ Revision: 76780
- new devel naming
- reconstruct the autofoo toolchain

