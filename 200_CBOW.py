from manim import *

def label_vector(vector, a, b, c=None, d=None, e=None, f=None, g=None,top_label=None, buff=0.5):
    labels = VGroup()
    labels.add(Text(str(a),font_size=20).next_to(vector.get_rows()[0], LEFT, buff=buff))
    labels.add(Text(str(b),font_size=20).next_to(vector.get_rows()[1], LEFT, buff=buff))
    if c is not None:
        labels.add(Text(str(c),font_size=20).next_to(vector.get_rows()[2], LEFT, buff=buff))
    if d is not None:
        labels.add(Text(str(d),font_size=20).next_to(vector.get_rows()[3], LEFT, buff=buff))
    if e is not None:
        labels.add(Text(str(e),font_size=20).next_to(vector.get_rows()[4], LEFT, buff=buff))
    if f is not None:
        labels.add(Text(str(f),font_size=20).next_to(vector.get_rows()[5], LEFT, buff=buff))
    if g is not None:
        labels.add(Text(str(g),font_size=20).next_to(vector.get_rows()[6], LEFT, buff=buff))
    if top_label is not None:
        labels.add(Text(str(top_label),font_size=20).next_to(vector.get_columns()[0], UP, buff=0.5))
    return labels

class CBoW(Scene):
    def construct(self):
        # Write sentence with arrow to computer
        sentence = Text("Sentence").shift(LEFT*3).scale(0.75)
        computer = ImageMobject("source_images/computer.png").shift(RIGHT*3).scale(0.2)
        sentence_to_computer = Arrow(start=sentence.get_right(),end=computer.get_left(),color=PURPLE)
        self.wait(6.57)
        self.play(Write(sentence),GrowArrow(sentence_to_computer),FadeIn(computer))
        self.wait(1.25)

        # Write word2vec and transform the arrow
        algo = Text("Word2vec").scale(0.75)
        self.play(FadeOut(sentence_to_computer),sentence.animate.shift(LEFT*2.5),computer.animate.shift(RIGHT*2.5))
        sentence_to_algo_to_computer = VGroup(Arrow(start=sentence.get_right(),end=algo.get_left(),color=PURPLE),Arrow(start=algo.get_right(),end=computer.get_left(),color=PURPLE))
        self.play(Write(algo),Write(sentence_to_algo_to_computer))
        self.wait(8)

        # Write token and transform the arrow again
        token = Text("Token").shift(LEFT*1.875).scale(0.75)
        self.play(FadeOut(sentence_to_algo_to_computer),algo.animate.shift(RIGHT*1.875))
        connecting_arrows = VGroup(Arrow(start=sentence.get_right(),end=token.get_left(),color=PURPLE),Arrow(start=token.get_right(),end=algo.get_left(),color=PURPLE),Arrow(start=algo.get_right(),end=computer.get_left(),color=PURPLE))
        self.play(Write(token),Write(connecting_arrows))
        self.wait(1.14)

        # Make computer into vector
        vector_1_raw = Matrix([[0.12],[1.41],[2.12],[9.83],[0.57],[5.05],[0.92]],bracket_h_buff=0.1)
        vector_1_labels = label_vector(vector_1_raw,1,2,3,4,"...",224,225)
        vector_1 = VGroup(vector_1_raw,vector_1_labels).move_to(computer.get_center())
        self.play(FadeTransform(computer,vector_1))
        self.wait(1.14)

        # Token definition
        words = Text("backpack",color=YELLOW).scale(0.6).next_to(token,UP,buff=2)
        words_line = Line(start=token.get_top(),end=words.get_bottom(),color=YELLOW)
        token_1 = VGroup(words,words_line)
        subwords = Text("back, pack",color=ORANGE).scale(0.6).next_to(sentence.get_right(),UP,buff=1.25)
        subwords_line = Line(start=token.get_top(),end=subwords.get_bottom(),color=ORANGE)
        token_2 = VGroup(subwords,subwords_line)
        characters = Text("b,a,c,k,p,a,c,k",color=BLUE).scale(0.6).next_to(algo.get_left(),UP,buff=1.25)
        characters_line = Line(start=token.get_top(),end=characters.get_bottom(),color=BLUE)
        token_3 = VGroup(characters,characters_line)
        self.wait(4.29)
        self.play(Write(token_1))
        self.wait(0.5)
        self.play(Write(token_2))
        self.wait(0.5)
        self.play(Write(token_3))
        self.wait(1.5)
        self.play(FadeOut(token_2,token_3))

        # Write similar man and woman vectors
        vector_2_raw = Matrix([[0.15],[1.44],[2.16],[9.89],[0.65],[5.11],[0.48]],bracket_h_buff=0.1)
        vector_2_labels = label_vector(vector_2_raw,1,2,3,4,"...",224,225,"man")
        vector_2 = VGroup(vector_2_raw,vector_2_labels).shift(LEFT*2)
        self.wait(15.3)
        vector_1.add(Text("woman",font_size=20).next_to(vector_1_raw.get_columns()[0],UP,buff=0.5))
        self.play(FadeOut(sentence,token_1,token,connecting_arrows,algo),vector_1.animate.shift(LEFT*3),Write(vector_2))
        self.wait(10.86)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        # CBoW title with example sentence
        continuous_bag_of_words = Text("Continuous Bag of Words",font_size=50).to_edge(UP)
        self.play(Write(continuous_bag_of_words))
        CBoW = Text("CBoW",font_size=50).move_to(continuous_bag_of_words.get_center())
        self.wait(0.5)
        self.play(FadeTransform(continuous_bag_of_words,CBoW))
        sentence = VGroup(
            Text("this"),
            Text("is"),
            Text("the"),
            Text("target").set_color(RED),
            Text("word")
        ).arrange(RIGHT, buff=1.5).next_to(CBoW,DOWN, buff=0.5)
        self.wait(2)
        self.play(Write(sentence))

        # Average representations quick example
        vector_data = [
            ([3.25, 7.81, 1.56, 9.34, 4.72, 0.93, 6.18], [1, 2, 3, 4, "...", 224, 225]),
            ([5.47, 2.09, 8.63, 0.41, 7.95, 3.72, 1.84], [1, 2, 3, 4, "...", 224, 225]),
            ([9.12, 4.56, 2.78, 6.31, 0.89, 5.23, 7.67], [1, 2, 3, 4, "...", 224, 225]),
            ([1.35, 8.74, 3.96, 6.52, 0.27, 9.81, 4.19], [1, 2, 3, 4, "...", 224, 225]),
            ([7.03, 2.46, 9.58, 5.71, 1.92, 8.37, 0.64], [1, 2, 3, 4, "...", 224, 225])
        ]
        vectors = VGroup()
        labels = VGroup()
        for i, (word, (vec_values, vec_labels)) in enumerate(zip(sentence, vector_data)):
            vector = Matrix([[v] for v in vec_values],bracket_h_buff=0.1).scale(0.6).next_to(word, DOWN, buff=0.5)
            vectors.add(vector)
            label = label_vector(vector, *vec_labels, buff=0.35)
            labels.add(label)
        context_vectors = VGroup(vectors[0],labels[0],vectors[1],labels[1],vectors[2],labels[2],vectors[4],labels[4])
        self.play(Write(context_vectors))
        self.wait(1)
        self.play(FadeTransform(context_vectors,VGroup(vectors[3],labels[3])))
        self.wait(4)
        self.play(FadeOut(vectors[3],labels[3]))

        # Simplification into two-dimensional vectors
        vector_data = [
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 1],
            [0, 0]
        ]

        vectors = VGroup()
        for word, vec_values in zip(sentence, vector_data):
            vector = Matrix([[v] for v in vec_values], bracket_h_buff=0.1).scale(0.6).next_to(word, DOWN, buff=0.5)
            vectors.add(vector)

        self.play(Write(vectors))
        self.wait(5)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        # Intro to example sentence and "I" calculation
        example_sentence = VGroup(
            Text("I",font_size=27).set_color(RED),
            Text("got",font_size=27),
            Text("a",font_size=27),
            Text("fine",font_size=27),
            Text("for",font_size=27),
            Text("parking",font_size=27),
            Text("violations",font_size=27),
        ).arrange(RIGHT, buff=1).to_edge(UP)
        self.play(Write(example_sentence))
        vector_data = [
            [[0.83, 1.5], [0, 0], [0, 0], [5, 0], [0, 0], [0, 0], [0, 9]],
            [[0.83, 1.5], [0.83, 1.5], [0, 0], [5, 0], [0, 0], [0, 0], [0, 9]],
            [[0.83, 1.5], [0.83, 1.5], [0.83, 1.5], [5, 0], [0, 0], [0, 0], [0, 9]],
            [[0.83, 1.5], [0.83, 1.5], [0.83, 1.5], [0, 1.5], [0, 0], [0, 0], [0, 9]],
            [[0.83, 1.5], [0.83, 1.5], [0.83, 1.5], [0, 1.5], [0.83, 1.5], [0, 0], [0, 9]],
            [[0.83, 1.5], [0.83, 1.5], [0.83, 1.5], [0, 1.5], [0.83, 1.5], [0.83, 1.5], [0, 9]],
            [[0.83, 1.5], [0.83, 1.5], [0.83, 1.5], [0, 1.5], [0.83, 1.5], [0.83, 1.5], [0.83, 0]]
        ]

        vectors = VGroup()
        for word, vec_values in zip(example_sentence, vector_data[0]):
            vector = Matrix([[v] for v in vec_values], bracket_h_buff=0.1).scale(0.6).next_to(word, DOWN, buff=0.5)
            vectors.add(vector)

        self.wait(1)
        self.play(Write(vectors[1:]))
        self.wait(12)
        self.play(FadeTransform(vectors[1:],vectors[0]))
        self.wait(1)

        # Representations for the rest of the sentence
        for i in range(6):
            self.play(example_sentence[i].animate.set_color(WHITE),example_sentence[i+1].animate.set_color(RED),run_time=0.5)
            vectors = VGroup()
            for word, vec_values in zip(example_sentence, vector_data[i+1]):
                vector = Matrix([[v] for v in vec_values], bracket_h_buff=0.1).scale(0.6).next_to(word, DOWN, buff=0.5)
                vectors.add(vector)

            self.play(Write(vectors[(i+2):]),run_time=0.5)
            animations = []
            for j in range(i+1):
                animations.append(FadeTransform(vectors[j], vectors[i+1]))
            for j in range(i+2, len(vectors)):
                animations.append(FadeTransform(vectors[j], vectors[i+1]))
            self.play(*animations,run_time=0.75)

        # Averaging them all to get a sentence vector
        avg_line = Line(start=example_sentence.get_left(),end=example_sentence.get_right()).next_to(example_sentence,DOWN,buff=2)
        sentence_vector = Matrix([[0.854],[1.285]]).next_to(avg_line,DOWN,buff=0.5)
        self.play(Write(avg_line),Write(sentence_vector))
        self.wait(14)

        # Subtract for the toy example and get the sentiment score
        subtraction = Text("-",font_size=100,color=RED).next_to(sentence_vector.get_rows()[1],LEFT,buff=0.6)
        score_line = Line(start=sentence_vector.get_left(),end=sentence_vector.get_right()).next_to(sentence_vector,DOWN,buff=0.25)
        score = Text("-0.431",color=RED).next_to(score_line,DOWN,buff=0.5).scale(0.8)
        self.play(Write(subtraction),Write(score_line),Write(score))
        self.wait(6.29)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        # Multiplication with weight matrix W that maps onto hidden layer
        dict_vector = Matrix([[4],[0]]).shift(LEFT*5)
        multiplication = MathTex(r"\times",font_size = 80).shift(LEFT*3)
        weight_matrix = Matrix([[7.39, 8.93], [1.23, 4.45], [3.22, 3.34], [0.43, 9.91], [1.36, 2.37], [5.79, 4.19], [6.41, 2.68] ])
        weight_matrix_label = Text("W").next_to(weight_matrix,UP)
        hidden_layer = Text("h",font_size=80).shift(RIGHT*5)
        weight_matrix_to_hidden_layer = Arrow(start=weight_matrix.get_right(),end=hidden_layer.get_left(),buff=0.25)
        self.play(Write(dict_vector))
        self.wait(4)
        self.play(Write(multiplication),Write(weight_matrix),Write(weight_matrix_label))
        self.wait(16)
        self.play(Write(weight_matrix_to_hidden_layer),Write(hidden_layer))
        self.wait(25.43)

        # Hidden layer equation
        equation = MathTex(r"\;", r"=", r"\frac{1}{C}", r"\sum_{w=1}^{C}", r"W", r"\cdot", r"v_w", font_size=80)
        colors = [WHITE, RED, BLUE, GREEN, PURPLE, ORANGE, YELLOW]
        for part, color in zip(equation, colors): part.set_color(color)
        equation.move_to(UP)
        rectangles, labels, lines = [], [], []
        label_texts = ["Space", "Equals", "Average", "Sum over each context word", "Weight matrix", "Dot Product", "Dictionary vector"]
        buffs = [0,0,0.5,2.75,1.5,2,2.5]
        for i, part in enumerate(equation):
            if i == 0 or i == 1 or i == 5: continue
            rect = SurroundingRectangle(part, buff=0.1, color=colors[i])
            label = Text(label_texts[i], font_size=24, color=colors[i]).next_to(rect, DOWN, buff=buffs[i])
            line = Line(rect.get_bottom(), label.get_top(), color=colors[i])
            rectangles.append(rect); labels.append(label); lines.append(line)
        self.play(FadeOut(dict_vector, multiplication, weight_matrix, weight_matrix_label, weight_matrix_to_hidden_layer),Write(equation),hidden_layer.animate.next_to(equation,LEFT))
        for rect, label, line in zip(rectangles, labels, lines):
            self.play(Write(rect), Write(line), Write(label), run_time=0.5)
        self.wait(14.57)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        # Bag of words with inverter limitation
        example_sentence[6].set_color(WHITE)
        self.play(Write(example_sentence))
        bag = ImageMobject("source_images/bag.png").scale(0.75).shift(DOWN*1)
        self.play(FadeIn(bag))
        for i in range(7):
            self.play(FadeOut(example_sentence[6-i],target_position=bag),run_time=0.3)
            self.wait(0.3)
        inverter_examples = VGroup(Text("not",color=RED),Text("good,",color=RED),Text("not",color=GREEN),Text("bad",color=GREEN)).arrange(RIGHT, buff=0.5).to_edge(UP)
        self.wait(6.76)
        self.play(Write(inverter_examples))
        self.wait(11)
        for i in range(4):
            self.play(FadeOut(inverter_examples[3-i],target_position=bag),run_time=0.3)
            self.wait(0.3)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        # Walkthrough of inverter limitation
        example_sentence = VGroup(
            Text("I",font_size=27),
            Text("am",font_size=27),
            Text("not",font_size=27),
            Text("feeling",font_size=27),
            Text("bad",font_size=27),
        ).arrange(RIGHT, buff=1).to_edge(UP)
        self.play(Write(example_sentence))
        vector_data = [
            [[0, 1.25], [0, 0], [0, 0], [0, 0], [0, 5]],
            [[0, 1.25], [0, 1.25], [0, 0], [0, 0], [0, 5]],
            [[0, 1.25], [0, 1.25], [0, 1.25], [0, 0], [0, 5]],
            [[0, 1.25], [0, 1.25], [0, 1.25], [0, 1.25], [0, 5]],
            [[0, 1.25], [0, 1.25], [0, 1.25], [0, 1.25], [0, 0]],
        ]

        self.wait(4)
        for i in range(5):
            self.play(example_sentence.animate.set_color(WHITE),example_sentence[i].animate.set_color(RED),run_time=0.5)
            vectors = VGroup()
            for word, vec_values in zip(example_sentence, vector_data[i]):
                vector = Matrix([[v] for v in vec_values], bracket_h_buff=0.1).scale(0.6).next_to(word, DOWN, buff=0.5)
                vectors.add(vector)

            self.play(Write(vectors[(i+1):]),run_time=0.5)
            animations = []
            for j in range(i):
                animations.append(FadeTransform(vectors[j], vectors[i]))
            for j in range(i+1, len(vectors)):
                animations.append(FadeTransform(vectors[j], vectors[i]))
            self.play(*animations,run_time=0.75)

        # Averaging them all to get a sentence vector
        avg_line = Line(start=example_sentence.get_left(),end=example_sentence.get_right()).next_to(example_sentence,DOWN,buff=2)
        sentence_vector = Matrix([[0], [1]]).next_to(avg_line,DOWN,buff=0.5)
        self.play(Write(avg_line),Write(sentence_vector))
        self.wait(4.29)

        # Subtract for the toy example and get the sentiment score
        subtraction = Text("-",font_size=100,color=RED).next_to(sentence_vector.get_rows()[1],LEFT,buff=0.6)
        score_line = Line(start=sentence_vector.get_left(),end=sentence_vector.get_right()).next_to(sentence_vector,DOWN,buff=0.25)
        score = Text("-1",color=RED).next_to(score_line,DOWN,buff=0.5).scale(0.8)
        self.play(Write(subtraction),Write(score_line),Write(score))
        self.wait(11.14)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

