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

#### Building Manually

```bash
git clone https://github.com/Quad4-Tactical/OSINT-Tools.git && cd OSINT-Tools
docker build -t osint-tools .
docker run -d --name osint-tools \
  -p 8000:8000 \
  -v /videos:/videos \
  osint-tools
```