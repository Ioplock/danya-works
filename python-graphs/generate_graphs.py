from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


OUT = Path(__file__).resolve().parent
plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["axes.grid"] = True
plt.rcParams["figure.dpi"] = 140


def save(fig, name):
    fig.tight_layout()
    fig.savefig(OUT / name, dpi=180, bbox_inches="tight")
    plt.close(fig)


def graph_fnp_tangent_plane():
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection="3d")

    x = np.linspace(0.1, 3.2, 80)
    y = np.linspace(0.1, 4.2, 80)
    X, Y = np.meshgrid(x, y)
    Z = np.sqrt(25 * X**2 + 9 * Y**2)
    Zp = (25 * np.sqrt(3) * X + 9 * np.sqrt(5) * Y) / (2 * np.sqrt(30))

    ax.plot_surface(X, Y, Z, alpha=0.55, color="#6aaed6", linewidth=0)
    ax.plot_surface(X, Y, Zp, alpha=0.42, color="#f28e2b", linewidth=0)

    a = np.array([np.sqrt(3), np.sqrt(5), 2 * np.sqrt(30)])
    ax.scatter(*a, color="#b00020", s=45, label="A")
    n = np.array([25 * np.sqrt(3), 9 * np.sqrt(5), -2 * np.sqrt(30)])
    n = n / np.linalg.norm(n)
    line = np.vstack([a - 2.2 * n, a + 2.2 * n])
    ax.plot(line[:, 0], line[:, 1], line[:, 2], color="#b00020", lw=2, label="нормаль")

    ax.set_title("Поверхность и касательная плоскость в точке A")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.legend(loc="upper left")
    ax.view_init(elev=24, azim=-58)
    save(fig, "fnp_04_tangent_plane.png")


def graph_fnp_directional_derivative():
    fig = plt.figure(figsize=(7.4, 5.8))
    ax = fig.add_subplot(111, projection="3d")

    a = np.array([1.0, 2.0, 1.0])
    b = np.array([-1.0, 0.0, 0.0])
    ab = b - a
    grad = np.array([6.0, 1.0, 4.5])
    grad_scaled = grad / np.linalg.norm(grad) * 1.8

    ax.scatter(*a, color="#b00020", s=55, label="A(1; 2; 1)")
    ax.scatter(*b, color="#1f77b4", s=55, label="B(-1; 0; 0)")
    ax.quiver(*a, *ab, color="#1f77b4", arrow_length_ratio=0.12, lw=2.2, label=r"$\overrightarrow{AB}$")
    ax.quiver(*a, *grad_scaled, color="#59a14f", arrow_length_ratio=0.12, lw=2.2, label=r"$\nabla u(A)$")

    ax.plot([a[0], b[0]], [a[1], b[1]], [a[2], b[2]], color="#1f77b4", lw=1, alpha=0.35)
    ax.text(*(a + np.array([0.08, 0.08, 0.08])), "A", color="#b00020")
    ax.text(*(b + np.array([0.08, 0.08, 0.08])), "B", color="#1f77b4")

    ax.set_title("Направление AB и градиент в точке A")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_xlim(-1.6, 3.0)
    ax.set_ylim(-0.5, 2.8)
    ax.set_zlim(-0.2, 2.8)
    ax.legend(loc="upper left")
    ax.view_init(elev=24, azim=-52)
    save(fig, "fnp_03_directional_derivative.png")


def graph_fnp_extremum():
    x = np.linspace(0.8, 6.0, 300)
    y = np.linspace(0.8, 6.0, 300)
    X, Y = np.meshgrid(x, y)
    Z = Y**2 - 18 * np.log(X * Y) + 6 * X - 36 / 5

    fig, ax = plt.subplots(figsize=(7, 5.5))
    cs = ax.contour(X, Y, Z, levels=18, colors="#4c78a8", linewidths=0.8)
    ax.clabel(cs, inline=True, fontsize=7)
    ax.scatter([3], [3], color="#b00020", s=50, zorder=3)
    ax.annotate("минимум (3; 3)", xy=(3, 3), xytext=(3.25, 3.55),
                arrowprops=dict(arrowstyle="->", color="#b00020"),
                color="#b00020")
    ax.set_title("Линии уровня функции около точки минимума")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_aspect("equal", adjustable="box")
    save(fig, "fnp_05_extremum_contours.png")


