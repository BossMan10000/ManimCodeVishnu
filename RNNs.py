
from manim import *

class IntrotoRNNs(Scene):
    def construct(self):
        Title = Text("Recurrent Nueral Network or RNN", font_size= 60, color = BLUE)
        description = Text("Accounts for negated words", font_size = 40, color = GREY).next_to(Title, DOWN*2)
        self.play(Write(Title))
        self.play(Write(description))
        self.wait(33)

class TokenEncoding(Scene):
    def construct(self):
        sentence = Text("I am not feeling bad", font_size=30,color = GREY)
        sentence1 = Text("I am not feeling bad", font_size=56,color = GREY)
        tword1 = sentence[0:2].set_color(BLUE)
        tword2 = sentence[2:6].set_color(BLUE)
        tword3 =sentence[6:9].set_color(BLUE)
        tword4 = sentence[9:11].set_color(BLUE)
        tword5 = sentence[11:15].set_color(BLUE)
        tword6 = sentence[15:18].set_color(BLUE)
        tword7 = sentence[18:24].set_color(BLUE)
        self.wait(6)
        Tokenized = Text("Tokenized Version",font_size=40).shift(UP*3)
        self.play(Write(sentence1))
        self.wait(9)
        self.clear()
        self.play(Write(Tokenized))
        self.add(Group(tword1,tword2,tword3,tword4,tword6,tword7).arrange(DOWN,buff =0.8))
        self.wait(10.5)
        self.remove(tword1)
        self.remove(tword2)
        self.remove(tword3)
        self.remove(tword4)
        self.remove(tword5)
        self.remove(tword6)
        self.remove(tword7)
        word1 = Text("I",font_size=36,color = BLUE)
        word2 = Text("am",font_size=36,color = BLUE)
        word3 = Text("not",font_size=36,color = BLUE)
        word4 = Text("feeling",font_size=36,color = BLUE)
        word5 = Text("bad",font_size=36,color = BLUE)
        self.add(Group(word1,word2,word3,word4,word5).arrange(DOWN,buff =0.8))
        self.wait(12)
        self.play(Tokenized.animate.shift(LEFT*4))
        self.play(word1.animate.shift(LEFT*4))
        self.play(word2.animate.shift(LEFT*4))
        self.play(word3.animate.shift(LEFT*4))
        self.play(word4.animate.shift(LEFT*4))
        self.play(word5.animate.shift(LEFT*4))
        self.wait(10.5)
        m0 = Matrix([[0],[0],[0]]).set_row_colors(GREEN,RED,GREY).shift(RIGHT*2+UP*1)
        m01 = Matrix([[0],[0],[0]]).set_row_colors(GREEN,RED,GREY).shift(RIGHT*4+UP*1)
        m02 = Matrix([[0],[0],[1]]).set_row_colors(GREEN,RED,GREY).shift(RIGHT*6+UP*1)
        m03 = Matrix([[0],[0],[0]]).set_row_colors(GREEN,RED,GREY).shift(RIGHT*2+DOWN*2)
        m04 = Matrix([[0],[1],[0]]).set_row_colors(GREEN,RED,GREY).shift(RIGHT*4+DOWN*2)
        Newinput = Matrix([[" Positive \\ Sentiment "], [" Negative \\ Sentiment "], ["Inverter"]], h_buff=1.5, v_buff=1.2, element_alignment_corner=np.array([0.5,0.5,0])).shift(RIGHT*2)
        RespectiveVector = Text("Respective Vector Representation",font_size=40).shift(UP*3+RIGHT*3)
        self.play(Write(Newinput))
        self.wait(28.5)
        self.play(FadeTransform(Newinput,m0))
        self.play(Write(RespectiveVector))
        self.play(Write(m01))
        self.play(Write(m02))
        self.play(Write(m03))
        self.play(Write(m04))
        self.play(word1.animate.shift(LEFT*1+DOWN*1))
        self.play(word3.animate.shift(RIGHT*1 +UP *1.1))
        self.play(word4.animate.shift(LEFT*0.4+DOWN*0.92))
        self.play(word5.animate.shift(UP*0.3+RIGHT*1.2))

        self.wait(7.5) 

