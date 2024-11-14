%define libname %mklibname aquamarine
%define devname %mklibname -d aquamarine

%define api 3

Name:           aquamarine
Version:        0.4.5
Release:        2
Summary:        A very light linux rendering backend library
License:        BSD-3-Clause
Group:          Hyprland
URL:            https://github.com/hyprwm/aquamarine
Source0:        https://github.com/hyprwm/aquamarine/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  egl-devel
BuildRequires:  pkgconfig(opengl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(hwdata)
BuildRequires:  pkgconfig(hyprutils)
BuildRequires:  pkgconfig(hyprwayland-scanner)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)

%description
Aquamarine is a very light linux rendering backend library. 
It provides basic abstractions for an application to render on a Wayland session (in a window) or a native DRM session.
It is agnostic of the rendering API (Vulkan/OpenGL) and designed to be lightweight, performant, and minimal.
Aquamarine provides no bindings for other languages. It is C++-only.

%package -n %{libname}
Summary:        Shared library for %{name}
Provides:  aquamarine

%description -n %{libname}
This package contains the shared library files.

%package -n %{devname}
Summary:  Development files for %{name}
Requires: %{libname} = %{EVRD}
Provides: aquamarine-devel

%description -n %{devname}
Development files for %{name}.

%prep
%autosetup -p1

%build
export CC=gcc
export CXX=g++
%cmake
%make_build

%install
%make_install -C build

%files -n %{libname} 
%license LICENSE
%doc README.md docs/env.md
%{_libdir}/lib%{name}.so.%{version}
%{_libdir}/lib%{name}.so.%{api}

%files -n %{devname}
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
