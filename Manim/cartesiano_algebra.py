from manim import *
config.tex_template.add_to_preamble(r"\usepackage{cancel}")
config.tex_template.add_to_preamble(r"\usepackage{amsmath}")
 
class sistemas_coordenados(Scene):
    def construct(self):
        # Crear las fórmulas con colores
        i_tong = MathTex(r"\hat{i}", color=RED)
        j_tong = MathTex(r"\hat{j}", color=GREEN)
        k_tong = MathTex(r"\hat{k}", color=BLUE)
        vec_x = MathTex(r"\Vec{x}=x\hat{i}", color=RED)
        vec_y = MathTex(r"\Vec{y}=y\hat{j}", color=GREEN)
        vec_z = MathTex(r"\Vec{z}=z\hat{k}", color=BLUE)
        vec_x_sum_y = MathTex(r"x\hat{i}+y\hat{j}", substrings_to_isolate=[r"\hat{i}", r"\hat{j}"])
        vec_x_sum_y.set_color_by_tex(r"\hat{i}", RED)
        vec_x_sum_y.set_color_by_tex(r"\hat{j}", GREEN)
        vector_s = MathTex(r"\Vec{s}=x\hat{i}+y\hat{j}", substrings_to_isolate=[r"x\hat{i}", r"y\hat{j}"])
        vector_s.set_color_by_tex(r"\hat{i}", RED)
        vector_s.set_color_by_tex(r"\hat{j}", GREEN)
        vec_s_sum_z = MathTex(r"\vec{r}=\vec{s}+z\hat{k}", substrings_to_isolate=[r"z\hat{k}"])
        vec_s_sum_z.set_color_by_tex(r"\hat{k}", BLUE)
        vector_rhat = MathTex(r"\Vec{r}=x\hat{i}+y\hat{j}+z\hat{k}", substrings_to_isolate=[r"x\hat{i}", r"y\hat{j}", r"z\hat{k}"])
        vector_rhat.set_color_by_tex(r"\hat{i}", RED)
        vector_rhat.set_color_by_tex(r"\hat{j}", GREEN)
        vector_rhat.set_color_by_tex(r"\hat{k}", BLUE)

        # Posicionamiento inicial
        formulas = [i_tong, j_tong, k_tong, vec_x, vec_y, vec_z, vec_x_sum_y, vector_s, vec_s_sum_z, vector_rhat]
        for formula in formulas:
            formula.move_to(ORIGIN)

        # ============ SECCIÓN 1 (0-5 segundos) ============
        texto1 = Text("Coordenadas Cartesianas").scale(0.8)
        self.play(Write(texto1), run_time=1.5)
        self.wait(0.5)
        self.play(FadeOut(texto1), run_time=1.5)
        self.wait(0.5)
        # Animación de vectores unitarios
        self.play(Write(i_tong), run_time=1)
        self.play(i_tong.animate.move_to([-2,1,0]), run_time=1)
        self.wait(0.5)
        self.play(Write(j_tong), run_time=1)
        self.play(j_tong.animate.move_to([0,1,0]), run_time=1)
        self.wait(0.5)
        self.play(Write(k_tong), run_time=1)
        self.play(k_tong.animate.move_to([2,1,0]), run_time=1)
        self.wait(1)

        # ============ SECCIÓN 2 (5-15 segundos) ============
        # Transformación a vectores componentes
        self.play(
            i_tong.animate.become(vec_x),
            run_time=1.5
        )
        self.play(
            i_tong.animate.move_to([-2,1,0]),
            run_time=1.5
        )
        self.wait(0.5)
        self.play(
            j_tong.animate.become(vec_y),
            run_time=1.5
        )
        self.play(
            j_tong.animate.move_to([0,1,0]),
            run_time=1.5
        )
        self.wait(0.5)
        self.play(
            k_tong.animate.become(vec_z),
            run_time=1.5
        )
        self.play(
            k_tong.animate.move_to([2,1,0]),
            run_time=1.5
        )
        self.wait(4)
        
        # ============ SECCIÓN 3 (15-25 segundos) ============
        # Transformación a vector resultante
        vec_s_transparente = vector_s.copy().set_opacity(0)
        
        self.play(
            i_tong.animate.become(vector_s),
            j_tong.animate.become(vec_s_transparente),
            k_tong.animate.to_corner(UP + RIGHT),
            run_time=2
        )
        self.wait(2)
        
        # ============ TRANSFORMACIÓN FINAL (25-30 segundos) ============
        vsz_inv = vec_s_sum_z.copy().set_opacity(0)
        self.play(
            i_tong.animate.become(vec_s_sum_z),
            k_tong.animate.become(vsz_inv),
            run_time=2
        )
        self.wait(1)
        self.play(
            i_tong.animate.become(vector_rhat),
            run_time=2,
        )
        self.wait(2)

