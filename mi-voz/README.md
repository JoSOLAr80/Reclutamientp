# Mi voz · Iré Publicidad

Aquí vive tu **voz clonada**: escribes un guion y obtienes el audio con tu propia voz,
sin volver a grabar. Usa [Chatterbox](https://github.com/resemble-ai/chatterbox)
(modelo abierto, licencia MIT, permite uso comercial, habla español).

> **Privacidad:** la carpeta `muestras/` NO se sube a GitHub (está en `.gitignore`).
> Guarda tu muestra de voz solo en tu computadora o en un repositorio **privado**.
> Con una muestra de tu voz cualquiera podría imitarte.

## 1. Graba tu muestra (una sola vez)
- 15 a 30 segundos hablando natural, en un cuarto silencioso con muebles o cortinas.
- Celular a un palmo de la boca. Sin música ni eco.
- Guárdala como `muestras/referencia.wav` (si es otro formato:
  `ffmpeg -i tu-audio.opus -ar 24000 -ac 1 muestras/referencia.wav`).

## 2. Instala (una sola vez)
Necesitas Python 3.10 o más reciente.
```bash
python3 -m venv .venv
source .venv/bin/activate          # en Windows: .venv\Scripts\activate
# Mac (Apple Silicon) o computadora con tarjeta NVIDIA:
pip install torch==2.6.0 torchaudio==2.6.0
# Computadora sin tarjeta gráfica (más lento):
# pip install torch==2.6.0 torchaudio==2.6.0 --index-url https://download.pytorch.org/whl/cpu
pip install -r requirements.txt
```
La primera vez descarga el modelo (unos 3 GB).

## 3. Genera audio con tu voz
```bash
python generar_voz.py "Sembramos hoy, cosechas clientes." salidas/eslogan.wav
python generar_voz.py --archivo guion.txt salidas/guion.wav      # una frase por línea
python generar_voz.py --archivo guion.txt salidas/guion.wav --emocion 0.7   # más energía
```

## Consejos
- Escribe "WhatsApp" normal; si alguna palabra suena rara, escríbela como se pronuncia.
- Si una frase sale mal, vuelve a generarla: cada intento suena un poco distinto.
- Los audios llevan una marca de agua inaudible (Perth) que identifica que fueron generados por IA.
