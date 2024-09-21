from manim import *

class 401_IntrotoSLSAIntuition(Scene):
    def construct(self):
        Title = Text("Single Layer Self Attention", font_size= 48,gradient = (GRAY,BLUE))
        subtitle = Text("SLSA", font_size = 24,gradient = (GRAY,BLUE)).next_to(Title,DOWN*1)
        
        self.play(Write(Title))
        self.play(Write(subtitle))
        self.wait(5)
        
        polysemous = Text("Polysemous",font_size =48, color = GRAY)
        multiple_meanings = Text("Words with Multiple meanings", font_size = 24, color = GRAY).next_to(polysemous,DOWN*1)
        
        self.play(FadeTransform(Title, polysemous))
        self.play(FadeTransform(subtitle, multiple_meanings))
        self.wait(5)

        bank = Text("Bank",color = GRAY)
        dollar = Text("$ ",font_size= 50,color = GREEN).to_edge(RIGHT)
        River = Text("River Bank ", color = BLUE).to_edge(LEFT)
        arrowtoriver = Arrow(bank.get_left(), River.get_right())
        arrowtodollar =Arrow(bank.get_left(), dollar.get_left(),buff =2)
        
        self.play(FadeTransform(polysemous, bank))
        self.play(FadeTransform(multiple_meanings, dollar))
        self.play(Write(River))
        self.play(GrowArrow(arrowtoriver))
        self.play(GrowArrow(arrowtodollar))
        self.wait(5)
        
        
        contextscentence = Text("I borrowed money from the bank")
        
        self.remove(arrowtoriver)
        self.remove(arrowtodollar)
        self.play(FadeTransform(bank,contextscentence))
        self.remove(River)
        self.play(dollar.animate.shift(UP*3 +LEFT*7))
        self.wait(5)
        
        attention = Text("Attention Scores", font_size = 48,gradient = (GRAY,BLUE)).to_edge(UP)
        relavence = Text("Based on each words relavance to other words", font_size = 24, gradient = (GRAY,BLUE))
        
        self.play(FadeTransform(dollar, attention))
        self.play(FadeTransform(contextscentence, relavence))
        self.wait(5)
        self.clear()
        
        deeper_nuances = Text("Self attention allows deeper nuances",gradient = (GRAY,BLUE))
        
        self.play(Write(deeper_nuances))
        self.wait(5)
        
