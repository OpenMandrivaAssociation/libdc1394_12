%define oname libdc1394
%define major	12
%define libname %mklibname dc1394_ %{major}
%define devname %mklibname dc1394_ %major -d

Summary:	Library for 1394 Digital Camera Specification
Name:		libdc1394_12
Version:	1.2.1
Release:	21
License:	GPLv2+
Group:		System/Libraries
Url:		http://sourceforge.net/projects/libdc1394/
Source0:	%{oname}-%{version}.tar.bz2
Patch0:		libdc1394-0.9.5-lib64.patch
Patch1:		libdc1394-1.2.1-clk_tck-deprecated.patch
Patch2:		libdc1394-1.2.1-videodev.h.patch
Patch3:		libdc1394-automake-1.13.patch
BuildRequires: 	pkgconfig(libraw1394) = 1.3.0
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

%package -n 	%{devname}
Summary: 	Development components for libdc1394
Group: 		Development/C
Requires: 	%{libname} = %{version}-%{release}
Provides: 	libdc1394_12-devel = %{version}-%{release}
Conflicts:	%mklibname -d dc1394

%description -n %{devname}
libdc1394 is a library that is intended to provide a high level programming
interface for application developers who wish to control IEEE 1394 based
cameras that conform to the 1394-based Digital Camera Specification (found at
http://www.1394ta.org/).

This archive contains the header-files for libdc1394 development

%prep
%setup -qn %{oname}-%{version}
%apply_patches
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

%files -n %{devname}
%{_bindir}/dc1394_vloopback
%{_includedir}/libdc1394
%{_libdir}/*.so

