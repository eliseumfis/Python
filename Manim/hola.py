from manim import *
import numpy as np

# Desactivar LaTeX completamente
config.disable_caching = True

class PhotoelectricEffect3D(ThreeDScene):
    def construct(self):
        # Configurar la cámara
        self.set_camera_orientation(phi=65 * DEGREES, theta=45 * DEGREES)
        
        # Datos experimentales (nA)
        voltages = np.array([-4.5, -2.5, -0.5, 1.5, 3.5, 5.5, 7.5, 9.5, 
                           11.5, 13.5, 15.5, 17.5, 19.5, 21.5, 23.5, 25.5, 27.5, 29.5])
        
        data_365 = np.array([0.01, 0.00, 1.64, 2.43, 2.44, 2.44, 2.50, 2.59, 
                           2.50, 2.44, 2.55, 2.44, 2.53, 2.51, 2.49, 2.46, 2.58, 2.33])
        
        data_405 = np.array([0.01, 0.00, 1.86, 3.40, 3.79, 3.96, 3.95, 4.05,
                           4.04, 3.94, 3.86, 3.77, 3.77, 3.96, 4.02, 4.28, 3.94, 4.21])
        
        data_436 = np.array([0.00, 0.00, 2.24, 4.79, 5.64, 5.87, 6.16, 5.71,
                           6.00, 5.92, 5.67, 5.73, 6.00, 5.99, 5.55, 6.06, 5.32, 6.03])
        
        wavelengths = np.array([365, 405, 436])
        
        # Colores del espectro
        color_365 = "#8B00FF"  # UV/Violeta
        color_405 = "#7B00FF"  # Violeta
        color_436 = "#4169E1"  # Azul
        
        # Normalizar datos
        v_norm = (voltages - voltages.min()) / (voltages.max() - voltages.min()) * 6 - 3
        w_norm = (wavelengths - wavelengths.min()) / (wavelengths.max() - wavelengths.min()) * 4 - 2
        
        # Crear ejes 3D simples
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
            z_range=[0, 7, 1],
            x_length=7,
            y_length=5,
            z_length=5,
            axis_config={"color": BLUE_E, "include_tip": False},
        )
        
        # Etiquetas usando Text (sin LaTeX)
        x_label = Text("Voltaje (V)", font_size=28, color=WHITE)
        x_label.rotate(90 * DEGREES, axis=UP)
        x_label.next_to(axes.x_axis, RIGHT, buff=0.5)
        
        y_label = Text("Long. onda (nm)", font_size=28, color=WHITE)
        y_label.rotate(90 * DEGREES, axis=RIGHT)
        y_label.next_to(axes.y_axis, UP, buff=0.5)
        
        z_label = Text("Corriente (nA)", font_size=28, color=WHITE)
        z_label.rotate(90 * DEGREES, axis=OUT)
        z_label.next_to(axes.z_axis, OUT, buff=0.8)
        
        # Función de superficie
        def surface_func(u, v):
            if v <= 0:
                t = (v + 2) / 2
                v_idx = np.interp(u, v_norm, np.arange(len(voltages)))
                i1 = np.interp(v_idx, np.arange(len(data_365)), data_365)
                i2 = np.interp(v_idx, np.arange(len(data_405)), data_405)
                current = i1 + t * (i2 - i1)
            else:
                t = v / 2
                v_idx = np.interp(u, v_norm, np.arange(len(voltages)))
                i2 = np.interp(v_idx, np.arange(len(data_405)), data_405)
                i3 = np.interp(v_idx, np.arange(len(data_436)), data_436)
                current = i2 + t * (i3 - i2)
            
            return np.array([u, v, current * 0.8])
        
        # Crear superficie
        surface = Surface(
            surface_func,
            u_range=[-3, 3],
            v_range=[-2, 2],
            resolution=(30, 15),
            fill_opacity=0.7,
            checkerboard_colors=[BLUE_D, BLUE_E],
            stroke_width=0.5,
        )
        
        # Crear curvas de datos
        points_365 = [axes.c2p(v_norm[i], w_norm[0], data_365[i] * 0.8) for i in range(len(voltages))]
        curve_365 = VMobject(color=color_365, stroke_width=5)
        curve_365.set_points_as_corners(points_365)
        
        points_405 = [axes.c2p(v_norm[i], w_norm[1], data_405[i] * 0.8) for i in range(len(voltages))]
        curve_405 = VMobject(color=color_405, stroke_width=5)
        curve_405.set_points_as_corners(points_405)
        
        points_436 = [axes.c2p(v_norm[i], w_norm[2], data_436[i] * 0.8) for i in range(len(voltages))]
        curve_436 = VMobject(color=color_436, stroke_width=5)
        curve_436.set_points_as_corners(points_436)
        
        # Puntos de datos
        dots_365 = VGroup(*[Dot3D(p, color=color_365, radius=0.06) for p in points_365])
        dots_405 = VGroup(*[Dot3D(p, color=color_405, radius=0.06) for p in points_405])
        dots_436 = VGroup(*[Dot3D(p, color=color_436, radius=0.06) for p in points_436])
        
        # Títulos (fijados a la cámara)
        title = Text("Efecto Fotoelectrico", font_size=48, color=WHITE, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        
        subtitle = Text("Fotocorriente vs Voltaje y Longitud de Onda", font_size=32, color=WHITE)
        subtitle.next_to(title, DOWN, buff=0.3)
        
        # Leyenda
        legend = VGroup(
            Text("365 nm (UV)", font_size=20, color=color_365),
            Text("405 nm (Violeta)", font_size=20, color=color_405),
            Text("436 nm (Azul)", font_size=20, color=color_436),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        legend.to_corner(UL, buff=1).shift(DOWN * 2)
        
        # === ANIMACIONES ===
        
        # Fijar elementos 2D a la cámara
        self.add_fixed_in_frame_mobjects(title, subtitle, legend)
        
        # Mostrar títulos
        self.play(
            Write(title),
            Write(subtitle),
            run_time=1.5
        )
        self.wait(0.5)
        
        # Mostrar ejes y etiquetas
        self.play(
            Create(axes),
            Write(x_label),
            Write(y_label),
            Write(z_label),
            run_time=2
        )
        self.wait(0.5)
        
        # Mostrar superficie
        self.play(Create(surface), run_time=3)
        self.wait(0.5)
        
        # Mostrar curvas
        self.play(
            Create(curve_365),
            Create(curve_405),
            Create(curve_436),
            run_time=2
        )
        
        # Mostrar puntos
        self.play(
            FadeIn(dots_365),
            FadeIn(dots_405),
            FadeIn(dots_436),
            run_time=1
        )
        
        # Mostrar leyenda
        self.play(FadeIn(legend), run_time=1)
        self.wait(1)
        
        # Rotación de cámara
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(10)
        self.stop_ambient_camera_rotation()
        
        self.wait(2)