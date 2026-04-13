# Guía de Reproducibilidad

Esta guía explica cómo reproducir completamente los resultados del proyecto desde cero.

## Prerrequisitos

- Python 3.10+
- `uv` instalado: `pip install uv`
- Cuenta gratuita en [Roboflow](https://roboflow.com) para descargar el dataset
- ~4 GB de espacio en disco (dataset + modelos)
- GPU recomendada para el entrenamiento (el pipeline funciona en CPU pero es lento)

## Paso a Paso

### 1. Configurar el entorno

```bash
git clone https://github.com/spardo83/computer_vision_2_tp.git
cd computer_vision_2_tp

uv venv
uv pip install -e .
uv pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu  # CPU
# uv pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121  # GPU CUDA 12.1

source .venv/bin/activate       # Linux/Mac
# .venv\Scripts\activate        # Windows

python -m ipykernel install --user --name=ppe-monitor --display-name "PPE Monitor"
```

### 2. Configurar la API Key de Roboflow

```bash
cp .env.example .env
# Editar .env y reemplazar TU_API_KEY_AQUI con tu clave de Roboflow
```

### 3. Ejecutar los notebooks en orden

Abrir Jupyter o VS Code y ejecutar con el kernel `PPE Monitor`:

| Notebook | Descripción | Outputs generados |
|---|---|---|
| `01_setup_and_dataset.ipynb` | Descarga el dataset y genera el EDA | `data/dataset_config.json`, gráficos EDA |
| `02_model_training.ipynb` | Fine-tuning de los 3 modelos YOLO | `models/*.pt`, `data/eval_results.json`, `data/latency_results.json` |
| `03_model_comparison.ipynb` | Comparación de arquitecturas | `data/comparison_metrics.png`, `data/speed_accuracy_tradeoff.png` |
| `04_tracking_demo.ipynb` | Demo con ByteTrack | `videos/output_*.mp4`, `data/demo_stats.json` |

### 4. Resultados esperados

Al finalizar el Notebook 02, deberían obtenerse métricas similares a:

| Modelo | mAP50 | Precision | Recall | FPS (CPU) |
|--------|-------|-----------|--------|-----------|
| YOLOv8n | ~0.777 | ~0.896 | ~0.685 | ~120 |
| YOLOv8m | ~0.858 | ~0.936 | ~0.787 | ~97 |
| YOLOv11n | ~0.769 | ~0.888 | ~0.698 | ~97 |

> Los resultados pueden variar levemente según el hardware y la versión de `ultralytics`.

## Alternativa: Google Colab

Los notebooks incluyen soporte para ejecutarse en Google Colab con GPU gratuita.
Al ejecutar en Colab, el notebook detecta el entorno automáticamente y ajusta
las rutas a Google Drive.

## Estructura de archivos generados

```
data/
├── construction-ppe/          # Dataset descargado (Notebook 01)
├── dataset_config.json        # Configuración del dataset
├── eval_results.json          # Métricas de validación por modelo
├── latency_results.json       # Benchmarks de latencia
└── demo_stats.json            # Estadísticas del sistema de tracking

models/
├── yolov8n_best.pt            # Mejor checkpoint YOLOv8n
├── yolov8m_best.pt            # Mejor checkpoint YOLOv8m
└── yolov11n_best.pt           # Mejor checkpoint YOLOv11n

runs/
├── yolov8n_ppe/               # Logs de entrenamiento YOLOv8n
├── yolov8m_ppe/               # Logs de entrenamiento YOLOv8m
└── yolov11n_ppe/              # Logs de entrenamiento YOLOv11n
```
