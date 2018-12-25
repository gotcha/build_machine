FROM gotcha/buildout_docker_alpine AS build
RUN apk add --no-cache --virtual .build-deps \
    gcc \
    libc-dev \
    zlib-dev \
    libjpeg-turbo-dev \
    libpng-dev \
    libxml2-dev \
    libxslt-dev \
    pcre-dev
COPY ./buildout.cfg /usr/src/app/buildout.cfg
RUN buildout -c /usr/src/app/buildout.cfg

FROM gotcha/buildout_docker_alpine
RUN apk add --no-cache --virtual .build-deps \
    libjpeg \
    libxslt \
    gettext \
&& addgroup -g 500 plone \
&& adduser -S -D -G plone -u 500 plone \
&& chown -R plone:plone /usr/src/app
COPY --from=build --chown=plone:plone /usr/src/app /usr/src/app
USER plone
CMD /usr/src/app/bin/instance
