%define _enable_debug_packages %{nil}
%define debug_package %{nil}

%define major 5
%define libname %mklibname Qt4Pas %{major}
%define devname %mklibname Qt4Pas -d

Summary:	Free Pascal Qt4 binding
Name:		qt4pas
# defined in .pro file inside source tarball
Version:	5.2.5
Release:	4
License:	LGPLv3+
Group:		System/Libraries
Url:		https://users.telenet.be/Jan.Van.hijfte/qtforfpc/fpcqt4.html
Source0:	qt4pas-V2.5_Qt4.5.3.tar.gz
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(QtWebKit)

%description
The Free Pascal Qt4 binding that allows Free Pascal
to interface with the C++ Library Qt.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Free Pascal Qt4 binding
Group:		System/Libraries

%description -n %{libname}
The Free Pascal Qt4 binding that allows Free Pascal
to interface with the C++ Library Qt.

%files -n %{libname}
%{_libdir}/libQt4Pas.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Free Pascal Qt4 binding
Group:		Development/Other
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
The Free Pascal Qt4 binding that allows Free Pascal
to interface with the C++ Library Qt.

%files -n %{devname}
%{_libdir}/libQt4Pas.so

#----------------------------------------------------------------------------

%prep
%setup -q -n qt4pas-V2.5_Qt4.5.3

%build
%qmake_qt4 Qt4Pas.pro
%make

%install
make install INSTALL_ROOT=%{buildroot}

