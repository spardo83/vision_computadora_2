"""
PPE Monitor – Sistema de Monitoreo Automático de EPP en Obras de Construcción
==============================================================================

Paquete Python del Trabajo Práctico de Visión por Computadora II (CEIA-UBA).

Módulos principales (implementados en notebooks):
    - Detección: YOLOv8n / YOLOv8m / YOLOv11n fine-tuneados sobre Construction-PPE
    - Tracking: ByteTrack vía Ultralytics para identidades persistentes por trabajador
    - Compliance: Motor de evaluación con lógica de tres estados por EPP por trabajador
      (CUMPLE / NO_CUMPLE / SIN_DATO) y ventana deslizante configurable
    - Alertas: Notificaciones en tiempo real para incumplimiento sostenido

Dataset:
    Construction Site Safety – Roboflow Universe
    Clases: Hardhat, Mask, NO-Hardhat, NO-Mask, NO-Safety Vest,
            Person, Safety Cone, Safety Vest, machinery, vehicle

Referencia:
    Ver paper/monitoreo_epp_construccion.pdf para la descripción completa del sistema.
"""

__version__ = "0.1.0"
__authors__ = ["Bohórquez, María Gabriela", "Ferrari, Maira Daniela", "Pardo, Sebastián"]
