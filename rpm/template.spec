Name:           ros-indigo-catkin
Version:        0.6.11
Release:        0%{?dist}
Summary:        ROS catkin package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/catkin
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       cmake
Requires:       gtest-devel
Requires:       python
Requires:       python-catkin_pkg >= 0.2.2
Requires:       python-empy
Requires:       python-nose
BuildRequires:  cmake
BuildRequires:  python
BuildRequires:  python-catkin_pkg >= 0.2.2
BuildRequires:  python-empy
BuildRequires:  python-mock
BuildRequires:  python-nose

%description
Low-level build system macros and infrastructure for ROS.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
#        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Dec 29 2014 Dirk Thomas <dthomas@osrfoundation.org> - 0.6.11-0
- Autogenerated by Bloom

* Mon Dec 22 2014 Dirk Thomas <dthomas@osrfoundation.org> - 0.6.10-0
- Autogenerated by Bloom

