import math

PLANE = ("M0 -8 L1.7 -2.4 L8 1.2 L8 2.7 L1.7 1.6 L1.1 5.5 L3.5 7.3 L3.5 8.5 "
         "L0 7.5 L-3.5 8.5 L-3.5 7.3 L-1.1 5.5 L-1.7 1.6 L-8 2.7 L-8 1.2 L-1.7 -2.4 Z")

CX, CY = 27.0, 38.0          # spiral centre, sits low-left so the plane gets room
TURNS  = 2.15
TH_MAX = TURNS * 2 * math.pi
R_MAX  = 18.8
B      = R_MAX / TH_MAX
EXIT   = math.radians(-72)    # tail finishes near the top, aimed at the plane
PHASE  = TH_MAX + EXIT        # derived, so changing TURNS keeps the exit fixed

def pt(th):
    r = B * th
    a = PHASE - th
    return (CX + r * math.cos(a), CY + r * math.sin(a))

# sample, then fit a smooth polybezier through the samples (Catmull-Rom -> cubic)
N = 74
ths = [TH_MAX * i / N for i in range(N + 1)]
P = [pt(t) for t in ths]

d = ["M%.2f %.2f" % P[0]]
for i in range(len(P) - 1):
    p0 = P[i - 1] if i > 0 else P[0]
    p1, p2 = P[i], P[i + 1]
    p3 = P[i + 2] if i + 2 < len(P) else P[-1]
    c1 = (p1[0] + (p2[0] - p0[0]) / 6.0, p1[1] + (p2[1] - p0[1]) / 6.0)
    c2 = (p2[0] - (p3[0] - p1[0]) / 6.0, p2[1] - (p3[1] - p1[1]) / 6.0)
    d.append("C%.2f %.2f %.2f %.2f %.2f %.2f" % (c1[0], c1[1], c2[0], c2[1], p2[0], p2[1]))
spiral = "".join(d)

# the plane is placed, not tangent-derived: it reads better parked in the
# top-right corner with the tail sweeping up toward it
px, py, ang, SCALE = 45.5, 17.5, -38.0, 0.95

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect width="64" height="64" rx="14" fill="#0B1017"/>
  <path d="{spiral}" fill="none" stroke="#78B4EA" stroke-width="3.5"
        stroke-linecap="round" stroke-linejoin="round"/>
  <g transform="translate({px:.2f} {py:.2f}) rotate({ang:.1f}) scale({SCALE})">
    <path d="{PLANE}" fill="#FFFFFF"/>
  </g>
</svg>
'''
open("public/favicon.svg", "w").write(svg)
print("plane at %.1f,%.1f angle %.1f | bytes %d" % (px, py, ang, len(svg)))
