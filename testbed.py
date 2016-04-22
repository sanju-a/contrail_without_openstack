from fabric.api import env

#Management ip addresses of hosts in the cluster
controller1 = 'root@10.1.1.98'
controller2 = 'root@10.1.1.114'
controller3 = 'root@10.1.1.3'
compute1 = 'root@10.1.1.19'
compute2 = 'root@10.1.1.35'


ext_routers = []

#Autonomous system number
router_asn = 64512

#Host from which the fab commands are triggered to install and provision
host_build = 'root@10.1.1.98'

#Role definition of the hosts.
env.roledefs = {
    'all': [controller1, controller2, controller3, compute1, compute2],
    'cfgm': [controller1, controller2, controller3],
    #'openstack': [openstack],
    'control': [controller1, controller2, controller3],
    'compute': [compute1, compute2],
    'collector': [controller1, controller2, controller3],
    'webui': [controller1, controller2, controller3],
    'database': [controller1, controller2, controller3],
    'rabbit': [controller1, controller2, controller3],
    'build': [host_build],
}

#Openstack admin password
env.openstack_admin_password = 'contrail123'

#Hostnames
env.hostnames = {
    'all': ['contrail-node7', 'contrail-node8', 'contrail-node9', 'contrail-node10','contrail-node11']
}

# Passwords of each host
# for passwordless login's no need to set env.passwords,
# instead populate env.key_filename in testbed.py with public key.
env.passwords = {
    controller1: 'c0ntrail123',
    compute1: 'c0ntrail123',
    #backup_node: 'secret',
    host_build: 'c0ntrail123',
}

# SSH Public key file path for passwordless logins
# if env.passwords is not specified.
#env.key_filename = '/root/.ssh/id_dsa.pub'

#For reimage purpose
env.ostypes = {
    controller1:'ubuntu',
    compute1:'ubuntu'
}

env.orchestrator = 'none' # ['openstack', 'vcenter', 'none']

#ntp server the servers should point to
#env.ntp_server = 'ntp.juniper.net'

# OPTIONAL COMPUTE HYPERVISOR CHOICE:
#======================================
# Compute Hypervisor
#env.hypervisor = {
#    host1: 'docker',
#}
#  Specify the hypervisor to be provisioned in the compute node.(Default=libvirt)

# INFORMATION FOR DB BACKUP/RESTORE ..
#=======================================================
#Optional,Backup Host configuration if it is not available then it will put in localhost
#backup_node = 'root@2.2.2.2'

# Optional, Local/Remote location of backup_data path
# if it is not passed it will use default path
#backup_db_path= ['/home/','/root/']
#cassandra backup can be defined either "full" or "custom"
#full -> take complete snapshot of cassandra DB
#custom -> take snapshot except defined in skip_keyspace
#cassandra_backup='custom'  [ MUST OPTION]
#skip_keyspace=["ContrailAnalytics"]  IF cassandra_backup is selected as custom
#service token need to define to do  restore of  backup data
#service_token = '53468cf7552bbdc3b94f'


#OPTIONAL ANALYTICS CONFIGURATION
#================================
# database_dir is the directory where cassandra data is stored
#
# If it is not passed, we will use cassandra's default
# /var/lib/cassandra/data
#
#database_dir = '<separate-partition>/cassandra'
#
# analytics_data_dir is the directory where cassandra data for analytics
# is stored. This is used to seperate cassandra's main data storage [internal
# use and config data] with analytics data. That way critical cassandra's
# system data and config data are not overrun by analytis data
#
# If it is not passed, we will use cassandra's default
# /var/lib/cassandra/data
#
#analytics_data_dir = '<separate-partition>/analytics_data'
#
# ssd_data_dir is the directory where cassandra can store fast retrievable
# temporary files (commit_logs). Giving cassandra an ssd disk for this
# purpose improves cassandra performance
#
# If it is not passed, we will use cassandra's default
# /var/lib/cassandra/commit_logs
#
#ssd_data_dir = '<seperate-partition>/commit_logs_data'

# Following variables allow analytics data to have different TTL in cassandra.
#analytics_config_audit_ttl controls TTL for config audit logs
#analytics_statistics_ttl controls TTL for stats
#analytics_flow_ttl controls TTL for flow data
#database_ttl controls TTL for rest of the data
#
#database_ttl = 48
#analytics_config_audit_ttl = 48
#analytics_statistics_ttl = 48
#analytics_flow_ttl = 48

# Following parameter allows to specify minimum amount of disk space in the
# analytics database partition, if configured amount of space is not present,
# it will fail provisioning.
minimum_diskGB = 32

#OPTIONAL BONDING CONFIGURATION
#==============================
#Inferface Bonding
#bond= {
#    host1 : { 'name': 'bond0', 'member': ['p2p0p0','p2p0p1'], 'mode': '802.3ad', 'xmit_hash_policy': 'layer3+4' },
#}

