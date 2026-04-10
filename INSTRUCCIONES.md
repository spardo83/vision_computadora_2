# Instrucciones de Ejecución – Paso a Paso

## 1. Setup del entorno (una sola vez)

Abrí una terminal en VS Code en la carpeta `computer_vision_2_tp/` y ejecutá:

```bash
# Crear entorno virtual con uv
uv venv

# Activar entorno
source .venv/bin/activate        # Linux / Mac
# .venv\Scripts\activate         # Windows PowerShell

# Instalar dependencias
uv pip install -e .

# Instalar PyTorch CPU (sin CUDA)
uv pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu

# Registrar el kernel para Jupyter en VS Code
python -m ipykernel install --user --name=ppe-monitor --display-name "PPE Monitor"
```

## 2. Seleccionar el kernel en VS Code

Al abrir cada notebook en VS Code, seleccionar el kernel **"PPE Monitor"** (arriba a la derecha del notebook).

## 3. Obtener API Key de Roboflow

1. Crear cuenta gratuita en https://roboflow.com
2. Ir a Account → API Keys → copiar la key
3. En el **Notebook 1**, reemplazar `"TU_API_KEY_AQUI"` con la key

## 4. Ejecutar los notebooks en orden

| Notebook | Qué hace | Tiempo estimado (CPU) |
|---|---|---|
| `01_setup_and_dataset.ipynb` | Descarga dataset + EDA | ~5 min |
| `02_model_training.ipynb` | Entrena 3 modelos YOLO | ~2-4 hs (15 epochs CPU) |
| `03_model_comparison.ipynb` | Compara métricas | ~10 min |
| `04_tracking_demo.ipynb` | Demo con video | ~15 min |

> **Consejo para CPU:** El entrenamiento puede tardar. Para probar rápido,
> reducir `EPOCHS = 5` en el Notebook 2. Para resultados finales del TP, usar 15-30.

## 5. Publicar en GitHub

```bash
# Instalar gh CLI si no está: https://cli.github.com
# Autenticar: gh auth login

chmod +x setup_github.sh
./setup_github.sh
```

O manualmente:
```bash
git init
git add .
git commit -m "feat: initial commit"
git branch -M main
git remote add origin https://github.com/spardo83/computer_vision_2_tp.git
git push -u origin main
```

## Tips

- Los notebooks están diseñados para correr **en secuencia** – el Notebook 2 requiere el `dataset_config.json` generado por el Notebook 1, etc.
- Los archivos generados se guardan en `data/` (JSONs con métricas) y `models/` (pesos `.pt`)
- El video de demo del Notebook 4 se guarda en `videos/output_tracked.mp4`
