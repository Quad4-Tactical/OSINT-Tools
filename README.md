# OSINT-Tools

A collection of useful tools that can be used with the built-in frontend or using just the API.

![OSINT Tools Preview](/preview/OSINT-Tools-Preview01.png)

## Installation

### Docker

```bash
docker run -it --rm -v $(pwd):/data -w /data python:3.7 bash
```

### Building the Docker image manually

```bash
docker build -t osint-tools .
```

### Running the Docker image

```bash
docker run -it --rm -v $(pwd):/data -w /data osint-tools bash
```