# OPTIONAL SEPARATION OF MANAGEMENT AND CONTROL + DATA and OPTIONAL VLAN
# INFORMATION
# =======================================================================
#control_data = {
#    controller1 : { 'ip': '10.1.1.98/24', 'gw' : '10.1.1.97', 'device': 'eth1' },
#    controller2 : { 'ip': '10.1.1.114/24', 'gw' : '10.1.1.113', 'device': 'eth1' },
#    controller3 : { 'ip': '10.1.1.3/24', 'gw' : '10.1.1.1', 'device': 'eth1' },
#    compute1 : { 'ip': '10.1.1.19/24', 'gw' : '10.1.1.17', 'device': 'eth1' },
#    compute2 : { 'ip': '10.1.1.35/24', 'gw' : '10.1.1.33', 'device': 'eth1' },
#}

#OPTIONAL STATIC ROUTE CONFIGURATION
#===================================
#static_route  = {
#    controller1 : [{ 'ip': '10.1.1.0', 'netmask' : '255.255.255.0', 'gw':'10.1.1.97', 'intf': 'eth1' }],
#    controller2 : [{ 'ip': '10.1.1.0', 'netmask' : '255.255.255.0', 'gw':'10.1.1.113', 'intf': 'eth1' }],
#    controller3 : [{ 'ip': '10.1.1.0', 'netmask' : '255.255.255.0', 'gw':'10.1.1.1', 'intf': 'eth1' }],
#    compute1 : [{ 'ip': '10.1.1.0', 'netmask' : '255.255.255.0', 'gw':'10.1.1.17', 'intf': 'eth1' }],
#    compute2 : [{ 'ip': '10.1.1.0', 'netmask' : '255.255.255.0', 'gw':'10.1.1.33', 'intf': 'eth1' }],
#}

#storage compute disk config
#storage_node_config = {
#    host1 : { 'disks' : ['sdc', 'sdd'] },
#}

#live migration config
#live_migration = True


#To disable installing contrail interface rename package
env.interface_rename = False

#In environments where keystone is deployed outside of Contrail provisioning
#scripts , you can use the below options
#
# Note :
# "insecure" is applicable only when protocol is https
# The entries in env.keystone overrides the below options which used
# to be supported earlier :
#  service_token
#  keystone_ip
#  keystone_admin_user
#  keystone_admin_password
#  region_name
#
#env.keystone = {
#    'keystone_ip'     : '10.84.29.166',
#    'auth_protocol'   : 'http',                  #Default is http
#    'auth_port'       : '35357',                 #Default is 35357
#    'admin_token'     : 'zc8SF2xht4HckHSCKWJqn4zjchxYMc2knWPGMkL9VMjGbWSHp8FRNc5Gt6rVRfKp',  #admin_token in keystone.conf
#    'admin_user'      : 'admin',                 #Default is admin
#    'admin_password'  : 'contrail123',           #Default is contrail123
#    'nova_password'   : 'contrail123',           #Default is the password set in admin_password
#    'neutron_password': 'contrail123',           #Default is the password set in admin_password
#    'service_tenant'  : 'services',               #Default is service
    #'admin_tenant'    : 'admin',                 #Default is admin
    #'region_name'     : 'RegionOne',             #Default is RegionOne
    #'insecure'        : 'True',                  #Default = False
#    'manage_neutron'  : 'no',                    #Default = 'yes' , Does configure neutron user/role in keystone required.
#}


#env.nova = {
#    'cpu_mode': 'host-passthrough', # Possible options: none, host-passthrough, host-model, and custom
#                                    # if cpu_mode is 'custom' specify cpu_model option too
#    'cpu_model': 'Nehalem',         # relevant only if cpu_mode is 'custom'
#}

# In High Availability setups.
env.ha = {
    'contrail_internal_vip'   : '10.1.1.241',               #Internal Virtual IP of the HA setup.
    'contrail_external_vip'   : '10.1.1.241',               #External Virtual IP of the HA setup.
#    'nfs_server'      : '3.3.3.3',               #IP address of the NFS Server which will be mounted to /var/lib/glance/images of openstack Node, Defaults to env.roledefs['compute'][0]
#    'nfs_glance_path' : '/var/tmp/images/',      #NFS Server path to save images, Defaults to /var/tmp/glance-images/
}

# In environments where openstack services are deployed independently
# from contrail, you can use the below options
# service_token : Common service token for for all services like nova,
#                 neutron, glance, cinder etc
# amqp_host     : IP of AMQP Server to be used in openstack
# manage_amqp   : Default = 'no', if set to 'yes' provision's amqp in openstack nodes and
#                 openstack services uses the amqp in openstack nodes instead of config nodes.
#                 amqp_host is neglected if manage_amqp is set
#
#env.openstack = {
#    'service_token' : 'zc8SF2xht4HckHSCKWJqn4zjchxYMc2knWPGMkL9VMjGbWSHp8FRNc5Gt6rVRfKp', #Common service token for for all openstack services
#    'amqp_host' : '10.84.29.165',            #IP of AMQP Server to be used in openstack
    #'manage_amqp' : 'no',                    #Default no, Manage seperate AMQP for openstack services in openstack nodes.
    #'osapi_compute_workers' : 40,             #Default 40, For low memory system reduce the osapi compute workers thread.
    #'conductor_workers' : 40,                 #Default 40, For low memory system reduce the conductor workers thread.
