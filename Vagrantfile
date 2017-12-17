# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure('2') do |config|

  config.vm.box = 'azure'
  config.vm.box_url = 'https://github.com/msopentech/vagrant-azure/raw/master/dummy.box' #Caja base vacía
  config.vm.network "private_network",ip: "192.168.11.4", virtualbox__intnet: "vboxnet0" #Ip privada
  config.vm.hostname = "localhost"
  config.vm.network "forwarded_port", guest: 80, host: 80

  # use local ssh key to connect to remote vagrant box
  config.vm.provider :azure do |azure, override|
    config.ssh.private_key_path = '~/.ssh/id_rsa'
    azure.vm_image_urn = 'canonical:UbuntuServer:16.04-LTS:16.04.201701130' #Imagen base del sistema
    azure.vm_size = 'Basic_A0' #Tamaño (recursos) de la MV
    azure.location = 'southcentralus'
    azure.tcp_endpoints = '80:80'
    azure.vm_name = "maquinaSubjectsGII"
    azure.resource_group_name= "subjectsgiibot"
    azure.tenant_id = "68c2006f-1c69-4334-a449-fbef01ac9b79"
    azure.client_id = "c1cc5441-f52e-481c-ab17-415f88c0afdd"
    azure.client_secret = "Mty17mZFgyVyvQZVyduHXF4RtpHtrbm1V9xGWsjmjq8="
    azure.subscription_id = "f5ad611a-c006-4caf-8ef7-137903b02e5e"
  end

  # Provisionar con ansible
  config.vm.provision "ansible" do |ansible|
    ansible.sudo = true
    ansible.playbook = "./provision/playbook.yml"
    ansible.verbose = "-vvvv"

    ansible.host_key_checking = false
  end

end
