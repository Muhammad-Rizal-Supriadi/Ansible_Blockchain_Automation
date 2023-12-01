# Ansible KPU Blockchain


Point penting untuk Running Ansible

    - Orderer
    - Peer
    - Chaincode
    - Vault

Struktur Folder 

    - arcive = digunakan untuk menyimpan password vault
    - group_vars = untuk menyimpan variabel untuk menyimpan file yang berisi variabel, dan password couchdb
    - inventory = untuk melakukan konfigurasi host
    - playbooks =
    - roles 
        - chaincode
        - orderer
        - peer
        - remove-project
    - ansibe.cfg = untuk melakukan konfigurasi inventory
    - chaincode.yml = untuk menjalankan fungsi chaincode 
        - installChaincode
        - deployChaincode
    - orderer.yml = untuk menjalankan orderer yang menjalankan perintah" dibawah ini
        - start-ca
        - generate-certificate
        - stop-docker-ca-kpu
        - remove-docker-ca-kpu
        - generate-artifacts-channel
        - start-orderer
        - pause
        - create-channel
        - generate-anchor-channel
        - remove-anchor
        - git-push
    - peer.yml = untuk menjalankan peer yang menjalankan perintah" dibawah ini
        - start-peer
        - start-ca-peer
        - paus
        - join-channel
    - prerequisite.yml = untuk menginstall keperluan yang dibutuhkan dalam pengembangan blockchain
        - curl
        - docker
        - git
        - golang
        - jq
        - nodejs
        - python
    - remove-project.yml = untuk menghapus project dan system jaringan blockchain.

Chaincode

    - Untuk menjalankan chaincode dengan mengetikan "ansible-playbook chaincode.yml"


Orderer

    - Untuk menjalankan orderer dengan mengetikan "ansible-playbook orderer.yml"

Peer

    - Untuk menjalankan Peer dengan mengetikan "ansible-playbook --ask-vault-pass peer.yml" lalu masukan password vault
    
Prerequisite

    - Untuk menjalankan prerequisite dengan mengetikan "ansible-playbook prerequisite.yml"
    - ganti hosts sesuai yang ingin diinstall dalam group pada file hosts

Remove-Project

    - Untuk menjalankan remove-project dengan mengetikan "ansible-playbook remove-project.yml" 
    - ganti hosts sesuai yang ingin di remove berdasarkan group pada file hosts         
   

Steps:
 
Running it:
--- Ansible Hyperledger Fabric Netowrk Pemilu ---

    1) Run Prerequisite
    2) Run Orderer
        1) start-ca
        2) generate-certificate
        3) stop-docker-ca-kpu
        4) remove-docker-ca-kpu
        5) generate-artifacts-channel
        6) start-orderer
        7) pause
        8) create-channel
        9) generate-anchor-channel
        10) remove-anchor
        11) git-push 
    3) Run Peer
        1) start-peer
        2) start-ca-peer
        3) paus
        4) join-channel
    4) Run Chaincode
        1) Install Chaincode
        2) Deploy Chaincode
    5) api-2.0
        1) Lakukan generate file generate-ccp.sh
        2) Rapikam hasil connection.json
        3) Pastikan chaincode sudah dideploy dan running pada docker ps -a
        4) Mulai lakukan transaksi
 

 Catatan:
 
Progress Ansible:

    - Sudah sampai mereplace generate-cpp.sh pada folder api-2.0
    - Untuk membuka hash vault gunakan perintah "ansible-vault decrypt hosts"
    - Untuk melakukan hash vault gunakan perintah "ansible-vault encrypt hosts"
    - Branch yang baru di "peers2"


