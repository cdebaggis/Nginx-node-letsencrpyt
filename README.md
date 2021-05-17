Minimal Node.js application for intro to Docker tutorial: https://www.digitalocean.com/community/tutorials/how-to-build-a-node-js-application-with-docker

Follow the steps from the Docker tutorial. The completed files are here on the Guthub. 

The rough steps I follow including the Docker tutorial look like this:

1. Route 53 domain name purchase
2. Elastic IP
3. Create A records in dnz zone with elastic ip
4. provision ubuntu 18 server
	- open ssh, http, https, DNS (UPD,TCP)
5. Associate Elastic IP with Ubuntu Server
6. Install Docker and Docker-compose on Ubuntu
7. MUST manually change url references
  -nginx.conf
	-docker-compose.yml
8. run sudo docker-compose up -d
9. Test

When the steps are completed uncomment the lines in the nginx.conf file in order to add the login page and the securelink.
