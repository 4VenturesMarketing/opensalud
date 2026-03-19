FROM nginx:stable-alpine

# Limpia el directorio por defecto de Nginx
RUN rm -rf /usr/share/nginx/html/*

# Copia todo el contenido del repo (index.html, manuel_villalon.jpeg, etc.)
COPY . /usr/share/nginx/html/

# Asegura permisos de lectura para el servidor
RUN chmod -R 755 /usr/share/nginx/html/

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
