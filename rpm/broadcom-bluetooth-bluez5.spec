Name: broadcom-bluetooth-bluez5
Summary: Broadcom Bluetooth utilities
URL: https://code.google.com/p/broadcom-bluetooth/
Version: 1.0.5
Release: 1
License: Apache 2.0
Source0: %{name}-%{version}.tar.bz2
Requires: bluez5-libs
BuildRequires: bluez5-libs-devel
Conflicts: broadcom-bluetooth
Obsoletes: broadcom-bluetooth <= 1.0.4

%description
Broadcom Bluetooth utilities

%prep
%autosetup -n %{name}-%{version}/broadcom-bluetooth

%build
%make_build

%install
%make_install

%files
%{_sbindir}/brcm_patchram_plus
%{_sbindir}/brcm_patchram_plus_h5
%{_sbindir}/brcm_patchram_plus_usb
