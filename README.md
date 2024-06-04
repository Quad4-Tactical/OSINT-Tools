# OSINT-Tools

A collection of useful tools that can be used with the built-in frontend or can be adapted for your own workflows using the API.

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

## TODO

### Existing Tools
- [ ] RSS Fetcher: Improve styling in result-container
- [ ] Argos Translate: Automatic Language Detection

### New Tools 
- [ ] Username Search (theHarvester)
- [ ] MAC Address Lookup
- [ ] IP Address Lookup
- [ ] Domain Lookup / Scanning
- [ ] Email Lookup / Email to Registered Accounts (Holehe)
- [ ] Phone Number Lookup
- [ ] GitHub Search / Profile Fetch
- [ ] Public People Search Sites Lookup
- [ ] Metadata Extraction
- [ ] Steam User Searching / Matching Schemas
- [ ] Audio Transcribe
- [ ] Conversion (Docs, Videos and Audio)

### Security Features
- [ ] Basic Auth *Optional*

### Core Features
- [ ] SQLite, PostgreSQL, SurrealDB Support
- [ ] Docker Compose
- [ ] Multi-Threading for certain tools
- [ ] Defined Pipelines (e.g. Fetch RSS (every x mins/hrs/days) -> Translate to en -> Save To Database)
- [ ] Release Python Package
- [ ] UI Improvements (Layout)
- [ ] API Documentation
- [ ] Add FFmpeg to Docker Images
- [ ] Export Buttons
- [ ] Use FastAPI routers

### Integrations
- [ ] Shodan API
- [ ] GrayNoise API
- [ ] Have I Been Pwned API
- [ ] Dehashed API
- [ ] SearXNG Search API
 

## Contributing

Feels free to contribute your ideas, tools or anything to help the project.