from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config
from nornir_netmiko.tasks import netmiko_save_config
from nornir_utils.plugins.functions import print_result

# Initialiseer Nornir met configuratiebestand
nr = InitNornir(config_file="./configs/config.yaml")

# Taak om configuratiebestanden naar apparaten te sturen
def netmiko_send_config_from_file(task):
    config_file = f"./snapshots/configs/{task.host.name}.txt"
    task.run(task=netmiko_send_config, config_file=config_file)

# Taak om de configuratie op te slaan
def netmiko_save_config_example(task):
    task.run(task=netmiko_save_config)

# Voer de taken parallel uit voor alle hosts in de Nornir inventory
results = nr.run(task=netmiko_send_config_from_file)
print_result(results)

# Voer de save-config taak parallel uit
results = nr.run(task=netmiko_save_config_example)
print_result(results)