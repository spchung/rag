FROM denoland/deno:alpine-1.44.4

WORKDIR /app

COPY . .
RUN deno cache main.ts
RUN deno task build

USER deno
EXPOSE 8000

CMD ["run", "-A", "main.ts"]
