FROM nginx:latest

ENV LISTEN=8000

ENV OPT_SERVER_PORT=http://opt:8000
ENV IHUB_SERVER_PORT=http://ihub:8000
ENV WEB_SERVER_PORT=http://web:8000

COPY ./nginx/templates/default.conf.template /etc/nginx/templates/