class HiddenStateIntuition(Scene):
    def construct(self):
        word1 = Text('"feeling"',font_size=56,color = BLUE).shift(LEFT*4+DOWN*1)
        m0 = Matrix([[0],[0],[0]]).set_row_colors(GREEN,RED,GREY).shift(DOWN*1)
        HiddenVec = Text("[...]", gradient = (GREEN,RED)).shift(RIGHT*4+DOWN*1)
        Token = Text("Token", font_size = 40).shift(UP*2 +LEFT*4)
        Embedding = Text("Embedded Token", font_size = 40).shift(UP*2)
        HiddenVector= Text("Hidden Vector", font_size = 40).shift(UP*2+RIGHT*4)
        self.play(Write(Token))
        self.play(Write(Embedding))
        self.play(Write(HiddenVector))
        self.play(Write(word1))
        self.play(Write(m0))
        self.play(Write(HiddenVec))
        arrow_to_vec = Arrow(word1.get_left(), m0.get_left(), buff=2)
        arrow_to_hiddenvec = Arrow(m0.get_left(), HiddenVec.get_left(), buff=0.8)
        self.play(GrowArrow(arrow_to_vec))
        self.play(GrowArrow(arrow_to_hiddenvec))
        self.wait(9) 
        self.remove(m0)
        self.remove(HiddenVec)
        hiden = Text("Hidden Computations")
        Inputt = Text("RNN Input").to_edge(LEFT*2)
        Output= Text("RNN Output").to_edge(RIGHT*2)
        arrow_to_hidn = Arrow(Inputt.get_left(), hiden.get_left(), buff=2)
        arrow_to_output = Arrow(hiden.get_left(), Output.get_left(), buff=2)
        self.play(GrowArrow(arrow_to_hidn))
        self.play(GrowArrow(arrow_to_output))
        self.play(FadeTransform(Embedding,hiden))
        self.remove(FadeTransform(Token,Inputt))
        self.remove(FadeTransform(HiddenVector,Output))
        self.remove(arrow_to_hidn)
        self.remove(arrow_to_output)
        self.remove(hiden)
        self.remove(Inputt)
    
        self.wait(5)
        HiddenLayertxt= Text("Hidden Layer").shift(UP*3+LEFT*4)
        HiddenVec = Text("[...]", gradient = (GREEN,RED)).shift(LEFT*4)
        HiddenVec1 = Text("[...]", gradient = (GREEN,RED)).shift(LEFT*4)
        HiddenVec2 = Text("[...]", gradient = (GREEN,RED)).shift(LEFT*4)
        HiddenVec3 = Text("[...]", gradient = (GREEN,RED)).shift(LEFT*4)
        self.play(FadeTransform(Output,HiddenLayertxt))
        self.add(Group(HiddenVec,HiddenVec1,HiddenVec2,HiddenVec3).arrange(DOWN,buff =0.8).shift(LEFT*4))
        self.wait(35) 
        hidnvec = Matrix([["No. \\ Positive \\ Words"], ["No. \\ Negative \\ Words"], ["Was \\ Previous \\ Word \\ Inverter?"], ["Inverted \\ Negative?"], ["Inverted \\ Positive?"]], h_buff=1.5, v_buff=1).to_edge(RIGHT)
        self.play(Write(hidnvec))
        self.remove(HiddenVec)
        self.remove(HiddenVec1)
        self.remove(HiddenVec2)
        self.remove(HiddenVec3)
        h =  MathTex("h").shift(LEFT*4)
        h1 = MathTex("h^1")
        h2 = MathTex("h^2")
        h3 = MathTex("h^3")
        h4 = MathTex("h^4")
        h5 = MathTex("h^5")
        self.wait(10)
        

        # Assemble the matrix (1 column, 5 rows)
        matrix = Matrix(
            [
                ["h^1"],
                ["h^2"],  # Use LaTeX for vertical dots
                ["h^3"],
                ["h^4"],
                ["h^5"],
            ]
        ).shift(LEFT*4)
        
        # Style the matrix (optional)
        matrix.set_column_colors(BLUE)
        equal = Text("=").next_to(h,RIGHT*6)
        self.play(FadeTransform(HiddenLayertxt,h))
        self.play(Write(equal))
        
        # Position and animate the matrix
        matrix.scale(1.5)  # Make it larger
        self.play(FadeTransform(h,matrix))
        
        self.wait(6)
        matrix1 = Matrix(
            [
                ["h^1_t"],
                ["h^2_t"],  # Use LaTeX for vertical dots
            ]
        ).shift(LEFT*4)
        hidnvecsimp = Matrix([["No. \\ Positive \\ Words"], ["No. \\ Negative \\ Words"]], h_buff=1.5, v_buff=1).shift(RIGHT*2)
        self.play(FadeTransform(matrix,matrix1))
        self.play(FadeTransform(hidnvec,hidnvecsimp))
        self.wait(59)
        yhat = MathTex("\hat{y}").shift(LEFT*3.2)
        ht1=MathTex("h^1_t - h^2_t")
        self.play(FadeTransform(matrix1, yhat))
        self.play(FadeTransform(hidnvecsimp,ht1))
        self.wait(33)

