

 
port={{ listen_port }}

{{ domain_needed }}
{{ bogus_priv }}

{% for int in interfaces %}
interface={{ int }}
{% endfor %}

#dhcp-range=eth1,192.168.100.100,192.168.100.199,4h
#dhcp-range=eth2,192.168.200.100,192.168.200.199,4h
