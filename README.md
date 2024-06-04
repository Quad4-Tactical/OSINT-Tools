# OSINT-Tools

A collection of useful tools that can be used with the built-in frontend or using just the API.

![OSINT Tools Preview](/preview/OSINT-Tools-Preview01.png)

## Installation

### Docker

#### Building Manually

```bash
git clone https://github.com/Quad4-Tactical/OSINT-Tools.git && cd OSINT-Tools
```

```bash
docker build -t osint-tools .
```

```bash
docker run -d -p 8000:8000 --name osint-tools osint-tools
```