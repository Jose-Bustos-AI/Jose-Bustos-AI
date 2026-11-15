# Cómo regenerar los gráficos del perfil

1. (Opcional) Repetir las capturas de las webs: `capturas.ps1` lanza Chrome en segundo plano. Hay que ajustar dentro la carpeta de salida y pasar las capturas a JPG en `capturas/`.
2. Generar los SVG animados: `python herramientas/generar.py herramientas/capturas assets`
3. Para añadir o quitar una tarjeta, editar la lista `CARDS` de `generar.py` y la tabla correspondiente del `README.md`.

Las tarjetas llevan la captura incrustada, así que no dependen de ningún servicio externo. La serpiente la genera cada día el flujo `.github/workflows/serpiente.yml` en la rama `output`.
