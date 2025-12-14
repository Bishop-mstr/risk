import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_box(ax, x, y, text, w=2.8, h=0.9, color='#ddeeff'):
    rect = patches.FancyBboxPatch((x - w/2, y - h/2), w, h,
                                  boxstyle="round,pad=0.1",
                                  ec="black", fc=color, zorder=2)
    ax.add_patch(rect)
    ax.text(x, y, text, ha='center', va='center', fontsize=8, zorder=3, fontweight='bold')

def draw_arrow(ax, x1, y1, x2, y2):
    ax.annotate("", xy=(x2, y2 - 0.45), xytext=(x1, y1 + 0.45),
                arrowprops=dict(arrowstyle="->", lw=1.5, color='black'), zorder=1)

def draw_side_arrow(ax, x1, y1, x2, y2, text):
    ax.annotate("", xy=(x2 + 1.4, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="->", lw=1.5, color='black'), zorder=1)
    ax.text((x1+x2+1.4)/2, y1 + 0.1, text, ha='center', fontsize=9)

fig, ax = plt.subplots(figsize=(8, 10))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')
ax.set_title("Ієрархічна схема", fontsize=14)

draw_box(ax, 5, 0.5, "Альтернативи\n(x1, x2, x3, x4)")

draw_box(ax, 5, 2, "Матриця F\n(Збитки)")
draw_arrow(ax, 5, 0.5, 5, 2)

draw_box(ax, 2.5, 4, "ZI_1\n(Середньоквадратичне)")
draw_arrow(ax, 5, 2, 2.5, 4)

draw_box(ax, 7.5, 4, "ZI_5\n(Вальд)")
draw_arrow(ax, 5, 2, 7.5, 4)

draw_box(ax, 2.5, 6, "FI_1\n(Норм. Середньокв.)")
draw_arrow(ax, 2.5, 4, 2.5, 6)

draw_box(ax, 7.5, 6, "FI_5\n(Норм. Вальд)")
draw_arrow(ax, 7.5, 4, 7.5, 6)

draw_box(ax, 5, 7.5, "FF\n(Інтегральна матриця)")
draw_arrow(ax, 2.5, 6, 5, 7.5)
draw_arrow(ax, 7.5, 6, 5, 7.5)

draw_box(ax, 5, 9, "KU / Інтегральна оцінка\n(Оптимальне: x4)")
draw_arrow(ax, 5, 7.5, 5, 9)

draw_side_arrow(ax, 8.5, 9, 5, 9, "U = {1/3, 2/3}")
draw_box(ax, 9, 9, "Вектор Пріоритетів\n(U)", w=2.0, color='#fff0e0')

plt.tight_layout()
plt.savefig("scheme_task8_ukr.png")
plt.show()