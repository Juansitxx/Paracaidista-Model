# Modelo del Paracaidista

Este repositorio contiene la implementación de un modelo matemático que simula la caída de un paracaidista bajo la influencia de la gravedad y la resistencia del aire. Se resuelve utilizando tres métodos numéricos diferentes: **Euler**, **Runge Kutta**, y **Heun**, implementados en un solo archivo Python.

## Descripción

El modelo del paracaidista se basa en la solución de una ecuación diferencial ordinaria (ODE) que describe la velocidad del paracaidista en función del tiempo, teniendo en cuenta la resistencia del aire. Este proyecto compara tres métodos numéricos:

1. **Método de Euler**: Aproximación simple que utiliza diferencias finitas para resolver ODEs.
2. **Método de Runge Kutta**: Un método más preciso de orden 4 que mejora las estimaciones de Euler.
3. **Método de Heun**: También conocido como "Euler mejorado", es una versión refinada del método de Euler.

## Requisitos

Antes de ejecutar el script, asegúrate de tener instaladas las siguientes dependencias:

- **numpy**: Para cálculos numéricos.
- **matplotlib**: Para la visualización gráfica de los resultados.

Puedes instalar estas librerías ejecutando:
```bash
pip install numpy matplotlib
