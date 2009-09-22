%define major 12
%define libname %mklibname dc1394_ %{major}
%define develname %mklibname dc1394 -d

Summary: 	Library for 1394 Digital Camera Specification
Name: 		libdc1394
Version: 	1.2.1
Release: 	%mkrel 6
License: 	GPL
Group: 		System/Libraries
URL: 		http://sourceforge.net/projects/libdc1394/
Source0: 	%{name}-%{version}.tar.bz2
Patch0:		libdc1394-0.9.5-lib64.patch
Patch1:		libdc1394-1.2.1-clk_tck-deprecated.patch
BuildRequires: 	libraw1394-devel X11-devel
Requires: 	libraw1394 kernel >= 2.4.2
Buildroot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
libdc1394 is a library that is intended to provide a high level programming
interface for application developers who wish to control IEEE 1394 based
cameras that conform to the 1394-based Digital Camera Specification (found at
http://www.1394ta.org/).

%package -n 	%{libname}
Summary: 	Dynamic library from libdc1394
Group: 		System/Libraries
Provides: 	libdc1394

%description -n %{libname}
libdc1394 is a library that is intended to provide a high level programming
interface for application developers who wish to control IEEE 1394 based
cameras that conform to the 1394-based Digital Camera Specification (found at
http://www.1394ta.org/).

%package -n 	%{develname}
Summary: 	Development components for libdc1394
Group: 		Development/C
Requires: 	%{libname} = %{version}-%{release}
%if "%{_lib}" != "lib"
Provides: 	libdc1394-devel = %{version}-%{release}
%endif
Provides: 	dc1394-devel = %{version}-%{release}
Provides: 	%{mklibname dc1394_ 12 -d} = %{version}
Obsoletes:	%{mklibname dc1394_ 12 -d}

%description -n %{develname}
libdc1394 is a library that is intended to provide a high level programming
interface for application developers who wish to control IEEE 1394 based
cameras that conform to the 1394-based Digital Camera Specification (found at
http://www.1394ta.org/).

This archive contains the header-files for libdc1394 development

%prep
%setup -q 
%patch0 -p1 -b .lib64
%patch1 -p1 -b .clk_tck
export WANT_AUTOCONF_2_1=1
autoreconf
aclocal

%build
%configure2_5x
make

%install
rm -rf %{buildroot}

%makeinstall

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README 
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_bindir}/dc1394_vloopback
%{_includedir}/libdc1394
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
