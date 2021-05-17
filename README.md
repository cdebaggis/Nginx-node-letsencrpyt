 Node.js application with Letsencrypt Certbot and a NGINX reverse proxy: https://www.digitalocean.com/community/tutorials/how-to-secure-a-containerized-node-js-application-with-nginx-let-s-encrypt-and-docker-compose

Follow the steps from the Docker tutorial. The completed files are here on the Guthub. 

The rough steps I follow including the Docker tutorial look like this:

1. Route 53 domain name purchase
2. Elastic IP
3. Create A records in dnz zone with elastic ip
4. provision ubuntu 18 server
	- open ssh, http, https, DNS (UPD,TCP)
5. Associate Elastic IP with Ubuntu Server
6. Install Docker and Docker-compose on Ubuntu
7. Clone the git to your user directory
8. MUST manually change domain references to your domain
  -nginx.conf
  -docker-compose.yml
8. You must also run the following 2 commands in the project diroectory:
  -sudo openssl dhparam -out /home/ubuntu/node_project/dhparam/dhparam-2048.pem 2048
  -sudo python3 generate-securelink.py
10. run sudo docker-compose up -d
11. Test

When the steps are completed uncomment the lines in the nginx.conf file in order to add the login page and the securelink.
