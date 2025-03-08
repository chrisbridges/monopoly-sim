# logging/Dockerfile
FROM fluent/fluentd:v1.16-1

# Copy custom Fluentd config
COPY fluent.conf /fluentd/etc/

# By default, Fluentd listens on port 24224
EXPOSE 24224

CMD ["fluentd", "-c", "/fluentd/etc/fluent.conf"]