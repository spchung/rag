# api/Dockerfile
FROM denoland/deno:alpine-1.44.4

WORKDIR /app

# Copy your Deno project files into the container
# Copy only necessary files to optimize Docker caching
COPY . .

# Cache and download dependencies for efficient builds
# RUN deno cache deps.ts

# Set Deno permissions and specify the entry point
CMD ["run", "--allow-net", "--allow-read", "main.ts"]

# Expose the port the app runs on
EXPOSE 8080