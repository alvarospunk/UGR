#!/bin/bash

#Proporcionar acceso mediante password
sudo sed -i 's/^#PasswordAuthentication yes/PasswordAuthentication yes/g' /etc/ssh/sshd_config;

#Reiniciar servicio ssh
sudo service ssh restart;

echo "Acceso habilitado por 30 segundos";

#Esperar unos segundos para que los usuarios puedan acceder al servidor
sleep 30;

#Dejar todo como estaba
sudo sed -i 's/PasswordAuthentication yes/#PasswordAuthentication yes/g' /etc/ssh/sshd_config

echo "Acceso cerrado";

#Reiniciar servicio ssh
sudo service ssh restart;


