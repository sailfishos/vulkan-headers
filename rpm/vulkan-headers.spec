# Based on Fedora packaging

Name:           vulkan-headers
Version:        1.2.183.0
Release:        1
Summary:        Vulkan Header files and API registry
License:        ASL 2.0
URL:            https://github.com/KhronosGroup/Vulkan-Headers
Source0:        vulkan-headers-%{version}.tar.gz

BuildRequires:  cmake
BuildArch:      noarch

%description
Vulkan Header files and API registry

%prep
%autosetup -n %{name}-%{version}/%{name}

%build
%cmake .
%make_build

%install
%make_install

%files
%license LICENSE.txt
%doc README.md
%{_includedir}/vulkan/
%{_includedir}/vk_video/
%dir %{_datadir}/vulkan/
%{_datadir}/vulkan/registry/
