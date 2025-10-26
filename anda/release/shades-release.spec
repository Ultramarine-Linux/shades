%global is_rawhide 0

%global release_name Gas Meter
%global fedora_codename Forty Three
%global codename gas_meter
%define dist_version 43

%if %{is_rawhide}
%define bug_version rawhide
%define releasever rawhide
%define doc_version rawhide
%else
%define bug_version %{dist_version}
%define releasever %{dist_version}
%define doc_version f%{dist_version}
%endif

%bcond_without sway
%endif

%dnl %if %{with flagship} || %{with plasma} || %{with gnome} || %{with xfce} || %{with atomic_flagship} || %{with atomic_plasma} || %{with atomic_gnome} || %{with atomic_xfce}
%dnl %global with_desktop 1
%dnl %endif

## ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
## ┃ Ultramarine Linux Shades Release Package ┃
## ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

Summary:	Ultramarine Linux Shades release files
%dnl Name:		ultramarine-shades-release
Version:	%{dist_version}
Release:	1%{?dist}
License:	MIT
Source0:	LICENSE
URL:        https://ultramarine-linux.org
Recommends: ultramarine-release-identity-basic
BuildArch:  noarch

Provides:   ultramarine-shades-release = %{version}-%{release}
Provides:   ultramarine-shades-release-variant = %{version}-%{release}

Provides:   system-shades-release
Provides:   system-shades-release(%{version})
Provides:   base-shades-module(platform:f%{version})

Requires:   ultramarine-release-common = %{version}-%{release}

Source70:   sway-stuff

BuildRequires:    systemd-rpm-macros

%description
Release files for Ultramarine Linux Shades.

# Create os-release files for the different editions
%if %{with sway}
# sway
cp -p os-release \
      %{buildroot}%{_prefix}/lib/os-release.basic
%endif

# Install licenses
mkdir -p licenses
install -pm 0644 %{SOURCE0} licenses/LICENSE

%files
%license LICENSE

%files common

%if %{with basic}
%files

%endif

%files notes
%doc readme/README.Ultramarine-Release-Notes

%changelog
%autochangelog
