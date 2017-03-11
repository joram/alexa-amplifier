# alexa-amplifier
alexa controls for denon amplifier
## ideas for more functionality
- word assosiation (TFIDF of the wikipedia page)
- fact-core facts (because fact core has the best facts)

## Setup (with Nginx on Ubuntu 6.04)
```
mkdir /var/www/amp
sudo letsencrypt certonly --webroot -w /var/www/amp -d amp.serenity.oram.ca
```
this creates certificates and keys here: `/etc/letsencrypt/live/amp.serenity.oram.ca/*.pem`

and the nginx config can look like this:
```
server {
  server_namei amp.serenity.oram.ca;
  listen 443 ssl;
  ssl_certificate /etc/letsencrypt/live/amp.serenity.oram.ca/fullchain.pem;
  ssl_certificate_key /etc/letsencrypt/live/amp.serenity.oram.ca/privkey.pem;

  ...

}```
