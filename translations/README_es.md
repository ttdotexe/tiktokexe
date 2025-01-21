# TTDOTEXE (TikTok.exe)

TTDOTEXE (TikTok.exe) es un proyecto innovador que combina el encanto de los memes de TikTok con tecnología de punta. Desarrollado con Python y Microsoft Azure Quantum Framework, este proyecto ofrece un enfoque divertido pero técnico al blockchain y al arte ASCII.

## Características

- **Animación en Arte ASCII**: Convierte GIFs en impresionantes animaciones ASCII para visualización en terminal.
- **Integración con Computación Cuántica**: Aprovecha Microsoft Azure Quantum Framework para mejorar la eficiencia criptográfica y computacional.
- **Blockchain de Solana**: Potenciado por la arquitectura rápida y de bajo costo de Solana, lo que hace que las interacciones blockchain sean fluidas.
- **Token SPL Basado en Python**: El primer token de Solana de su tipo codificado completamente en Python.
- **Enfoque Comunitario**: Totalmente de código abierto para inspirar colaboración y creatividad.

## Perspectivas Visuales

### Entendiendo la Conversión de Color y ASCII

#### Conversión de Colores en Arte ASCII
TTDOTEXE mapea los colores de los fotogramas de GIF a caracteres ASCII con precisión.

![Tabla de Colores de 8 bits](./images_rdm/8-bit_color_table.png)
*Ejemplo de mapeo de colores de 8 bits para arte ASCII.*

#### Análisis de Brillo y Píxeles
El brillo y la saturación de los píxeles son clave para seleccionar caracteres ASCII para las animaciones.

![Análisis de Brillo y Saturación](./images_rdm/imgBrightnes.png)
*Niveles de brillo y saturación que afectan el mapeo ASCII.*

#### Procesamiento Fotograma por Fotograma
Se logran animaciones fluidas a través de un cuidadoso análisis fotograma por fotograma.

![Procesamiento de Fotogramas](./images_rdm/imgVideoFrames.png)
*Análisis fotograma por fotograma para animaciones continuas.*

---

## Requisitos Previos

Antes de ejecutar el proyecto, asegúrate de tener instalados los siguientes elementos:

- **Docker**
- **Python 3.8+**
- **pip**

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/ttdotexe/tiktokexe.git
cd tiktokexe
```

2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

3. (Opcional) Configura un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

## Ejecución del Proyecto Localmente

1. Ejecuta la animación en arte ASCII:

```bash
python TIKTOKEXE.py
```

2. Obtén los holders del token utilizando el script fetch_wallet:

```bash
python fetch_wallet.py
```

## Ejecución con Docker

1. Construye la imagen de Docker:

```bash
docker build -t tiktokexe .
```

2. Ejecuta el contenedor:

```bash
docker run --rm -it tiktokexe
```

## Estructura del Proyecto

```plaintext
.
├── assets                # GIFs y otros recursos
├── images_rdm            # Imágenes de referencia
├── src                   # Código fuente
│   ├── ascii_generator.py
│   ├── ascii_player.py
│   ├── utils.py
├── translations          # Archivos de traducción
├── TIKTOKEXE.py          # Punto de entrada principal
├── fetch_wallet.py       # Script para obtener holders del token
├── requirements.txt      # Dependencias de Python
├── Dockerfile            # Configuración de Docker
└── README.md             # Documentación del proyecto
```

## ¿Por qué Microsoft Azure Quantum?

Azure Quantum proporciona algoritmos inspirados en la computación cuántica de última generación que mejoran las funciones criptográficas, optimizan los procesos computacionales y permiten intercambios de claves seguros. Esta integración garantiza que TTDOTEXE sea eficiente, escalable y seguro.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## Contribuciones

¡Las contribuciones son bienvenidas! No dudes en abrir issues o enviar pull requests.

## Contacto

Sigue el progreso de TTDOTEXE en [GitHub](https://github.com/ttdotexe/tiktokexe). ¡Comparte tus comentarios y hagamos este proyecto aún mejor!
