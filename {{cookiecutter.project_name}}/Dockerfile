FROM debian:stable-slim AS build

RUN apt-get update && apt-get install -y \
    curl ca-certificates mime-support python3-dev build-essential zlib1g-dev libssl-dev \
    libffi-dev libsqlite3-dev sqlite3

RUN apt-get install make --reinstall

# Build Python
WORKDIR /opt/cpython3/
RUN curl -O "https://www.python.org/ftp/python/3.8.2/Python-3.8.2.tar.xz"
RUN tar -xf "Python-3.8.2.tar.xz"
WORKDIR Python-3.8.2
RUN ./configure --enable-optimizations
RUN make -j "$(nproc)"



FROM nginx:stable

RUN apt-get update && apt-get install -y \
    curl ca-certificates mime-support make gcc libsqlite3-dev

# Install Python
COPY --from=build /opt/cpython3 /opt/cpython3
WORKDIR /opt/cpython3/Python-3.8.2/
RUN make install
RUN python3.8 -m pip install poetry uwsgi

# Copy apps and related dependencies
WORKDIR /application/
COPY ["pyproject.toml", "poetry.lock", "manage.py", "./"]
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-dev

WORKDIR /application/{{cookiecutter.project_name}}/
COPY ["{{cookiecutter.project_name}}", "./"]

# Set envvars
ENV DJANGO_SETTINGS_MODULE {{cookiecutter.project_name}}.settings.development
ENV NGINX_HOST localhost
ENV NGINX_PORT 8080

# Migrate and prepare static
WORKDIR /application/
RUN python3.8 manage.py migrate && python3.8 manage.py collectstatic

# Entrypoint compiles Nginx config & starts uWSGI
COPY server/nginx-default.conf.template /etc/nginx/conf.d/default.conf.template
COPY server/uwsgi.ini /
COPY docker/docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["nginx", "-g", "daemon off;"]
EXPOSE ${NGINX_PORT}
