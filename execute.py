from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_configure

config = """
ntp server 1.2.3.4
ntp server 2.3.4.5
"""

nr = InitNornir(config_file='./configs/config.yaml')
result = nr.run(task=napalm_configure, 
                configuration=config, 
                dry_run=True)

print_result(result)