class sistemas_coordenados_cilindricos(Scene):
    def construct(self):

        #definicion de variables en coordenadas cilindricas
         #sistema cilindrico
        vec_s=MathTex(r"\vec{s}=\vec{x}+\vec{y}")
        cos_phi=MathTex(r"\cos{\phi}=\frac{x}{s}")
        x=MathTex(r"x=s\cos{\phi}")
        sin_phi=MathTex(r"\sin{\phi}=\frac{y}{s}")
        y=MathTex(r"y=s\sin{\phi}")
        vec_s2=MathTex(r"\vec{s}=x\hat{i}+y\hat{j}")
        vec_s_tongo2=MathTex(r"\vec{s}=s(\cos{\phi}\hat{i}+\sin{\phi}\hat{j})")
        s_tongo=MathTex(r"\hat{s}=cos{\phi}\hat{i}+\sin{\phi}\hat{j}")
        vec_r=MathTex(r"\vec{r}=s\hat{s}+z\hat{k}")
        vec_vel=MathTex(r"\dot{\vec{r}}=\dot{s}\hat{s}+s{\dot\hat{s}}+\dot{z}\hat{k}")
        s_tongo_hat=MathTex(r"\dot{\hat{s}}=\frac{d\hat{s}}{dt}")
        dsdt=MathTex(r"\dot{\hat{s}}=\frac{d\hat{\phi}}{dt}\frac{d\hat{s}}{d\phi}")
        dsdt2=MathTex(r"\dot{\hat{s}}=\dot{\phi}(-\sin{\phi}\hat{i}+\cos{\phi}\hat{j})")
        vec_acel=MathTex(r"\ddot\vec{r}=\ddot{s}\hat{s}+\dot{s}\dot{\hat{s}}+\dot{s}\dot{\phi}\hat{\phi}+s\dot{\phi}\hat{\phi}+s\dot{\phi}\dot\hat{\phi}+\ddot{z}\hat{k}")
        vec_acel2=MathTex(r"(\ddot{s}-s\dot{\phi^2})\hat{s}+(s\ddot{\phi}+2\dot{s}\dot{\phi})\hat{\phi}+\ddot{z}\hat{k}")

        #hacer un array con todas las formulas para que partan todas en el origen
        formulas2=[vec_s, cos_phi, x, sin_phi, y, vec_s2, vec_s_tongo2, s_tongo, vec_r, vec_vel,s_tongo_hat, dsdt, dsdt2]

        for formula2 in formulas2:
            formula2.animate.move_to(ORIGIN)




        # Animación construcción vector s y ángulos
        self.play(Write(vec_r))  # Aparece vec_r
        self.wait(0.2)
        self.play(vec_r.animate.to_corner(UP+LEFT))  # Mueve vec_r a la esquina (sin desaparecer)
        self.play(Write(vec_s)) 
        self.wait(0.5)
        self.play(vec_s.animate.next_to(vec_r, DOWN, aligned_edge=LEFT))  # vec_s debajo de vec_r
        self.play(cos_phi.animate.move_to([-2,2,0]))
        self.wait(0.2)
        self.play(x.animate.move_to([2,2,0]))
        self.wait(0.2)
        self.play(sin_phi.animate.move_to([-2,0,0]))
        self.wait(0.2)
        self.play(y.animate.move_to([2,0,0]))
        self.wait(0.2)

        # Reorganiza elementos (opcional, si necesitas moverlos)
        self.play(
            cos_phi.animate.move_to([-2,3,0]),
            x.animate.move_to([2,3,0]),
            sin_phi.animate.move_to([-2,1,0]),
            y.animate.move_to([2,1,0])
        )

        # Escribe vec_s_tongo2 y lo coloca debajo de vec_s
        self.play(Write(vec_s_tongo2)) 
        self.play(vec_s_tongo2.animate.next_to(vec_s, DOWN, aligned_edge=LEFT))  # vec_s_tongo2 debajo de vec_s

        # Borra todo excepto vec_r, vec_s y vec_s_tongo2
        self.play(*[FadeOut(mob) for mob in self.mobjects if mob not in [vec_r, vec_s, vec_s_tongo2]])
        self.wait(0.5)


        # Posición inicial (ejemplo: esquina superior derecha)
        starting_pos = UP+RIGHT
        buff_distance = 0.4  # Espaciado vertical entre elementos

        # Escribe s_tongo y lo coloca en la esquina superior derecha
        self.play(Write(s_tongo))
        self.play(s_tongo.animate.to_corner(starting_pos))
        self.wait(0.2)

        # Escribe vec_vel debajo de s_tongo
        self.play(Write(vec_vel))
        self.play(vec_vel.animate.next_to(s_tongo, DOWN, aligned_edge=LEFT, buff=buff_distance))
        self.wait(0.2)

        # Escribe s_tongo_hat debajo de vec_vel
        self.play(Write(s_tongo_hat))
        self.play(s_tongo_hat.animate.next_to(vec_vel, DOWN, aligned_edge=LEFT, buff=buff_distance))
        self.wait(0.2)

        # Escribe dsdt debajo de s_tongo_hat
        self.play(Write(dsdt))
        self.play(dsdt.animate.next_to(s_tongo_hat, DOWN, aligned_edge=LEFT, buff=buff_distance))
        self.wait(0.2)

        # Escribe dsdt2 debajo de dsdt
        self.play(Write(dsdt2))
        self.play(dsdt2.animate.next_to(dsdt, DOWN, aligned_edge=LEFT, buff=buff_distance))
        self.wait(2)

