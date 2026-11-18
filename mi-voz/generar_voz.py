"""Genera audio con tu voz clonada a partir de un texto.

Uso:
  python generar_voz.py "Hola, soy Iré Publicidad." salidas/saludo.wav
  python generar_voz.py --archivo guion.txt salidas/guion.wav     (una frase por línea)

Opciones:
  --referencia  muestra de tu voz (por defecto muestras/referencia.wav)
  --pausa       segundos de silencio entre frases (por defecto 0.45)
  --emocion     0.3 = calmado · 0.5 = natural · 0.8 = muy expresivo
"""
import argparse, os, torch, torchaudio as ta
from chatterbox.mtl_tts import ChatterboxMultilingualTTS

p = argparse.ArgumentParser()
p.add_argument('texto', nargs='?', help='texto a decir (o usa --archivo)')
p.add_argument('salida', help='archivo .wav de salida')
p.add_argument('--archivo', help='archivo de texto, una frase por línea')
p.add_argument('--referencia', default=os.path.join(os.path.dirname(__file__), 'muestras', 'referencia.wav'))
p.add_argument('--pausa', type=float, default=0.45)
p.add_argument('--emocion', type=float, default=0.5)
p.add_argument('--idioma', default='es')
a = p.parse_args()

frases = [l.strip() for l in open(a.archivo, encoding='utf-8') if l.strip()] if a.archivo else [a.texto]
if not frases or not frases[0]:
    p.error('escribe un texto o usa --archivo')
if not os.path.exists(a.referencia):
    p.error(f'no encuentro la muestra de voz: {a.referencia}')

device = 'cuda' if torch.cuda.is_available() else ('mps' if torch.backends.mps.is_available() else 'cpu')
modelo = ChatterboxMultilingualTTS.from_pretrained(device=device)
partes = []
for i, f in enumerate(frases, 1):
    print(f'[{i}/{len(frases)}] {f}')
    w = modelo.generate(f, language_id=a.idioma, audio_prompt_path=a.referencia,
                        exaggeration=a.emocion, cfg_weight=0.5, temperature=0.75)
    partes += [w, torch.zeros(1, int(a.pausa * modelo.sr))]
os.makedirs(os.path.dirname(os.path.abspath(a.salida)), exist_ok=True)
ta.save(a.salida, torch.cat(partes, dim=1), modelo.sr)
print('Listo:', a.salida)
