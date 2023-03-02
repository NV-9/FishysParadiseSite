import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fishysparadisesite.settings')

application = get_wsgi_application()

"""
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    server_name fishysparadise.fun;
    if ($http_x_forwarded_proto = "http") {
        return 307 https://$host$request_uri;
    }
    location = /favicon.ico { access_log off; log_not_found off; }
    location /static {
        autoindex on;
        alias /var/www/fishysparadise.fun/static/;
        include /etc/nginx/mime.types;
    }
    location / {
        include proxy_params;
        proxy_pass http://localhost:8000;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Scheme $scheme;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    listen [::]:443 ssl ipv6only=on; # managed by Certbot
    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/fishysparadise.fun/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/fishysparadise.fun/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

}

"""
