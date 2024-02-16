# Based on Fedora packaging

Name:           vulkan-headers
Version:        1.3.277
Release:        1
Summary:        Vulkan Header files and API registry
License:        ASL 2.0 or MIT
URL:            https://github.com/KhronosGroup/Vulkan-Headers
Source0:        vulkan-headers-%{version}.tar.gz

BuildRequires:  cmake
BuildArch:      noarch

%description
Vulkan Header files and API registry

%prep
%autosetup -n %{name}-%{version}/%{name}

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE.md LICENSES/Apache-2.0.txt LICENSES/MIT.txt
%doc README.md
%{_includedir}/vulkan/
%{_includedir}/vk_video/
%dir %{_datadir}/cmake/VulkanHeaders/
%dir %{_datadir}/vulkan/
%{_datadir}/cmake/VulkanHeaders/*.cmake
%{_datadir}/vulkan/registry/