class 402_Sselfattentionscore(Scene):
    def construct(self):
        attentionfactors = Text("Query(Q)   Key(K)  Value(V)", font_size = 44)
        
        self.play(Write(attentionfactors))
        self.wait(5)
        
        
        # Create equation and matrices
        formula = MathTex(r"\text{Attention}(Q, K, V) = \text{softmax} \left( \frac{QK^T}{\sqrt{d_k}} \right) V")
        self.play(FadeTransform(attentionfactors,formula))
        self.wait(5)
        self.clear()
        
        number_line = NumberLine(x_range=[-5, 5, 1], length=10, include_numbers=True, font_size=24)
        number_line_label = Text("Input Values", font_size=32).next_to(number_line, DOWN)
        self.play(Create(number_line), Write(number_line_label))
        self.wait()

        # Define example input values and calculate softmax
        input_values = np.array([-2, -1, 0, 1, 2])
        softmax_values = np.exp(input_values) / np.sum(np.exp(input_values))

        # Create bars to represent input values and their corresponding softmax outputs
        input_bars = VGroup(*[Rectangle(width=0.8, height=value, color=BLUE) for value in input_values])
        softmax_bars = VGroup(*[Rectangle(width=0.8, height=value, color=GREEN) for value in softmax_values])

        input_bars.arrange(RIGHT, buff=0.2).move_to(number_line.number_to_point(0))
        softmax_bars.arrange(RIGHT, buff=0.2).move_to(number_line.number_to_point(0))
        softmax_bars.shift(DOWN * 2)

        # Labels for the bars
        input_labels = VGroup(*[
            DecimalNumber(num, num_decimal_places=2).scale(0.6).next_to(bar, UP) 
            for num, bar in zip(input_values, input_bars)
        ])
        softmax_labels = VGroup(*[
            DecimalNumber(num, num_decimal_places=2).scale(0.6).next_to(bar, DOWN) 
            for num, bar in zip(softmax_values, softmax_bars)
        ])

        # Show the bars
        self.play(
            AnimationGroup(
                *[FadeIn(bar) for bar in input_bars],
                *[Write(label) for label in input_labels],
                lag_ratio=0.2
            )
        )
        self.wait()

        # Animate the softmax transformation
        self.play(
            AnimationGroup(
                *[Transform(input_bars[i], softmax_bars[i]) for i in range(len(input_values))],
                *[Write(label) for label in softmax_labels],
                lag_ratio=0.2
            )
        )
        self.wait()

        # Add axis labels
        softmax_axis_label = Text("Softmax Output (Probability)", font_size=24).next_to(softmax_bars, DOWN, buff=0.5)
        self.play(Write(softmax_axis_label))

        self.wait(2) 
        self.clear()
        
        definition = Text("Query: a question or request for information.", font_size=32)
        self.play(Write(definition))
        self.wait(1)

        # Transition to self-attention context
        self.play(definition.animate.to_edge(UP))
        self.wait(2)

        
        # Question in a thought bubble
        question = Text("Are there any adjectives in front of me?").scale(0.7)
        self.play(Write(question))
        self.wait(5)
        self.clear()
        
        vector = Text("[...]").to_edge(RIGHT*9)
        
        self.play(FadeTransform(definition, vector))
        self.wait(1)
        
        token = Text("Token Encoding").to_edge(LEFT*5)
        tokenmatrix = Matrix([[25],[36],[91],[36],[17],[11],[54]]).set_row_colors(BLUE,WHITE,GREY,BLUE,WHITE,GREY,BLUE).next_to(vector,LEFT*3)
        Wq = MathTex(r"W_Q ").next_to(tokenmatrix,LEFT *3)
        equal = Text("=").next_to(tokenmatrix,RIGHT*1)
        timers = Text("*").next_to(tokenmatrix,LEFT*1)
        
        self.play(Write(token))
        self.wait(1)
        self.play(FadeTransform(token,tokenmatrix))
        self.play(Write(Wq))
        self.play(Write(equal))
        self.play(Write(timers))
        self.wait(5)
        
        tokenmatrix1 = Matrix([[65],[53],[76],[34],[92],[56],[19]]).set_row_colors(BLUE,WHITE,GREY,BLUE,WHITE,GREY,BLUE).next_to(vector,LEFT*3)
        tokenmatrix2 = Matrix([[35],[63],[98],[24],[11],[62],[97]]).set_row_colors(BLUE,WHITE,GREY,BLUE,WHITE,GREY,BLUE).next_to(vector,LEFT*3)
        tokenmatrix3 = Matrix([[65],[43],[58],[86],[99],[26],[18]]).set_row_colors(BLUE,WHITE,GREY,BLUE,WHITE,GREY,BLUE).next_to(vector,LEFT*3)
        tokenmatrix4 = Matrix([[29],[98],[28],[30],[61],[39],[37]]).set_row_colors(BLUE,WHITE,GREY,BLUE,WHITE,GREY,BLUE).next_to(vector,LEFT*3)
        tokenmatrix5 = Matrix([[21],[93],[78],[26],[27],[66],[22]]).set_row_colors(BLUE,WHITE,GREY,BLUE,WHITE,GREY,BLUE).next_to(vector,LEFT*3)
        
        question = Text("Are there any adjectives in front of me?").to_edge(UP)
        self.play(Write(question))
        self.play(FadeTransform(tokenmatrix,tokenmatrix1))
        self.wait(0.5)
        self.play(FadeTransform(tokenmatrix1,tokenmatrix2))
        self.wait(0.5)
        self.play(FadeTransform(tokenmatrix2,tokenmatrix3))
        self.wait(0.5)
        self.play(FadeTransform(tokenmatrix3,tokenmatrix4))
        self.wait(0.5)
        self.play(FadeTransform(tokenmatrix4,tokenmatrix5))
        self.wait(5)



