from manim import *


class Dictionary1(Scene):
    def construct(self):
        Title = Text("Sentiment Analysis",font_size = 68,gradient=(RED,GREEN))
        Company = Text("Travel Company" , color=BLUE, font_size=48)
        Review = Text("Reviews" , color=BLUE, font_size=28).next_to(Company, DOWN * 4)
        self.play(Write(Title))
        self.wait(13.5)
        self.play(FadeOut(Title))
        self.clear()
        self.play(Write(Company))
        self.wait(3)
        plus_symbol = Text("+", font_size=120,color = GREEN).shift(4 * RIGHT)
        minus_symbol = Text("-", font_size=120, color = RED).shift(4 * LEFT)

        # Create arrows(FadeTransform(cat, bland))
        arrow_to_plus = Arrow(Review.get_right(), plus_symbol.get_left(), buff=0.8)
        arrow_to_minus = Arrow(Review.get_left(), minus_symbol.get_left(), buff=0.8)

        # Add everything to the scene
        self.play(Write(Review),
                  FadeIn(plus_symbol, shift=DOWN),
                  FadeIn(minus_symbol, shift=DOWN),
                  GrowArrow(arrow_to_plus),
                  GrowArrow(arrow_to_minus))

        self.wait(15)
        self.clear()
        
        
class Dictionary2(Scene):
    def construct(self):
        plus_symbol = Text("+", font_size=120,color = GREEN).shift(4 * RIGHT)
        minus_symbol = Text("-", font_size=120, color = RED).shift(4 * LEFT)
        String = Text('"String"')

        # Create arrows(FadeTransform(cat, bland))
        arrow_to_plus = Arrow(String.get_right(), plus_symbol.get_left(), buff=0.8)
        arrow_to_minus = Arrow(String.get_left(), minus_symbol.get_left(), buff=0.8)

        # Add everything to the scene
        self.play(Write(String),
                  FadeIn(plus_symbol, shift=DOWN),
                  FadeIn(minus_symbol, shift=DOWN),
                  GrowArrow(arrow_to_plus),
                  GrowArrow(arrow_to_minus))

        self.wait(6)
        self.remove(arrow_to_plus)
        self.remove(arrow_to_minus)
        Dictionary = MarkupText("Dictionary", font_size= 52, gradient=(RED,GREEN)).to_edge(UP)
        self.play(FadeTransform(String, Dictionary))
        self.play(plus_symbol.animate.shift(UP*2))
        self.play(minus_symbol.animate.shift(UP*2))
        self.wait(6)
        Positive_Word1 = Text("Great", color= GREEN)
        Positive_Word2 = Text("Good", color= GREEN)
        Positive_Word3 = Text("Like", color= GREEN)
        self.add(Group(Positive_Word1,Positive_Word2,Positive_Word3).arrange(DOWN,buff =0.8))
        self.play(Positive_Word1.animate.shift(RIGHT*4+DOWN*1))
        self.play(Positive_Word2.animate.shift(RIGHT*4+DOWN*1))
        self.play(Positive_Word3.animate.shift(RIGHT*4+DOWN*1))
        self.wait(6)

        Negitive_Word1 = Text("Hate", color= RED)
        Negitive_Word3 = Text("Dislike", color= RED)
        Negitive_Word2 = Text("Upset", color= RED)
        self.add(Group(Negitive_Word1,Negitive_Word2,Negitive_Word3).arrange(DOWN,buff =0.8))
        self.play(Negitive_Word1.animate.shift(LEFT*4+DOWN*1))
        self.play(Negitive_Word2.animate.shift(LEFT*4+DOWN*1))
        self.play(Negitive_Word3.animate.shift(LEFT*4+DOWN*1))
        self.wait(6)
        score_additiondescriptionNeg = MarkupText("Negitive  sentiment words with corresponding score",font_size= 20, color = GRAY).shift(UP*1.2+LEFT*4)
        self.play(Write(score_additiondescriptionNeg))
        score_additiondescriptionPos = MarkupText("Positive  sentiment words with corresponding score",font_size= 20, color = GRAY).shift(UP*1.2+RIGHT*4)
        self.play(Write(score_additiondescriptionPos))
        pos3 = Text("(+3)", font_size= 48, color = GREEN).next_to(Positive_Word1, RIGHT*1)
        pos2 = Text("(+2)",font_size= 48, color = GREEN).next_to(Positive_Word2, RIGHT*1)
        pos1 = Text("(+1)",font_size= 48, color= GREEN).next_to(Positive_Word3, RIGHT*1)
        Neg3 = Text("(-3)",font_size= 48, color = RED).next_to(Negitive_Word1, RIGHT*1)
        Neg2 = Text("(-2)",font_size= 48, color = RED).next_to(Negitive_Word2, RIGHT*1)
        Neg1 = Text("(-1)",font_size= 48, color= RED).next_to(Negitive_Word3, RIGHT*1)
        self.play(Write(Neg3))
        self.play(Write(Neg1))
        self.play(Write(Neg2))
        self.play(Write(pos3))
        self.play(Write(pos2))
        self.play(Write(pos1))
        self.wait(7.5)
        self.clear()
        example_text = Text("I dislike this product, but I like this company.")
        example_text[1:2].set_color(RED)
        example_text[1:3].set_color(RED)
        example_text[1:4].set_color(RED)
        example_text[1:5].set_color(RED)
        example_text[1:6].set_color(RED)
        example_text[1:7].set_color(RED)
        example_text[1:8].set_color(RED)
        example_text[24:28].set_color(GREEN)
        self.play(Write(example_text))
        self.wait(15)
        Neg11 = Text("(-1)",font_size= 48, color= RED).shift(DOWN*2+LEFT*1)
        pos11 = Text("(+1)",font_size= 48, color= GREEN).shift(DOWN*2+ RIGHT*1)
        self.play(FadeTransform(example_text[1:8],Neg11))
        self.play(FadeTransform(example_text[24:28],pos11))
        equal = Text("=").shift(DOWN*2+ RIGHT * 2)
        plus = Text("+").shift(DOWN*2)
        zero = Text("0").shift(DOWN*2 + RIGHT *2.6)
        self.play(Write(equal))
        self.play(Write(plus))
        self.play(Write(zero))
        nuetral = Text("Nuetral Sentiment",font_size= 34, color = GREY).shift(DOWN*2+RIGHT*4.3)
        self.play(FadeTransform(zero,nuetral))
        self.wait(22.5)
        self.clear()
        sarcasm = Text("Great! my car broke down again", gradient=(GREEN,RED))
        self.play(Write(sarcasm))
        self.wait(15)
        self.clear()