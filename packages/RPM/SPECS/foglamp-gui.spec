%define __spec_install_pre /bin/true

Name:          foglamp-gui
Vendor:        Dianomic Systems, Inc. <info@dianomic.com>
Version:       __VERSION__
Release:       1
BuildArch:     __ARCH__
Summary:       FogLAMP GUI
License:       Apache License
Group:         IoT
URL:           http://www.dianomic.com

%description
	FogLAMP GUI

%pre
#!/usr/bin/env bash
echo "Installing FogLAMP GUI"
stop_nginx_service () {
    sudo systemctl stop nginx
}

stop_nginx_service


%preun
#!/usr/bin/env bash
PKG_NAME="foglamp-gui"

%post
#!/usr/bin/env bash
set -e

set_files_ownership () {
    chown -R root:root usr/share/nginx/html/*
}

start_nginx_service () {
    sudo systemctl start nginx
    sudo systemctl status nginx | grep "Active:"
}

set_files_ownership
start_nginx_service

%files
/usr/share/nginx/html/*