#}

#neutron_metadata_proxy_shared_secret = True

# Neutron specific configuration
#env.neutron = {
#   'protocol': 'http', # Default is http
#}

#To enable multi-tenancy feature
multi_tenancy = True

#To enable haproxy feature
haproxy = False

#To Enable prallel execution of task in multiple nodes
do_parallel = False

# To configure the encapsulation priority. Default: MPLSoGRE
#env.encap_priority =  "'MPLSoUDP','MPLSoGRE','VXLAN'"

# Optional proxy settings.
# env.http_proxy = os.environ.get('http_proxy')

#To enable LBaaS feature
# Default Value: False
#env.enable_lbaas = True

# Ceilometer enable/disable installation and provisioning
# Default Value: False
#enable_ceilometer = True

#OPTIONAL REMOTE SYSLOG CONFIGURATION
#===================================
#For R1.10 this needs to be specified to enable rsyslog.
#For Later releases this would be enabled as part of provisioning,
#with following default values.
#
#port = 19876
#protocol = tcp
#collector = dynamic i.e. rsyslog clients will connect to servers in a round
#                         robin fasion. For static collector all clients will
#                         connect to a single collector. static - is a test
#                         only option.
#status = enable
#
#env.rsyslog_params = {'port':19876, 'proto':'tcp', 'collector':'dynamic', 'status':'enable'}

#OPTIONAL Virtual gateway CONFIGURATION
#=======================================

#Section vgw is only relevant when you want to use virtual gateway feature.
#You can use one of your compute node as  gateway .

#Definition for the Key used
#-------------------------------------
#vn: Virtual Network fully qualified name. This particular VN will be used by VGW.
#ipam-subnets: Subnets used by vn. It can be single or multiple
#gateway-routes: If any route is present then only those routes will be published
#by VGW or Default route (0.0.0.0) will be published

#env.vgw = {host1: {'vgw1':{'vn':'default-domain:admin:public:public', 'ipam-subnets': ['10.204.220.128/29', '10.204.220.136/29', 'gateway-routes': ['8.8.8.0/24', '1.1.1.0/24']}]},
#                   'vgw2':{'vn':'default-domain:admin:public1:public1', 'ipam-subnets': ['10.204.220.144/29']}
#          }

#OPTIONAL optional tor agent and tsn CONFIGURATION
#==================================================
#Section tor agent is only relevant when you want to use Tor Agent feature.
#You can use one of your compute node as  Tor Agent . Same or diffrent compute
#node should be enable as tsn

#Definition for the Key used
#-------------------------------------
# tor_ip: IP of the tor switch
# tor_agent_id: Unique Id of the tor switch to identify. Typicaly a numeric value.
# tor_agent_name: Unique name for TOR Agent. This is optional field. If this is
#                 not specified name used will be <hostname>-<tor_agent_id>
# tor_ovs_port: Port number to be used by ovs
# tor_ovs_protocol: Connection protocol to be used by ovs. Currently only TCP
# tor_tsn_ip: TSN node ip
# tor_agent_ovs_ka: Tor Agent OVSDB keepalive timer in milli seconds
#env.tor_agent =
#{host3:[{'tor_ip':'10.204.217.39','tor_agent_id':'1','tor_agent_name':'nodexx-1', 'tor_ovs_port':'9999','tor_ovs_protocol':'tcp','tor_tsn_ip':'10.204.221.35', 'tor_agent_ovs_ka':'10000'}]}

# OPTIONAL DPDK CONFIGURATION
# ===========================
# If some compute nodes should use DPDK vRouter version it has to be put in
# env.dpdk dictionary. The format is:
# env.dpdk = {
#     host1: { 'huge_pages' : '50', 'coremask' : '0xf' },
#     host2: { 'huge_pages' : '50', 'coremask' : '0,3-7' },
# }
# huge_pages - Specify what percentage of host memory should be reserved
#              for access with huge pages
# coremask   - Specify CPU affinity mask to run vRouter with. Supported formats:
#              hexadecimal, comma-sepparated list of CPUs, dash-separated range
#              of CPUs.
# OPTIONAL vrouter limit parameter
# ==================================
#env.vrouter_module_params = {
#     host2:{'mpls_labels':'131072', 'nexthops':'131072', 'vrfs':'65536', 'macs':'262144'},
#}
#
# OPTIONAL md5 key enabling
# There are 2 ways of enabling BGP md5 key on node apart from the webui.
# 1. Before provisioning the node, include an env dict in testbed.py as shown below specifying the desired key value #    on the node. The key should be of type "string" only.
# 2. If md5 is not included in testbed.py and the node is already provisioned, you can run the
#    contrail-controller/src/config/utils/provision_control.py script with a newly added argument for md5.
# The below env dict is for first method specified, where you include a dict in testbed.py as shown below:
#  env.md5 = {
#     host1: 'juniper',
#  }
# 'juniper' is the md5 key that will be configured on the node.
