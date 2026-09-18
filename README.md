# GitHub Banner Generator

A lightweight Python tool for generating minimalist GitHub profile banners with custom text, fonts, and layered glow effects.

Built with Pillow, the project is designed to make it easy to generate clean, reusable banners directly from code.

## Features

- Custom banner dimensions
- Custom text
- Custom fonts
- Centered text rendering
- Layered glow effects
- PNG export

## Example

Generated banner:

![Example banner](output/example.png)

## Tech

- Python
- Pillow

## Usage

```bash
py -m src.banner_generator.generator
````

## Project Structure

```text
banner-generator/
├── assets/
│   └── fonts/
├── output/
├── src/
│   └── banner_generator/
│       ├── __init__.py
│       ├── config.py
│       └── generator.py
└── README.md
```

## Development

This project was implemented manually as a learning project. No AI was used to write the code.

## Roadmap

* Command-line interface
* Configurable colors
* Multiple glow presets
* Background effects
* Export presets for GitHub profiles

## License

This project uses the Press Start 2P font, licensed under the SIL Open Font License 1.1.