class Hidden_State_Computations(Scene):
    def construct(self):
        # Nonlinear functions, weights, biases
        self.wait(4.25)
        parameters = VGroup(Text("Nonlinear functions",font_size=50,color=YELLOW),Text("Weights",font_size=50,color=BLUE),Text("Biases",font_size=50,color=PURPLE)).arrange(DOWN, buff=0.5)
        self.play(Write(parameters))
        self.wait(0.75)
        self.play(FadeOut(parameters[1],parameters[2]),parameters[0].animate.move_to(UP*3))

        # Nonlinear functions
        sigmoid_axes = Axes(
            x_range=[-6, 6, 1],
            y_range=[-0.25, 1.5, 1],
            axis_config={"color": WHITE}
        )
        sigmoid_curve = sigmoid_axes.plot(lambda x: 1 / (1 + np.exp(-x)), color=BLUE)
        sigmoid_label = Text("Sigmoid", font_size=40).next_to(sigmoid_axes,UP,buff=1)
        sigmoid = VGroup(sigmoid_axes, sigmoid_curve, sigmoid_label).scale(0.5)
        relu_axes = Axes(
            x_range=[-6, 6, 1],
            y_range=[-1, 6, 1],
            axis_config={"color": WHITE}
        )
        relu_curve = relu_axes.plot(lambda x: max(0, x), color=RED)
        relu_label = Text("ReLU", font_size=40).next_to(relu_axes,UP,buff=1)
        relu = VGroup(relu_axes, relu_curve, relu_label).scale(0.5)
        graph_group = VGroup(sigmoid, relu).arrange(RIGHT, buff=1)
        self.play(Write(graph_group))
        self.wait(16)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        # Weights
        circles = VGroup(
            *[Circle(radius=0.2, color=BLUE) for _ in range(4)]
        )
        labels = VGroup(
            *[Text(f"input {i + 1}", font_size=24) for i in range(4)]
        )
        for label, circle in zip(labels, circles):
            label.next_to(circle, LEFT)
        elements = VGroup(
            *[VGroup(circle, label) for circle, label in zip(circles, labels)]
        ).arrange(DOWN, buff=1.25).shift(LEFT*3.5)
        lines = VGroup()
        weight_labels = VGroup()
        for i, circle in enumerate(circles):
            angles = [PI / 6, PI / 4, PI / 3]
            lengths = [2, 3, 4]
            direction_vectors = [
                np.array([np.cos(angle), np.sin(angle), 0])
                for angle in angles
            ]
            end_points = [
                lengths[i] * direction_vectors[i] - np.array([0, 2, 0])
                for i in range(len(lengths))
            ]
            for j in range(3):
                line = Line(start=circle.get_center(), end=end_points[j], color=GRAY)
                lines.add(line)

        proportions=[0.2,0.5,0.7,0.2,0.5,0.7,0.2,0.5,0.7,0.2,0.5,0.7]
        for i,line in enumerate(lines):
            angle = line.get_angle()
            endpoint = line.point_from_proportion(proportions[i])
            weight_label = MathTex(rf"\times w",color=BLUE).scale(0.75).move_to(endpoint)
            weight_label.rotate(angle)
            weight_labels.add(weight_label)
        self.play(Write(elements))
        self.play(Write(lines))
        self.play(Write(weight_labels))
        self.wait(5)

        # Bias
        bias = Text("+ b",color=PURPLE).scale(2).next_to(lines,RIGHT)
        self.play(Write(bias))
        self.wait(8)
        wx = Text("wx",color=BLUE).scale(2).next_to(bias,LEFT,buff=0.4)
        self.play(FadeTransform(VGroup(elements,lines,weight_labels),wx))
        self.play(VGroup(wx,bias).animate.move_to(ORIGIN))
        self.wait(24)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        # Equation for hidden state
        equation1 = MathTex(r"\mathbf{h}_t = f(\mathbf{W}^{(hx)} \mathbf{x}_t + \mathbf{W}^{(hh)} \mathbf{h}_{t-1} + \mathbf{b})").scale(1.25).shift(UP*0.5)
        self.play(Write(equation1))
        self.wait(41)
        equation2 = MathTex(r"\hat{y} = \mathbf{W}^{(S)} \mathbf{h}_t").scale(1.25).shift(DOWN*0.5)
        self.play(Write(equation2))
        self.wait(8)

        