def graph_integral_area_cartesian():
    x1 = np.linspace(-1, 3, 300)
    x2 = np.linspace(3, 7, 300)
    y1 = np.sqrt(x1 + 1)
    y2 = np.sqrt(7 - x2)

    fig, ax = plt.subplots(figsize=(7.5, 5))
    ax.plot(x1, y1, color="#1f77b4", lw=2, label=r"$y=\sqrt{x+1}$")
    ax.plot(x2, y2, color="#ff7f0e", lw=2, label=r"$y=\sqrt{7-x}$")
    ax.fill_between(x1, 0, y1, color="#1f77b4", alpha=0.25)
    ax.fill_between(x2, 0, y2, color="#ff7f0e", alpha=0.25)
    ax.scatter([-1, 3, 7], [0, 2, 0], color="#333333", s=25)
    ax.axhline(0, color="black", lw=1)
    ax.set_title("Фигура, ограниченная графиками")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    save(fig, "int_01_area_cartesian.png")


def graph_integral_polar():
    fig = plt.figure(figsize=(6.5, 6.5))
    ax = fig.add_subplot(111, projection="polar")
    first = True
    for center in [0, 2 * np.pi / 3, 4 * np.pi / 3]:
        ph_full = np.linspace(center - np.pi / 6, center + np.pi / 6, 500)
        rr_full = 2 * np.cos(3 * ph_full)
        ax.plot(
            ph_full,
            rr_full,
            color="#1f77b4",
            lw=1.8,
            label=r"$r=2\cos3\varphi$" if first else None,
        )
        first = False
    phi = np.linspace(0, 2 * np.pi, 1000)
    ax.plot(phi, np.ones_like(phi), color="#333333", lw=1.4, label=r"$r=1$")

    for center in [0, 2 * np.pi / 3, 4 * np.pi / 3]:
        ph = np.linspace(center - np.pi / 9, center + np.pi / 9, 300)
        rr = 2 * np.cos(3 * ph)
        ax.fill_between(ph, 1, rr, where=rr >= 1, color="#59a14f", alpha=0.35)

    ax.set_title(r"Части розы $r=2\cos3\varphi$, где $r\geq 1$")
    ax.set_rmax(2.15)
    ax.legend(loc="upper right", bbox_to_anchor=(1.25, 1.12))
    save(fig, "int_02_polar_area.png")


def graph_integral_hyperbola_region():
    x = np.linspace(-15 / 4, 15 / 4, 800)
    y_outer = 3 * np.sqrt(1 + x**2 / 25)
    y_inner = np.full_like(x, np.nan)
    mask = np.abs(x) >= 3
    y_inner[mask] = (5 / 3) * np.sqrt(x[mask] ** 2 - 9)

    fig, ax = plt.subplots(figsize=(7, 6))
    center = np.abs(x) <= 3
    ax.fill_between(x[center], -y_outer[center], y_outer[center], color="#59a14f", alpha=0.28)
    right = x >= 3
    left = x <= -3
    for part in [left, right]:
        ax.fill_between(x[part], y_inner[part], y_outer[part], color="#59a14f", alpha=0.28)
        ax.fill_between(x[part], -y_outer[part], -y_inner[part], color="#59a14f", alpha=0.28)

    ax.plot(x, y_outer, color="#1f77b4", lw=2, label=r"$\frac{y^2}{9}-\frac{x^2}{25}=1$")
    ax.plot(x, -y_outer, color="#1f77b4", lw=2)
    left = x <= -3
    right = x >= 3
    first = True
    for part in [left, right]:
        ax.plot(
            x[part],
            y_inner[part],
            color="#ff7f0e",
            lw=2,
            label=r"$\frac{x^2}{9}-\frac{y^2}{25}=1$" if first else None,
        )
        ax.plot(x[part], -y_inner[part], color="#ff7f0e", lw=2)
        first = False
    ax.scatter([-15 / 4, 15 / 4, -15 / 4, 15 / 4],
               [15 / 4, 15 / 4, -15 / 4, -15 / 4],
               color="#333333", s=22)
    ax.axhline(0, color="black", lw=0.8)
    ax.axvline(0, color="black", lw=0.8)
    ax.set_title("Область, вращаемая вокруг оси Ox")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_aspect("equal", adjustable="box")
    ax.legend(loc="upper center")
    save(fig, "int_03_hyperbola_region.png")


