# Ajedrez en python

Este proyecto es una implementación del juego de ajedrez en Python. El objetivo es ofrecer una simulación completa del juego de ajedrez, incluyendo el tablero, las piezas y las reglas básicas. El proyecto está diseñado para ser una base sólida para aprender sobre la programación de juegos y la lógica detrás de un juego de ajedrez.

## Author
- Valentin I. Becerra
- [@vbcrr4](https://www.github.com/vbcrr4)
- Legajo: 62180

## Instalación
Para instalar el juego de ajedrez, sigue los siguientes pasos:

1. Clona el repositorio:
   ```bash
   git clone https://github.com/um-computacion-tm/ajedrez-2024-vbcrr4.git
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd ajedrez-2024-vbcrr4 
   ```
3. Instala las dependencias requeridas:
   ```bash
   pip install -r requirements.txt
   ```

## Uso
Para ejecutar el juego de ajedrez, sigue los siguientes pasos:

1. Construir la imagen Docker:
    ```bash
    sudo docker buildx build -t ajedrez-valen . --no-cache
    ```
2. Ejecutar el juego de ajedrez:
    ```bash
    sudo docker run -it ajedrez-valen
    ```

## Status Badges

### MAIN
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/ajedrez-2024-vbcrr4/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/ajedrez-2024-vbcrr4/tree/main)

### DEVELOP
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/ajedrez-2024-vbcrr4/tree/develop.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/ajedrez-2024-vbcrr4/tree/develop)

### Maintainability Badge
[![Maintainability](https://api.codeclimate.com/v1/badges/feae1058b7acb7817753/maintainability)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-vbcrr4/maintainability)

### Test Coverage Badge
[![Test Coverage](https://api.codeclimate.com/v1/badges/feae1058b7acb7817753/test_coverage)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-vbcrr4/test_coverage)