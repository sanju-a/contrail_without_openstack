# Installing Contrail Networking without openstack

* Clone & use Tony's github page (https://github.com/tonyliu0592/opencontrail/wiki/Libvirt) to install Contrail without Openstack. Complete the steps till section "Install Contrail"

* Clone and use the repo "https://github.com/vshenoy83/bird-bgp-ospf" to install Bird routing stack & the anycast VIP health check and also configure required configuration files. The VIP and the choice of protocol (OSPF vs BGP) can be controlled from the var files under group_vars directory. The Control-data network interface (eth1) IP address and the TOR IP is configured in the hosts file.

* Once bird comes up and running next step is to validate the cluster. This can be done by following steps starting from the section "Libvirt/KVM" https://github.com/tonyliu0592/opencontrail/wiki/Libvirt
 