class 403_Example1(Scene):
    def construct(self):
        example = Text("The large river bank").to_edge(UP)

        self.play(Write(example))
        self.wait(2)
        
        tokenmatrix1 = Matrix([[65],[53],[76],[34],["..."],[56],[19]]).set_row_colors(BLUE,WHITE,GREY,BLUE,WHITE,GREY,BLUE).next_to(example[0],DOWN*2)
        tokenmatrix2 = Matrix([[35],[63],[98],[24],["..."],[62],[97]]).set_row_colors(BLUE,WHITE,GREY,BLUE,WHITE,GREY,BLUE).next_to(example[5],DOWN*2)
        tokenmatrix3 = Matrix([[65],[43],[58],[86],["..."],[26],[18]]).set_row_colors(BLUE,WHITE,GREY,BLUE,WHITE,GREY,BLUE).next_to(example[10],DOWN*2)
        tokenmatrix4 = Matrix([[29],[98],[28],[30],["..."],[39],[37]]).set_row_colors(BLUE,WHITE,GREY,BLUE,WHITE,GREY,BLUE).next_to(example[15],DOWN*2)
        
        self.play(Create(tokenmatrix1))
        self.play(Create(tokenmatrix2))
        self.play(Create(tokenmatrix3))
        self.play(Create(tokenmatrix4))
        self.wait(5)
        
        errow1 = MathTex(r"\vec{E}_1",color=BLUE).next_to(example[1],DOWN*2)
        errow2 = MathTex(r"\vec{E}_2",color=BLUE).next_to(example[5],DOWN*2)
        errow3 = MathTex(r"\vec{E}_3",color=BLUE).next_to(example[10],DOWN*2)
        errow4 = MathTex(r"\vec{E}_4",color=BLUE).next_to(example[14],DOWN*2)
        
        self.play(FadeTransform(tokenmatrix1,errow1))
        self.play(FadeTransform(tokenmatrix2,errow2))
        self.play(FadeTransform(tokenmatrix3,errow3))
        self.play(FadeTransform(tokenmatrix4,errow4))
        self.wait(5)
        
        Wq = MathTex(r"W_Q ",color=YELLOW).shift(LEFT*1)
        Query = Text(" = Query Vector",font_size = 32).next_to(Wq,RIGHT*4)
        Qroow = MathTex(r"= \vec{W}_1",color=YELLOW).next_to(Wq,RIGHT*4.5)
        Qr1 = MathTex(r"\vec{W}_1",color=YELLOW).next_to(example[1], DOWN*8)
    
        self.play(Write(Wq))
        self.play(errow1.animate.next_to(Wq, RIGHT*1))
        self.play(Write(Query))
        self.wait(1)
        self.play(FadeTransform(Query,Qroow))
        self.wait(5)
        self.play(errow1.animate.next_to(example[1],DOWN*2))
        self.play(Qroow.animate.next_to(example[1], DOWN*7))
        self.play(Wq.animate.next_to(example[1], DOWN*5+LEFT*1))
        self.play(FadeTransform(Qroow,Qr1))
        self.wait(5)
        
        arrowtoQr1= Arrow(errow1.get_left(), Qr1.get_left(),buff=0.4)
        question = Text("Are there any adjectives in front of me?",font_size=32).next_to(Qr1,RIGHT*2)
        arrowtoQuestion = Arrow(Qr1.get_right(), question.get_left(),buff=0.4)
        self.play(GrowArrow(arrowtoQr1))
        self.play(Write(question))
        self.play(GrowArrow(arrowtoQuestion))
        self.wait(5)
        
       
        The = Text("The").shift(UP*3+LEFT*2)
        
        self.remove(arrowtoQuestion)
        self.remove(question)
        self.remove(errow2)
        self.remove(errow3)
        self.remove(errow4)
        self.remove(arrowtoQr1)
        self.wait(1)
        self.play(FadeTransform(example,The))
        self.play(errow1.animate.next_to(The,DOWN*2))
        self.play(Qr1.animate.next_to(The, DOWN*7))
        self.play(Wq.animate.next_to(The, DOWN*5+LEFT*1))
        
        rwoq = Arrow(errow1.get_left(), Qr1.get_left(),buff=0.4)
        
        self.play(GrowArrow(rwoq))
        self.wait(5)
        
        The1 = Text("The").shift(UP*3+RIGHT*2)
        errow12 = MathTex(r"\vec{E}_1",color=BLUE).next_to(The1,DOWN*2)
        Wk= MathTex(r"W_K ",color= GREEN).next_to(The1,DOWN*5+LEFT*1)
        Kr1 = MathTex(r"\vec{K}_1",color=GREEN).next_to(The1, DOWN*7)
        kwoq = Arrow(errow12.get_left(), Kr1.get_left(),buff=0.4)
        
        self.play(Write(The1))
        self.play(Write(errow12))
        self.play(Write(Wk))
        self.play(Write(Kr1))
        self.play(Write(kwoq))
        self.wait(5)
        
        approx_eq = Text("≈")
        arrowfwteq = Arrow(Qr1.get_right(), approx_eq.get_left(),buff=0.4)
        arrowfkteq = Arrow(Kr1.get_left(), approx_eq.get_right(),buff=0.4)
        
        self.play(Write(approx_eq))
        self.play(GrowArrow(arrowfwteq))
        self.play(GrowArrow(arrowfkteq))
        self.wait(5)

