# OSINT-Tools

A collection of useful tools that can be used with the built-in frontend or using just the API.

![OSINT Tools Preview](/preview/OSINT-Tools-Preview01.png)

## Installation

### Docker

```bash
docker run -d --name osint-tools \
  -p 8000:8000 \
  -v /videos:/videos \
  ghcr.io/quad4-tactical/osint-tools:latest
```

### Podman

```bash
podman run -p 8000:8000 -v /videos:/videos ghcr.io/quad4-tactical/osint-tools:latest
```

## Building Manually

### Docker

```bash
git clone https://github.com/Quad4-Tactical/OSINT-Tools.git && cd OSINT-Tools
docker build -t osint-tools .
docker run -d --name osint-tools \
  -p 8000:8000 \
  -v /videos:/videos \
  osint-tools
```

### Podman

```bash
git clone https://github.com/Quad4-Tactical/OSINT-Tools.git && cd OSINT-Tools
podman build -t osint-tools .
podman run -p 8000:8000 -v /videos:/videos osint-tools
```