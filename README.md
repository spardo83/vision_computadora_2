# Sistema de Monitoreo Automático de EPP en Obras de Construcción

**Trabajo Práctico – Visión por Computadora II**
**Autores:** Pardo, Sebastián. Ferrari, Maira Daniela

---

## Descripción

Sistema basado en deep learning para detectar automáticamente el uso de Equipamiento de Protección Personal (EPP) en obras de construcción, con seguimiento persistente de trabajadores mediante ByteTrack.

El sistema detecta en tiempo real la presencia/ausencia de:
- 🪖 Casco de seguridad (Hardhat)
- 🦺 Chaleco reflectivo (Safety Vest)
- 😷 Mascarilla (Mask)

## Arquitectura

```
Video de entrada → YOLOv8/v11 (detección) → ByteTrack (tracking) → Compliance Engine → Alertas
```

## Stack Técnico

| Componente | Tecnología |
|---|---|
| Lenguaje | Python 3.10+ |
| Gestor de paquetes | [uv](https://docs.astral.sh/uv/) |
| Detección | Ultralytics YOLO (v8n, v8m, v11n) |
| Tracking | ByteTrack (vía Ultralytics) |
| Dataset | [Construction-PPE – Roboflow Universe](https://universe.roboflow.com/roboflow-universe-projects/construction-site-safety) |
| Entorno | Jupyter Notebook + VS Code |

## Dataset

Dataset: **Construction Site Safety** (Roboflow Universe)
Clases: `Hardhat`, `Mask`, `NO-Hardhat`, `NO-Mask`, `NO-Safety Vest`, `Person`, `Safety Cone`, `Safety Vest`, `machinery`, `vehicle`

Referencia académica:
> Roboflow Universe Projects. Construction Site Safety Dataset. Roboflow, 2024.
> Dataset asociado a: [Automation in Construction, 2024](https://www.sciencedirect.com/science/article/pii/S0926580524001882)

## Estructura del Proyecto

```
computer_vision_2_tp/
├── notebooks/
│   ├── 01_setup_and_dataset.ipynb     # Setup + EDA del dataset
│   ├── 02_model_training.ipynb        # Fine-tuning YOLOv8n / v8m / v11n
│   ├── 03_model_comparison.ipynb      # Comparación de arquitecturas
│   └── 04_tracking_demo.ipynb         # Demo con ByteTrack + alertas
├── src/ppe_monitor/                   # Módulo Python del proyecto
├── data/                              # Dataset (no incluido en git)
├── models/                            # Pesos entrenados (no incluidos en git)
├── runs/                              # Outputs de entrenamiento YOLO
├── videos/                            # Videos de entrada/salida
├── pyproject.toml                     # Dependencias (uv)
└── .gitignore
```

## Instalación y Uso

### Prerrequisitos
- Python 3.10+
- [uv](https://docs.astral.sh/uv/) instalado

### Setup del entorno

```bash
# Clonar repositorio
git clone https://github.com/spardo83/computer_vision_2_tp.git
cd computer_vision_2_tp

# Crear entorno virtual e instalar dependencias con uv
uv venv
uv pip install -e .

# Instalar PyTorch (CPU)
uv pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu

# Para GPU (CUDA 12.1)
# uv pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121

# Activar entorno
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows

# Registrar kernel de Jupyter
python -m ipykernel install --user --name=ppe-monitor --display-name "PPE Monitor"
```

### Ejecutar Notebooks (en orden)

Abrir VS Code en la carpeta del proyecto y ejecutar:

1. `notebooks/01_setup_and_dataset.ipynb` – Configurar API key de Roboflow y descargar dataset
2. `notebooks/02_model_training.ipynb` – Entrenar los tres modelos
3. `notebooks/03_model_comparison.ipynb` – Comparar y seleccionar el mejor modelo
4. `notebooks/04_tracking_demo.ipynb` – Demo con video de obra

### API Key de Roboflow

Registrarse en [roboflow.com](https://roboflow.com) (gratuito) y obtener la API key en Account → API Keys.
En el Notebook 1, reemplazar `"TU_API_KEY_AQUI"` con la key obtenida.

## Resultados

### Comparación de Modelos

| Modelo | mAP50 | mAP50-95 | Precision | Recall | Latencia (CPU) |
|--------|-------|----------|-----------|--------|----------------|
| YOLOv8n | 0.777 | 0.476 | 0.896 | 0.685 | 8.3ms (120 FPS) |
| YOLOv8m | **0.858** | **0.580** | **0.936** | **0.787** | 10.3ms (97 FPS) |
| YOLOv11n | 0.769 | 0.461 | 0.888 | 0.698 | 10.3ms (97 FPS) |

## Notebooks

### Notebook 1 – Setup & Dataset
Análisis exploratorio del dataset Construction-PPE: distribución de clases, estadísticas de bounding boxes, visualización de muestras con anotaciones.

### Notebook 2 – Fine-tuning de Modelos
Entrenamiento con transfer learning desde pesos COCO. Configuración adaptada para CPU (imgsz=416, batch=4, epochs=15).

### Notebook 3 – Comparación de Arquitecturas
Comparación cuantitativa de YOLOv8n vs YOLOv8m vs YOLOv11n con métricas mAP, Precision, Recall, latencia de inferencia y curvas de entrenamiento.

### Notebook 4 – Tracking + Demo
Integración de ByteTrack para tracking persistente. Motor de compliance con ventana deslizante. Generación de video anotado con alertas en tiempo real.

## Referencias

- Redmon, J. et al. (2016). You Only Look Once: Unified, Real-Time Object Detection.
- Zhang, Y. et al. (2022). ByteTrack: Multi-Object Tracking by Associating Every Detection Box. ECCV 2022.
- Ultralytics YOLO Documentation: https://docs.ultralytics.com
- Dataset: Automation in Construction, 2024. DOI: 10.1016/j.autcon.2024.105356

## Licencia

MIT License – Ver LICENSE para más detalles.
