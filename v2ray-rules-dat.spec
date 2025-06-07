%global forgeurl  https://github.com/Loyalsoldier/v2ray-rules-dat
%global tag       202506062213
Version:          %{tag}

%forgemeta

Name:             v2ray-rules-dat
Release:          1%{?dist}
Summary:          Enhanced edition of V2Ray rules dat files
License:          GPLv3
URL:              %{forgeurl}
Source0:          %{forgesource}
Source1:          %{forgeurl}/releases/download/%{tag}/geoip.dat
Source2:          %{forgeurl}/releases/download/%{tag}/geosite.dat
BuildArch:        noarch

Obsoletes:        v2ray-geoip < 202103160000-1
Obsoletes:        v2ray-domain-list-community < 20210316000000-1

%description
Enhanced edition of V2Ray rules dat files.
Compatible with Xray-core, Shadowsocks-windows, Trojan-Go and leaf.


%prep
%forgesetup


%build
# There is nothing to do.


%install
install -m 0755 -vd        %{buildroot}%{_datadir}/v2ray
install -m 0644 -vp %{S:1} %{buildroot}%{_datadir}/v2ray/geoip.dat
install -m 0644 -vp %{S:2} %{buildroot}%{_datadir}/v2ray/geosite.dat


%files
%license LICENSE
%{_datadir}/v2ray/geoip.dat
%{_datadir}/v2ray/geosite.dat


%changelog
* Tue Mar 16 2021 sixg0000d <sixg0000d@gmail.com> - 202103160825-1
- Initial v2ray-rules-dat