class Example(Scene):
    def construct(self):
        img = ImageMobject("/Users/vishypullela/Desktop/Summer_Reasearch_UMD/Manim_Activity/media/images/taco-bell-crunchwrap-feature.jpg", scale_to_resolution= 1000)
        review = Text("The food is not bad, could be better")
        self.wait(6)
        self.add(img)
        self.wait(14)
        self.clear()
        self.play(Write(review))
        Tokenized = Text("Tokenized Version",font_size=40).shift(UP*3)
        self.wait(4)
        self.play(FadeTransform(review, Tokenized))
        word1 = Text("The",font_size=32,color= BLUE)
        word2 = Text("food",font_size=32,color= BLUE)
        word3 = Text("is",font_size=32,color= BLUE)
        word4 = Text("not",font_size=32,color= BLUE)
        word5 = Text(" bad",font_size=32,color= BLUE)
        word6 = Text("could",font_size=32,color= BLUE)
        word7 = Text("be",font_size=32,color= BLUE)
        word8 = Text("better",font_size=32,color= BLUE)
        self.add(Group(word1,word2,word3,word4,word5).arrange(DOWN,buff =0.8).shift(LEFT*2))
        self.add(Group(word6,word7,word8).arrange(DOWN,buff =0.8).shift(RIGHT*2))
        self.wait(10)
        m0 = Matrix([[0],[0],[0]]).set_row_colors(GREEN,RED,GREY).shift(UP*2+LEFT*3)
        m01 = Matrix([[0],[0],[0]]).set_row_colors(GREEN,RED,GREY).shift(UP*2+LEFT*1)
        m02 = Matrix([[0],[0],[0]]).set_row_colors(GREEN,RED,GREY).shift(UP*2+RIGHT*1)
        m03 = Matrix([[0],[0],[1]]).set_row_colors(GREEN,RED,GREY).shift(UP*2+RIGHT*3)
        m04 = Matrix([[0],[1],[0]]).set_row_colors(GREEN,RED,GREY).shift(DOWN*2+LEFT*3)
        m05 = Matrix([[0],[0],[0]]).set_row_colors(GREEN,RED,GREY).shift(DOWN*2+LEFT*1)
        m06 = Matrix([[0],[0],[0]]).set_row_colors(GREEN,RED,GREY).shift(DOWN*2+RIGHT*1)
        m07 = Matrix([[1],[0],[0]]).set_row_colors(GREEN,RED,GREY).shift(DOWN*2+RIGHT*3)
        self.clear()
        self.play(FadeTransform(word1,m0))
        self.play(FadeTransform(word2,m01))
        self.play(FadeTransform(word3,m02))
        self.play(FadeTransform(word4,m03))
        self.play(FadeTransform(word5,m04))
        self.play(FadeTransform(word6,m05))
        self.play(FadeTransform(word7,m06))
        self.play(FadeTransform(word8,m07))
        self.wait(15)
        self.remove(m01)
        self.remove(m02)
        self.remove(m03)
        self.remove(m04)
        self.remove(m05)
        self.remove(m06)
        self.remove(m07)
        self.play(m0.animate.shift(DOWN*2))
        self.wait(5)
        whx = Matrix([["..."],["..."],["..."]])
        self.play(Write(whx))
        self.wait(3)
        #YO Andres can you fix the equation bellow so (hx)is superscriptedand the (hh) is subscripted
        whx1 = MathTex("f(x_1 \cdot W^{hx} + b_1)")
        htmin1 = MathTex("h_1").shift(LEFT*5)
        self.remove(m0)
        self.play(FadeTransform(whx, whx1))
        self.wait(20)
        whx2 = MathTex("f(x_2 \cdot W^{hx}+ b_1)")
        rrninitalweights = MathTex(" \cdot  w^{hh}").shift(LEFT*4.1)
        #t=2
        self.play(FadeTransform(whx1,htmin1))
        self.wait(18)
    
        self.play(m0.animate.shift(RIGHT*2))
        self.play(whx.animate.shift(RIGHT*1))
        self.wait(10)
        self.remove(m0)
        self.play(Write(rrninitalweights))
        self.remove(whx)
        self.remove(rrninitalweights)
        totalequal = MathTex("h_2 = f(h_1 \cdot w^{hh} + x_2 \cdot W^{hx} + b_2)")
        self.play(FadeTransform(htmin1,totalequal))
        self.wait(22)
        h4 = MathTex("\hat{y} = h_8 * W^s")
        self.play(FadeTransform(totalequal,h4))
        self.wait(14)
        self.clear()
        selfattention = Text("Self Attention",gradient = (BLUE, GREEN))
        self.play(Write(selfattention))
        self.wait(5)
        
        
     
        
        