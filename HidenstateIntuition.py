from manim import *

class HiddenhidenStateIntuition(Scene):
    def construct(self):
       
        hiden = Text("Hidden Computations",font_size= 32)
        Inputt = Text("RNN Input",font_size= 32).to_edge(LEFT)
        Output= Text("RNN Output",font_size= 32).to_edge(RIGHT)
        arrow_to_hidn = Arrow(Inputt.get_left(), hiden.get_left(), buff=2)
        arrow_to_output = Arrow(hiden.get_right(), Output.get_left(), buff=2)
        self.play(Write(hiden))
        self.play(Write(Inputt))
        self.play(Write(Output))
        self.play(GrowArrow(arrow_to_hidn))
        self.play(GrowArrow(arrow_to_output))
        self.wait(5)

        self.remove(hiden)
        self.remove(Inputt)
     
class yhat(Scene):
    def construct(self):
        h4 = MathTex("\hat{y} = h_8 * W^s")
        self.play(Write(h4))
        self.wait(4)