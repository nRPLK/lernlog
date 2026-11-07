# Lernlog Python – Übung 01: Reihenschwingkreis (HWE Bsp. 2.55)
# Ziel: Variablen, math-Modul, Funktionen, f-Strings
# Kontrolle: f_r = 711,8 Hz | I_r = 100 mA | Q = 2,236 | B = 318,3 Hz | U_L = U_C = 22,36 V

import math

# Gegebene Werte (SI-Einheiten!)
R = 100        # Ohm
L = 50e-3      # Henry  (50 mH)
C = 1e-6       # Farad  (1 µF)
U = 10         # Volt
X_C=0
X_L=0

# TODO 1: Resonanzfrequenz  f_r = 1 / (2·π·√(L·C))
f_r = 1/(2*math.pi*math.sqrt(L*C))

# TODO 2: Strom bei Resonanz  I_r = U / R   (bei f_r heben sich X_L und X_C auf)
I_r = U / R

# TODO 3: Güte  Q = (1/R) · √(L/C)
Q = (1/R) * math.sqrt(L/C)

# TODO 4: Bandbreite  B = f_r / Q
B = f_r / Q

# TODO 5: Blindwiderstand bei f_r  X_L = 2·π·f_r·L   und Spannung  U_L = I_r · X_L


X_L = 2* math.pi *f_r*L
X_C = 1/(2*math.pi*f_r*C)
U_L = I_r * X_L

print(f"f_r = {f_r:.1f} Hz")
print(f"I_r = {I_r*1000:.0f} mA")
print(f"Q   = {Q:.3f}")
print(f"B   = {B:.1f} Hz")
print(f"U_L = U_C = {U_L:.2f} V")

# BONUS: Schreib eine Funktion  impedanz(f)  die |Z| = √(R² + (X_L − X_C)²) zurückgibt,
# und gib |Z| für 0,8·f_r, f_r und 1,25·f_r aus.  Kontrolle: bei 0,8·f_r ca. 141,9 Ω



def quadrat(x):
    return x*x

def impedanz(f):
    X_L = 2* math.pi *f*L
    X_C = 1/(2*math.pi*f*C)
    return math.sqrt(quadrat(R)+quadrat(X_L-X_C))

print(f"|Z| bei 0.8= {impedanz(0.8*f_r):.2f}")
print(f"|Z|= {impedanz(f_r):.2f}")
print(f"|Z| bei 1.25= {impedanz(1.25*f_r):.2f}")

for i in range(50,751,100):
    print(f"|Z| bei {i}={impedanz(i):.2f}")