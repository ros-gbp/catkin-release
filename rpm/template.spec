Name:           ros-melodic-catkin
Version:        0.7.15
Release:        0%{?dist}
Summary:        ROS catkin package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/catkin
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       cmake
Requires:       gmock-devel
Requires:       gtest-devel
Requires:       python
Requires:       python-catkin_pkg > 0.4.3
Requires:       python-empy
Requires:       python-nose
BuildRequires:  cmake
BuildRequires:  python
BuildRequires:  python-catkin_pkg > 0.4.3
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
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Mon Mar 04 2019 Dirk Thomas <dthomas@osrfoundation.org> - 0.7.15-0
- Autogenerated by Bloom

* Wed Jun 06 2018 Dirk Thomas <dthomas@osrfoundation.org> - 0.7.14-0
- Autogenerated by Bloom

* Thu May 31 2018 Dirk Thomas <dthomas@osrfoundation.org> - 0.7.13-0
- Autogenerated by Bloom

* Tue May 01 2018 Dirk Thomas <dthomas@osrfoundation.org> - 0.7.12-0
- Autogenerated by Bloom

* Fri Feb 02 2018 Dirk Thomas <dthomas@osrfoundation.org> - 0.7.11-0
- Autogenerated by Bloom

* Wed Jan 24 2018 Dirk Thomas <dthomas@osrfoundation.org> - 0.7.10-0
- Autogenerated by Bloom

* Mon Jan 22 2018 Dirk Thomas <dthomas@osrfoundation.org> - 0.7.9-0
- Autogenerated by Bloom

