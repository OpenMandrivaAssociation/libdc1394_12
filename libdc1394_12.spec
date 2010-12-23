%define oname libdc1394
%define major 12
%define libname %mklibname dc1394_ %{major}
%define develname %mklibname dc1394_ %major -d

Summary: 	Library for 1394 Digital Camera Specification
Name: 		libdc1394_12
Version: 	1.2.1
Release: 	%mkrel 10
License: 	GPLv2+
Group: 		System/Libraries
URL: 		http://sourceforge.net/projects/libdc1394/
Source0: 	%{oname}-%{version}.tar.bz2
Patch0:		libdc1394-0.9.5-lib64.patch
Patch1:		libdc1394-1.2.1-clk_tck-deprecated.patch
BuildRequires: 	libraw1394_8-devel
BuildRequires:	libx11-devel
BuildRequires:	libxv-devel
Buildroot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
libdc1394 is a library that is intended to provide a high level programming
interface for application developers who wish to control IEEE 1394 based
cameras that conform to the 1394-based Digital Camera Specification (found at
http://www.1394ta.org/).

%if %_lib != lib
%package -n 	%{libname}
Summary: 	Dynamic library from libdc1394
Group: 		System/Libraries

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
%setup -q -n %oname-%version
%patch0 -p1 -b .lib64
%patch1 -p1 -b .clk_tck
autoreconf -fi

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%if %_lib == lib
%files
%else
%files -n %{libname}
%endif
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README 
%{_libdir}/libdc1394_control.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_bindir}/dc1394_vloopback
%{_includedir}/libdc1394
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