def graph_integral_arc_rect():
    x = np.linspace(2, 5, 400)
    y = np.log(x**2 - 1)
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(x, y, color="#1f77b4", lw=2)
    ax.scatter([2, 5], [np.log(3), np.log(24)], color="#333333", s=25)
    ax.set_title(r"Дуга $y=\ln(x^2-1)$, $2\leq x\leq 5$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    save(fig, "int_04a_arc_rect.png")


def graph_integral_arc_param():
    t = np.linspace(0, np.pi / 6, 400)
    x = 2 * np.cos(t) ** 3
    y = np.sin(t) ** 3
    fig, ax = plt.subplots(figsize=(6.5, 5))
    ax.plot(x, y, color="#1f77b4", lw=2)
    ax.scatter([x[0], x[-1]], [y[0], y[-1]], color="#333333", s=25)
    ax.set_title(r"Параметрическая дуга, $0\leq t\leq \pi/6$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_aspect("equal", adjustable="box")
    save(fig, "int_04b_arc_param.png")


def graph_integral_surface_curve():
    t = np.linspace(0, 2 * np.pi, 900)
    x = 2 * np.cos(t) - np.cos(2 * t)
    y = 2 * np.sin(t) - np.sin(2 * t)

    fig, ax = plt.subplots(figsize=(7, 5.5))
    ax.plot(x, y, color="#9aa0a6", lw=1.5, label="вся кривая")
    upper = (t >= 0) & (t <= np.pi)
    ax.plot(x[upper], y[upper], color="#1f77b4", lw=2.8, label="верхняя половина")
    ax.axhline(0, color="black", lw=0.8)
    ax.axvline(0, color="black", lw=0.8)
    ax.set_title("Кривая, вращаемая вокруг оси Ox")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_aspect("equal", adjustable="box")
    ax.legend()
    save(fig, "int_05_surface_curve.png")


def graph_integral_surface_3d():
    t = np.linspace(0, np.pi, 220)
    theta = np.linspace(0, 2 * np.pi, 160)
    T, TH = np.meshgrid(t, theta)
    x = 2 * np.cos(T) - np.cos(2 * T)
    radius = 2 * np.sin(T) - np.sin(2 * T)
    y = radius * np.cos(TH)
    z = radius * np.sin(TH)

    fig = plt.figure(figsize=(8, 5.8))
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(x, y, z, color="#6aaed6", alpha=0.75, linewidth=0, antialiased=True)
    ax.set_title("Поверхность вращения вокруг оси Ox")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.view_init(elev=22, azim=-60)
    save(fig, "int_05_surface_3d.png")


def graph_integral_physics_model():
    fig, ax = plt.subplots(figsize=(7, 4.6))
    ax.set_aspect("equal", adjustable="box")

    earth = plt.Circle((0, 0), 1.0, color="#6aaed6", alpha=0.8)
    ax.add_patch(earth)
    ax.plot(0, 0, "o", color="#333333", ms=4)

    theta = np.deg2rad(28)
    r0 = 1.0
    r1 = 1.65
    p0 = np.array([r0 * np.cos(theta), r0 * np.sin(theta)])
    p1 = np.array([r1 * np.cos(theta), r1 * np.sin(theta)])

    ax.plot([0, p0[0]], [0, p0[1]], color="#333333", lw=1.4)
    ax.plot([0, p1[0]], [0, p1[1]], color="#333333", lw=1.0, ls="--")
    ax.annotate("", xy=p1, xytext=p0, arrowprops=dict(arrowstyle="->", lw=2.2, color="#b00020"))
    ax.scatter([p0[0], p1[0]], [p0[1], p1[1]], color=["#333333", "#b00020"], s=35, zorder=4)

    mid_r = 1.34
    pmid = np.array([mid_r * np.cos(theta), mid_r * np.sin(theta)])
    tangent = np.array([-np.sin(theta), np.cos(theta)])
    h0 = pmid - 0.15 * tangent
    h1 = pmid + 0.15 * tangent
    ax.plot([h0[0], h1[0]], [h0[1], h1[1]], color="#b00020", lw=1.5)
    ax.text(*(pmid + 0.18 * tangent), "H", color="#b00020", ha="center", va="center")

    ax.text(*(p0 + np.array([0.03, -0.08])), "r=R", color="#333333")
    ax.text(*(p1 + np.array([0.04, 0.03])), "r=R+H", color="#b00020")
    ax.text(-0.08, -0.12, "центр", color="#333333")
    ax.text(-0.28, -0.02, "Земля", color="white", weight="bold")
    ax.text(1.8, 0.55, r"$F(r)=\frac{MgR^2}{r^2}$", fontsize=13)
    ax.text(1.8, 0.32, r"$A=\int_R^{R+H}F(r)\,dr$", fontsize=13)

    ax.set_title("Физическая модель подъема тела")
    ax.set_xlim(-1.25, 3.0)
    ax.set_ylim(-1.15, 1.55)
    ax.axis("off")
    save(fig, "int_07_physics_model.png")


def main():
    graph_fnp_directional_derivative()
    graph_fnp_tangent_plane()
    graph_fnp_extremum()
    graph_integral_area_cartesian()
    graph_integral_polar()
    graph_integral_hyperbola_region()
    graph_integral_arc_rect()
    graph_integral_arc_param()
    graph_integral_surface_curve()
    graph_integral_surface_3d()
    graph_integral_physics_model()


if __name__ == "__main__":
    main()
