# Act 4 - Mapa conceptual: Entradas y Salidas de un microcontrolador
# Reglas: conceptos en cajas, palabras de enlace en las flechas,
# jerarquía de lo general (arriba) a lo específico (abajo).
# Requiere: pip install matplotlib

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(16, 10))
ax.set_xlim(0, 16)
ax.set_ylim(0, 10.5)
ax.axis("off")

# ---------- paleta ----------
AZUL, VERDE, ROSA = "#a8d8ea", "#c9f2c9", "#ffd6de"
AMARILLO, GRIS, BLANCO = "#fff3b0", "#eeeeee", "#ffffff"

# ---------- funciones de dibujo ----------
def caja(x, y, texto, color, fs=11):
    """Dibuja un CONCEPTO (caja)."""
    ax.text(x, y, texto, ha="center", va="center", fontsize=fs,
            weight="bold",
            bbox=dict(boxstyle="round,pad=0.5", fc=color, ec="#333", lw=1.4))

def enlace(x1, y1, x2, y2, texto="", dx=0, dy=0.3, punteada=False):
    """Dibuja una relación (flecha) con su PALABRA DE ENLACE."""
    props = dict(arrowstyle="-|>", color="#333", lw=1.6, shrinkA=8, shrinkB=8)
    if punteada:
        props["linestyle"] = "--"
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1), arrowprops=props)
    if texto:
        ax.text((x1 + x2) / 2 + dx, (y1 + y2) / 2 + dy, texto, ha="center",
                va="center", fontsize=9, style="italic", color="#333",
                bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none"))

# ---------- NIVEL 1: concepto general ----------
caja(8, 9.7, "MICROCONTROLADOR", AZUL, 13)

# ---------- NIVEL 2: las dos ramas ----------
caja(4, 7.8, "ENTRADAS\n(reciben información del mundo)", VERDE, 11)
caja(12, 7.8, "SALIDAS\n(envían información al mundo)", ROSA, 11)
enlace(7.2, 9.6, 4.2, 8.15, "recibe datos de…", dx=-0.6)
enlace(8.8, 9.6, 11.8, 8.15, "envía datos a…", dx=0.6)

# ---------- NIVEL 3: clasificación ----------
caja(1.9, 6.1, "DIGITALES", VERDE)
caja(5.6, 6.1, "ANALÓGICAS", VERDE)
caja(9.0, 6.1, "DIGITALES", ROSA)
caja(13.3, 6.1, "ANALÓGICAS (PWM)", ROSA, 10)
enlace(3.5, 7.5, 2.1, 6.5, "se clasifican en", dx=-1.1, dy=0.1)
enlace(4.5, 7.5, 5.4, 6.5, "se clasifican en", dx=1.15, dy=0.1)
enlace(10.7, 7.5, 9.2, 6.5, "se clasifican en", dx=-1.15, dy=0.1)
enlace(13.2, 7.5, 13.2, 6.5, "se clasifican en", dx=1.5, dy=0)

# ---------- NIVEL 4: ejemplos ----------
caja(1.9, 4.6, "botón, interruptor,\nsensor DHT11", GRIS, 9)
caja(5.6, 4.6, "LDR, potenciómetro,\nsensor TMP36", GRIS, 9)
caja(9.0, 4.6, "LED, buzzer, relé", GRIS, 9)
caja(13.3, 4.6, "servo, motor DC,\nLED RGB", GRIS, 9)
enlace(1.9, 5.8, 1.9, 4.9, "por ejemplo", dx=1.35, dy=0)
enlace(5.6, 5.8, 5.6, 4.9, "por ejemplo", dx=1.45, dy=0)
enlace(9.0, 5.8, 9.0, 4.9, "por ejemplo", dx=1.35, dy=0)
enlace(13.3, 5.8, 13.3, 4.9, "por ejemplo", dx=1.5, dy=0)

# ---------- NIVEL 5: funciones en el código ----------
caja(1.9, 3.0, "digitalRead()", AMARILLO, 10)
caja(5.6, 3.0, "analogRead()", AMARILLO, 10)
caja(9.0, 3.0, "digitalWrite()", AMARILLO, 10)
caja(13.3, 3.0, "analogWrite()", AMARILLO, 10)
enlace(1.9, 4.2, 1.9, 3.4, "se lee con", dx=1.1, dy=0)
enlace(5.6, 4.2, 5.6, 3.4, "se lee con", dx=1.15, dy=0)
enlace(9.0, 4.2, 9.0, 3.4, "se controla con", dx=1.55, dy=0)
enlace(13.3, 4.2, 13.3, 3.4, "se controla con", dx=1.65, dy=0)

# ---------- NIVEL 6: notas técnicas ----------
caja(5.6, 1.6, "usa el ADC: convierte voltaje (0-5 V)\nen un número (0-1023)", BLANCO, 9)
caja(13.3, 1.6, "usa PWM: simula salida analógica\ncon pulsos digitales", BLANCO, 9)

enlace(5.6, 2.7, 5.6, 1.95, "se apoya en", dx=1.2, dy=0, punteada=True)
enlace(13.3, 2.7, 13.3, 1.95, "se apoya en", dx=1.3, dy=0, punteada=True)

# ---------- título y guardado ----------
ax.set_title("MAPA CONCEPTUAL: ENTRADAS Y SALIDAS (E/S) DE UN MICROCONTROLADOR",
             fontsize=13, weight="bold", pad=15)
plt.savefig("mapa_conceptual_ES.png", dpi=200, bbox_inches="tight")
plt.show()