class 404_ValueMatrixAttention(Scene):
    def construct(self):

        formula = MathTex(r"\text{Attention}(Q, K, V) = \text{softmax} \left( \frac{QK^T}{\sqrt{d_k}} \right) V")
        num=MathTex(r"{QK^T}")
        denom= MathTex(r"{\sqrt{d_k}")
      
        self.play(Write(formula))
        self.wait(5)
        self.play(FadeTransform(formula,num))
        self.wait(5)
        self.play(FadeTransform(num,denom))
        self.wait(5)
        self.clear()
        # Set up word embeddings
        river_embedding = Arrow(LEFT*10, LEFT*1, color=BLUE, buff=2)  
        large_value_vector = Arrow(ORIGIN, UP * 3, color=GREEN, buff=0)

        # Display word embeddings
        river_label = Text("River").next_to(river_embedding, DOWN)
        value_label = MathTex("W_v").next_to(large_value_vector, LEFT)

        self.play(Create(river_embedding), Write(river_label))
        self.wait()

        # Show value matrix multiplication
        value_matrix = Matrix([[0.8, 0.2], [0.3, 0.7]]).next_to(ORIGIN, LEFT*1)
        value_matrix_label = Text("Value Matrix").next_to(value_matrix, UP)
        
        
        self.play(Create(value_matrix), Write(value_matrix_label))
        self.wait()
        
        # Calculate the resulting value vector from matrix multiplication
        result_value_vector = Arrow(value_matrix.get_right(), value_matrix.get_right() + RIGHT * 3 + UP * 2.5, color=YELLOW, buff=1)
        res_label = Text("Value Vector",font_size=24).next_to(result_value_vector, DOWN)
        self.play(Write( result_value_vector), Write( res_label))
        self.remove(value_matrix)
        self.remove(value_label)
        self.remove(value_matrix_label)
        self.wait()

        # Show addition of value vector to river embedding
        combined_embedding = Arrow(ORIGIN, RIGHT * 3 + UP * 2.5, color=PURPLE, buff=1)
        combined_label = Text("Large River").next_to(combined_embedding, RIGHT)
        self.play(Transform(river_embedding, combined_embedding), Transform(river_label, combined_label))
        self.wait(10)
        self.clear()
      
        
        SLSA = Text("SLSA",gradient=(GRAY,BLUE)).to_edge(UP)
        handly = Text("Polysemous Words", font_size=24).next_to(SLSA,DOWN*2)
        context = Text("Understands richer context", font_size = 24).next_to(handly,DOWN*2)                                                               
      
        self.play(Write(SLSA))
        self.play(Write(handly))
        self.play(Write(context))
        self.wait(10)
      

        
      




        
        
        
        

 

       



        
    
