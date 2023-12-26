%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-rmw-implementation
Version:        2.15.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rmw_implementation package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-rolling-rmw-implementation-packages(member)
%if 0%{?with_weak_deps}
Recommends:     ros-rolling-rmw-fastrtps-cpp
%endif

Requires:       ros-rolling-ament-index-cpp
Requires:       ros-rolling-rcpputils
Requires:       ros-rolling-rcutils
Requires:       ros-rolling-rmw-implementation-cmake
Requires:       ros-rolling-ros-workspace
BuildRequires:  ros-rolling-ament-cmake
BuildRequires:  ros-rolling-ament-index-cpp
BuildRequires:  ros-rolling-rcpputils
BuildRequires:  ros-rolling-rcutils
BuildRequires:  ros-rolling-rmw
BuildRequires:  ros-rolling-rmw-cyclonedds-cpp
BuildRequires:  ros-rolling-rmw-fastrtps-cpp
BuildRequires:  ros-rolling-rmw-fastrtps-dynamic-cpp
BuildRequires:  ros-rolling-rmw-implementation-cmake
BuildRequires:  ros-rolling-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-rolling-ament-cmake-gtest
BuildRequires:  ros-rolling-ament-lint-auto
BuildRequires:  ros-rolling-ament-lint-common
BuildRequires:  ros-rolling-performance-test-fixture
%endif

%description
Proxy implementation of the ROS 2 Middleware Interface.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/rolling" \
    -DAMENT_PREFIX_PATH="/opt/ros/rolling" \
    -DCMAKE_PREFIX_PATH="/opt/ros/rolling" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Tue Dec 26 2023 William Woodall <william@openrobotics.org> - 2.15.0-1
- Autogenerated by Bloom

* Wed Oct 04 2023 William Woodall <william@openrobotics.org> - 2.14.0-1
- Autogenerated by Bloom

* Thu Apr 27 2023 William Woodall <william@openrobotics.org> - 2.13.0-1
- Autogenerated by Bloom

* Tue Apr 11 2023 William Woodall <william@openrobotics.org> - 2.12.0-1
- Autogenerated by Bloom

* Fri Mar 24 2023 William Woodall <william@openrobotics.org> - 2.11.0-3
- Autogenerated by Bloom

* Tue Mar 21 2023 William Woodall <william@openrobotics.org> - 2.11.0-2
- Autogenerated by Bloom

