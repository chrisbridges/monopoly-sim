FROM fluent/fluentd:v1.16-1

# Switch to root to install packages
USER root

# # Install netcat (Debian-based)
# RUN apt-get update && apt-get install -y netcat

# If Alpine-based, you'd do:
# RUN apk add --no-cache netcat-openbsd

# Switch back to fluent user if needed
USER fluent

COPY fluent.conf /fluentd/etc/
EXPOSE 24224
CMD ["fluentd", "-c", "/fluentd/etc/fluent.conf"]