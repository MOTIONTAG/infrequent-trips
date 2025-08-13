# MOTIONTAG Infrequent Trip Identification

This repository contains the open-source Python implementation of the logic used to identify and group infrequent trips from mobility data. This project was initiated by MOTIONTAG to provide a transparent, reusable, and community-driven tool for researchers, planners, and developers working with trip and travel behavior datasets. While the original backend logic at MOTIONTAG is implemented in Ruby, this version has been created in Python to ensure wider accessibility and ease of use for the broader community. For more information about MOTIONTAG technology and products, visit [motiontag.com](https://motiontag.com).

## About The Project

The core purpose of this module is to process a standardized trip dataset and apply a specific set of rules to classify and group individual trip stages into "infrequent trips." This is particularly useful for transportation research and mobility studies where understanding non-routine travel behavior is critical. This module intentionally focuses only on the logic for identifying infrequent trips. The underlying processes of trip detection, stage segmentation, and mode of transport identification are part of MOTIONTAG's proprietary standard software and are not included in this repository.

## Getting Started

### Prerequisites

- [uv](https://docs.astral.sh/uv/getting-started/installation/) - A fast Python package installer and resolver

### Setup

1. Clone the repository:
   ```bash
   git clone git@github.com:MOTIONTAG/infrequent-trips.git
   cd infrequent-trips
   ```

2. Install dependencies using uv (this will automatically create a virtual environment):
   ```bash
   uv sync
   ```

### Running Tests

```bash
uv run python -m unittest discover -s tests
```

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated. If you have a suggestion that would make this better, please fork the repo and create a pull request.

## License

See `LICENSE` for more information.
