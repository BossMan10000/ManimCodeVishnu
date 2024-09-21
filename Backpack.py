from manim import *
import random

class Backpack_Model(Scene):
    def construct(self):
        # Reference back to CBoW
        CBoW = Text("CBoW", font_size=50).to_edge(UP)
        self.play(Write(CBoW))
        sentence = VGroup(
            Text("this"),
            Text("is"),
            Text("the"),
            Text("target").set_color(RED),
            Text("word")
        ).arrange(RIGHT, buff=1.5).next_to(CBoW, DOWN, buff=0.5)
        self.play(Write(sentence))
        vector_data = [[0, 1],[2, 0],[6, 0],[4, 1],[0, 3]]
        vectors = VGroup()
        for word, vec_values in zip(sentence, vector_data):
            vector = Matrix([[v] for v in vec_values]).scale(0.6).next_to(word, DOWN, buff=0.5)
            vectors.add(vector)
        context_vectors = VGroup(vectors[0], vectors[1], vectors[2], vectors[4])
        self.play(Write(context_vectors))
        self.wait(1)
        self.play(FadeTransform(context_vectors, VGroup(vectors[3])))
        self.wait(7.86)
        self.play(FadeOut(vectors[3]))

        # Adaptation for backpacks
        sense_vector_data = [[[2, 0], [7, 0], [0, 1]],[[5, 0], [0, 2], [0, 4]],[[0, 9], [0, 5], [1, 0]],[[9.21,12.14]],[[3, 0], [0, 4], [4, 0]]]
        context_weights = [[0.35, 0.57, 0.46],[0.29, 0.77, 0.62],[0.41, 0.53, 0.68],[None],[0.21, 0.33, 0.44]]
        sense_vectors = VGroup()
        weights = VGroup()
        for i, word in enumerate(sentence):
            vec_group = sense_vector_data[i]
            if i == 3:
                continue
            for j, vec_values in enumerate(vec_group):
                vector = Matrix([[v] for v in vec_values]).scale(0.6)
                if j == 0:
                    vector.next_to(word, DOWN, buff=0.5)
                else:
                    vector.next_to(sense_vectors[-1], DOWN, buff=0.5)
                sense_vectors.add(vector)
                weight = MathTex(r"\times" + str(context_weights[i][j]),color=RED).scale(0.6).next_to(vector,RIGHT,buff=0.1)
                weights.add(weight)
        self.play(Write(sense_vectors))
        self.wait(3)
        self.play(Write(weights))
        self.wait(5)
        weighted_sum_vector = Matrix([[9.21],[12.1]]).scale(0.6).next_to(sentence[3],DOWN,buff=0.5)
        self.play(FadeTransform(VGroup(sense_vectors,weights),weighted_sum_vector))
        self.wait(4.14)
        self.play(FadeOut(weighted_sum_vector))

        # Comparison of CBoW vs backpack model
        dummy_weights = VGroup()
        for vec in context_vectors:
            dummy_weights.add(MathTex(r"\times 1",color=RED).scale(0.6).next_to(vec,RIGHT,buff=0.1))
        self.play(Write(context_vectors))
        self.play(Write(dummy_weights))
        self.wait(4.86)
        self.play(FadeTransform(VGroup(context_vectors,dummy_weights),VGroup(sense_vectors,weights)),run_time=3.86)
        self.wait(11)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        # Sense vector intuition
        nurse = Text("Nurse",color=BLUE).to_edge(UP,buff=1)
        nurse_senses = VGroup(VGroup(Matrix([[4],[0]]),Text('= "to nurse, nurses, nursing"')).scale(0.6).arrange(RIGHT,buff=0.25).next_to(nurse,DOWN,buff=0.75),VGroup(Matrix([[0],[0]]),Text('= "nurse, profession, job, care"')).scale(0.6).arrange(RIGHT,buff=0.25),VGroup(Matrix([[0],[0]]),Text('= "female, woman, she, her"')).scale(0.6).arrange(RIGHT,buff=0.25)).arrange(DOWN,buff=0.5)
        self.play(Write(nurse),Write(nurse_senses[0][0]),Write(nurse_senses[1][0]),Write(nurse_senses[2][0]))
        self.wait(9.71)
        self.play(Write(nurse_senses[0][1]))
        self.wait(5)
        self.play(Write(nurse_senses[1][1]))
        self.wait(5)
        self.play(Write(nurse_senses[2][1]))
        self.wait(9.14)

        # Contextualization weight intution
        nurse_example_1 = Text('"I nursed the dog back to health"',color=BLUE).to_edge(UP,buff=1)
        nurse_example_2 = Text('"I love being a nurse"',color=BLUE).to_edge(UP,buff=1)
        self.play(FadeTransform(nurse,nurse_example_1))
        importance = VGroup(Text("important (0.9)",color=GREEN).scale(0.6).next_to(nurse_senses[0][1][1],RIGHT,buff=-0.1).shift(DOWN*0.1),Text("not important (0.1)",color=RED).scale(0.6).next_to(nurse_senses[1][1][1],RIGHT,buff=-0.1).shift(DOWN*0.1),Text("not important (0.2)",color=RED).scale(0.6).next_to(nurse_senses[2][1][1],RIGHT,buff=-0.1).shift(DOWN*0.1),Text("not important (0.1)",color=RED).scale(0.6).next_to(nurse_senses[0][1][1],RIGHT,buff=-0.1).shift(DOWN*0.1),Text("important (0.9)",color=GREEN).scale(0.6).next_to(nurse_senses[1][1][1],RIGHT,buff=-0.1).shift(DOWN*0.1),Text("important (0.7)",color=GREEN).scale(0.6).next_to(nurse_senses[2][1][1],RIGHT,buff=-0.1).shift(DOWN*0.1))
        self.wait(2)
        self.play(FadeTransform(nurse_senses[0][1][1:], importance[0]),FadeTransform(nurse_senses[1][1][1:], importance[1]),FadeTransform(nurse_senses[2][1][1:], importance[2]))
        self.wait(6)
        self.play(FadeTransform(nurse_example_1, nurse_example_2))
        self.wait(2)
        self.play(FadeTransform(importance[0], importance[3]),FadeTransform(importance[1], importance[4]),FadeTransform(importance[2], importance[5]))
        self.wait(7.43)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        # 3 steps
        steps = VGroup(Text("1. Learn Sense Vectors",color=YELLOW),Text("2. Calculate Contextualization Weights",color=PURPLE),Text("3. Sum the Products",color=BLUE)).arrange(DOWN,buff=0.5)
        self.play(Write(steps[0]))
        self.wait(5)
        self.play(Write(steps[1]))
        self.wait(5)
        self.play(Write(steps[2]))
        self.wait(11.14)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        # Analogy
        shed = ImageMobject("source_images/shed.png").scale(0.75)
        hammer = ImageMobject("source_images/hammer.png").scale(0.25).shift(DOWN*1+LEFT*1.25)
        saw = ImageMobject("source_images/saw.png").scale(0.25).next_to(hammer,RIGHT,buff=-1)
        shovel = ImageMobject("source_images/shovel.png").scale(0.25).next_to(saw,RIGHT,buff=-1)
        hoe = ImageMobject("source_images/hoe.png").scale(0.25).next_to(shovel,RIGHT,buff=-1.25)
        context_word_analogy = VGroup(Text("Context").next_to(shed,UP).shift(LEFT*1.75+DOWN*2.15).rotate(30 * DEGREES),Text("Word").next_to(shed,UP).shift(RIGHT*1.5+DOWN*2).rotate(-30 * DEGREES))
        vector_analogy = Text("Sense vectors").scale(0.6).next_to(shed,DOWN)
        vector_analogy_lines = VGroup(Line(start=hammer.get_bottom(),end=vector_analogy.get_top()),Line(start=saw.get_bottom(),end=vector_analogy.get_top()),Line(start=shovel.get_bottom(),end=vector_analogy.get_top()),Line(start=hoe.get_bottom(),end=vector_analogy.get_top()))
        analogy = Group(shed,hammer,saw,shovel,hoe,context_word_analogy,vector_analogy,vector_analogy_lines).shift(UP*0.5)
        self.play(FadeIn(shed),Write(context_word_analogy))
        self.wait(5.43)
        self.play(FadeIn(hammer,saw,shovel,hoe),Write(vector_analogy),Write(vector_analogy_lines))
        self.wait(13.14)
        self.play(analogy.animate.shift(LEFT*3))
        deck = ImageMobject("source_images/deck.png").shift(RIGHT*4).scale(0.5)
        self.play(FadeIn(deck),hammer.animate.scale(1.5),saw.animate.scale(1.5),shovel.animate.scale(0.5),hoe.animate.scale(0.5))
        self.wait(7.14)
        garden = ImageMobject("source_images/garden.png").shift(RIGHT*4).scale(0.5)
        self.play(FadeOut(deck),FadeIn(garden),hammer.animate.scale(0.3333333333),saw.animate.scale(0.333333333),shovel.animate.scale(3),hoe.animate.scale(3))
        self.wait(19.43)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        # Math behind sense vectors
        sentence = VGroup(Text("That",color=YELLOW),Text("move",color=YELLOW),Text("was",color=YELLOW),Text("sick",color=YELLOW)).arrange(RIGHT,buff=1).to_edge(UP)
        self.play(Write(sentence))
        self.wait(4)
        rep_vector_data = [[0, 0],[1, 0],[0, 0],[0, 5]]
        rep_vectors = VGroup()
        for word, vec_values in zip(sentence, rep_vector_data):
            rep_vector = Matrix([[v] for v in vec_values]).scale(0.6).next_to(word, DOWN, buff=0.5)
            rep_vectors.add(rep_vector)
        original_rep_vectors = rep_vectors.copy()
        self.play(Write(rep_vectors))
        self.wait(3.14)
        feed_forward = MathTex("FF").scale(2.5).shift(DOWN*1+LEFT*2)
        self.play(Write(feed_forward))
        self.wait(6.86)
        for rep_vector in rep_vectors:
            rep_vector.get_entries()[0].set_color(GREEN)
            self.wait(0.45)
        for rep_vector in rep_vectors:
            rep_vector.get_entries()[1].set_color(RED)
            self.wait(0.172)
        outputs_mini = VGroup(Matrix([[9],[0]]).scale(0.6).next_to(sentence[2].get_right(),DOWN,buff=2.25),Matrix([[0],[4]]).scale(0.6).next_to(sentence[2].get_right(),DOWN,buff=3.5),Matrix([[0],[5]]).scale(0.6).next_to(sentence[2].get_right(),DOWN,buff=4.75))
        feed_to_outputs = VGroup(Arrow(start=feed_forward.get_right(),end=outputs_mini[0].get_left()),Arrow(start=feed_forward.get_right(),end=outputs_mini[1].get_left()),Arrow(start=feed_forward.get_right(),end=outputs_mini[2].get_left()))
        self.play(rep_vectors[3].animate.next_to(feed_forward,LEFT,buff=2))
        rep_to_feed = Arrow(start=rep_vectors[3].get_right(),end=feed_forward.get_left())
        self.play(GrowArrow(rep_to_feed))
        self.wait(3.71)
        self.play([GrowArrow(feed_to_output) for feed_to_output in feed_to_outputs],Write(outputs_mini))
        contexts = VGroup(Text('"cool, great, ..."',color=GREEN).scale(0.6).next_to(outputs_mini[0],RIGHT),Text('"ill, nausea, ..."',color=RED).scale(0.6).next_to(outputs_mini[1],RIGHT),Text('"throw up, puke, ..."',color=RED).scale(0.6).next_to(outputs_mini[2],RIGHT))
        self.wait(11.14)
        self.play(Write(contexts[0]))
        self.wait(4)
        self.play(Write(contexts[1:]))
        self.wait(5.43)
        self.play(FadeOut(rep_vectors[3],contexts),outputs_mini.animate.scale(0.5).next_to(sentence[3],DOWN,buff=0.4))
        rest_outputs = VGroup(VGroup(Matrix([[0],[0]]).scale(0.6).next_to(sentence[2].get_right(),DOWN,buff=2.25),Matrix([[0],[0]]).scale(0.6).next_to(sentence[2].get_right(),DOWN,buff=3.5),Matrix([[0],[0]]).scale(0.6).next_to(sentence[2].get_right(),DOWN,buff=4.75)),VGroup(Matrix([[3],[0]]).scale(0.6).next_to(sentence[2].get_right(),DOWN,buff=2.25),Matrix([[0],[0]]).scale(0.6).next_to(sentence[2].get_right(),DOWN,buff=3.5),Matrix([[0],[0]]).scale(0.6).next_to(sentence[2].get_right(),DOWN,buff=4.75)),VGroup(Matrix([[0],[0]]).scale(0.6).next_to(sentence[2].get_right(),DOWN,buff=2.25),Matrix([[0],[0]]).scale(0.6).next_to(sentence[2].get_right(),DOWN,buff=3.5),Matrix([[0],[1]]).scale(0.6).next_to(sentence[2].get_right(),DOWN,buff=4.75)))
        for i,vector in enumerate(rep_vectors[:3]):
            self.play(vector.animate.next_to(feed_forward,LEFT,buff=2),Write(rest_outputs[i]),run_time=0.6)
            self.wait(0.25)
            self.play(FadeOut(vector),rest_outputs[i].animate.scale(0.5).next_to(sentence[i],DOWN,buff=0.4),run_time=0.6)
        senses = rest_outputs.copy()
        self.play(FadeOut(outputs_mini))
        senses.add(outputs_mini.align_to(senses[0],UP))
        senses.scale(2).arrange(RIGHT,buff=4)
        self.play(FadeOut(feed_forward,rep_to_feed,feed_to_outputs))
        self.wait(0.79)

        # Math behind contextualization weights
        sentence.set_color(PURPLE)
        self.wait(10)
        self.play(FadeTransform(VGroup(rest_outputs),original_rep_vectors[:3]))
        self.wait(2)
        transformer = MathTex("T").scale(2.5).shift(DOWN*1)
        self.play(Write(transformer), original_rep_vectors[0].animate.next_to(transformer, LEFT, buff=2), run_time=1.143)
        rep_to_trans = Arrow(start=original_rep_vectors[0].get_right(), end=transformer.get_left())
        self.play(GrowArrow(rep_to_trans), run_time=1.143)
        upgraded = VGroup()
        upgraded_rep = Matrix([[1],[0]]).scale(0.6).next_to(sentence[3], DOWN, buff=3.5).set_color(PURE_GREEN)
        upgraded.add(upgraded_rep)
        trans_to_upgraded = Arrow(start=transformer.get_right(), end=upgraded_rep.get_left())
        self.play(GrowArrow(trans_to_upgraded), Write(upgraded_rep), run_time=1.143)
        self.play(FadeOut(original_rep_vectors[0]), upgraded_rep.animate.next_to(sentence[0], DOWN, buff=0.5), run_time=1.143)
        upgraded_reps = VGroup(Matrix([[3],[0]]).scale(0.6).next_to(sentence[3], DOWN, buff=3.5).set_color(PURE_GREEN),Matrix([[1],[0]]).scale(0.6).next_to(sentence[3], DOWN, buff=3.5).set_color(PURE_GREEN))
        for i, vec in enumerate(original_rep_vectors[1:3]):
            self.play(vec.animate.next_to(transformer, LEFT, buff=2), run_time=1.143)
            upgraded_rep = upgraded_reps[i]
            upgraded.add(upgraded_rep)
            self.play(Write(upgraded_rep), run_time=1.143)
            self.play(FadeOut(vec), upgraded_rep.animate.next_to(sentence[i + 1], DOWN, buff=0.5), run_time=1.143)
        self.play(FadeOut(rep_to_trans, transformer, trans_to_upgraded), run_time=1.143)
        self.play(Write(senses[:3].move_to(ORIGIN).shift(DOWN*1+LEFT*2)),run_time=1.257)
        pairs = VGroup()
        for sense_set in senses:
            for sense in sense_set:
                key_matrix_raw = Matrix([[round(random.random(),1),round(random.random(),1),round(random.random(),1)],[round(random.random(),1),round(random.random(),1),round(random.random(),1)],[round(random.random(),1),round(random.random(),1),round(random.random(),1)]],h_buff=1).scale(0.3).set_color(TEAL_D).next_to(sense,RIGHT,buff=0.9)
                key_label = Text("K",color=TEAL_D).scale(0.25).next_to(key_matrix_raw,UP,buff=0.01)
                key_matrix = VGroup(key_matrix_raw,key_label)
                query_matrix_raw = Matrix([[round(random.random(),1),round(random.random(),1),round(random.random(),1)],[round(random.random(),1),round(random.random(),1),round(random.random(),1)],[round(random.random(),1),round(random.random(),1),round(random.random(),1)]],h_buff=1).scale(0.3).set_color(LIGHT_BROWN).next_to(key_matrix_raw,RIGHT,buff=0.9)
                query_label = Text("Q",color=LIGHT_BROWN).scale(0.25).next_to(query_matrix_raw,UP,buff=0.01)
                query_matrix = VGroup(query_matrix_raw,query_label)
                pairs.add(key_matrix,query_matrix)
                self.play(Write(key_matrix),Write(query_matrix),run_time=1.257)
        upgrades = VGroup()
        for i,vec in enumerate(upgraded):
            self.play(vec.animate.scale(0.75),run_time=0.200810811)
            copies = VGroup(vec.copy(),vec.copy(),vec.copy(),vec.copy(),vec.copy())
            self.play(Write(copies),run_time=0.01)
            upgrades.add(vec,*[copy for copy in copies])
        upgrade_matrix_prods = VGroup()
        for i,upgrade in enumerate(upgrades):
                self.play(upgrade.animate.next_to(pairs[i][0],LEFT),run_time=0.200810811)
                mult = MathTex(r"\cdot").scale(0.65).next_to(upgrade,RIGHT,buff=0.1)
                upgrade_matrix_prods.add(VGroup(upgrade,mult,pairs[i]))
                self.play(Write(mult),run_time=0.200810811)
        values = VGroup()
        for i,prod in enumerate(upgrade_matrix_prods):
            if i % 2 != 0:
                query = Text("query",color=LIGHT_BROWN).scale(0.5).move_to(prod.get_center())
                values.add(query)
                self.play(FadeTransform(prod,query),run_time=0.111111111)
            else:
                key = Text("key",color=TEAL_D).scale(0.5).move_to(prod.get_center())
                values.add(key)
                self.play(FadeTransform(prod,key),run_time=0.111111111)
        softmaxes = VGroup()
        for i,value in enumerate(values):
            if i % 2 == 0:
                softmax = VGroup(MathTex(r"softmax("),MathTex(r"key",color=TEAL_D),MathTex(r"\cdot"),MathTex(r"query",color=LIGHT_BROWN),MathTex(r")")).arrange(RIGHT,buff=0.1).scale(0.65).move_to(VGroup(value,values[i+1]).get_center())
                softmax[3].shift(DOWN*0.05)
                softmaxes.add(softmax)
                self.play(FadeTransform(VGroup(value,values[i+1]),softmax),run_time=0.73)
            else:
                continue
        weights = VGroup(MathTex("0.54",color=PURPLE),MathTex("0.19",color=PURPLE),MathTex("0.27",color=PURPLE),MathTex("0.31",color=PURPLE),MathTex("0.43",color=PURPLE),MathTex("0.26",color=PURPLE),MathTex("0.65",color=PURPLE),MathTex("0.16",color=PURPLE),MathTex("0.19",color=PURPLE),MathTex("0.34",color=PURPLE),MathTex("0.37",color=PURPLE),MathTex("0.29",color=PURPLE),MathTex("0.45",color=PURPLE),MathTex("0.23",color=PURPLE),MathTex("0.32",color=PURPLE),MathTex("0.82",color=PURPLE),MathTex("0.11",color=PURPLE),MathTex("0.07",color=PURPLE),MathTex("0.29",color=PURPLE),MathTex("0.28",color=PURPLE),MathTex("0.43",color=PURPLE),MathTex("0.78",color=PURPLE),MathTex("0.11",color=PURPLE),MathTex("0.11",color=PURPLE),MathTex("0.71",color=PURPLE),MathTex("0.17",color=PURPLE),MathTex("0.12",color=PURPLE),MathTex("0.37",color=PURPLE),MathTex("0.36",color=PURPLE),MathTex("0.27",color=PURPLE),MathTex("0.92",color=PURPLE),MathTex("0.06",color=PURPLE),MathTex("0.02",color=PURPLE),MathTex("0.57",color=PURPLE),MathTex("0.24",color=PURPLE),MathTex("0.19",color=PURPLE))
        for i,softmax in enumerate(softmaxes):
            self.play(FadeTransform(softmax,weights[i+27].scale(1.5).move_to(softmax.get_center()).align_to(softmax,LEFT)),run_time=0.25)
        self.wait(5)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        # Putting it together with a math example, step 1
        self.play(Write(steps[0].move_to(ORIGIN)))
        self.wait(4)
        self.play(FadeOut(steps[0]))
        self.play(Write(sentence.set_color(MAROON_E)),run_time=1.66666667)
        self.play(Write(original_rep_vectors[0].next_to(sentence[0],DOWN,buff=0.5)),Write(original_rep_vectors[1].next_to(sentence[1],DOWN,buff=0.5)),Write(original_rep_vectors[2].next_to(sentence[2],DOWN,buff=0.5)),Write(original_rep_vectors[3].next_to(sentence[3],DOWN,buff=0.5)),Write(feed_forward),run_time=1.66666667)
        outputs_senses = senses.copy()
        outputs = VGroup(VGroup(outputs_senses[0][0].next_to(sentence[2].get_right(),DOWN,buff=2.25),outputs_senses[0][1].next_to(sentence[2].get_right(),DOWN,buff=3.5),outputs_senses[0][2].next_to(sentence[2].get_right(),DOWN,buff=4.75)),VGroup(outputs_senses[1][0].next_to(sentence[2].get_right(),DOWN,buff=2.25),outputs_senses[1][1].next_to(sentence[2].get_right(),DOWN,buff=3.5),outputs_senses[1][2].next_to(sentence[2].get_right(),DOWN,buff=4.75)),VGroup(outputs_senses[2][0].next_to(sentence[2].get_right(),DOWN,buff=2.25),outputs_senses[2][1].next_to(sentence[2].get_right(),DOWN,buff=3.5),outputs_senses[2][2].next_to(sentence[2].get_right(),DOWN,buff=4.75)),VGroup(outputs_senses[3][0].next_to(sentence[2].get_right(),DOWN,buff=2.25),outputs_senses[3][1].next_to(sentence[2].get_right(),DOWN,buff=3.5),outputs_senses[3][2].next_to(sentence[2].get_right(),DOWN,buff=4.75)))
        for i,rep_vector in enumerate(original_rep_vectors):
            if i==0:
                self.play(rep_vector.animate.next_to(feed_forward,LEFT,buff=2),run_time=0.555555557)
                self.play(Write(rep_to_feed),Write(feed_to_outputs),Write(outputs[i]),run_time=0.555555557)
                self.play(outputs[i].animate.scale(0.5).next_to(sentence[i],DOWN,buff=0.5),FadeOut(rep_vector),run_time=0.555555557)
            else:
                self.play(rep_vector.animate.next_to(feed_forward,LEFT,buff=2),run_time=0.555555557)
                self.play(Write(outputs[i]),run_time=0.555555557)
                self.play(outputs[i].animate.scale(0.5).next_to(sentence[i],DOWN,buff=0.5),FadeOut(rep_vector),run_time=0.555555557)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        # Putting it together with a math example, step 2
        self.play(Write(steps[1].move_to(ORIGIN)))
        self.wait(1.5)
        self.play(FadeOut(steps[1]))
        self.play(Write(sentence),run_time=0.734285714)
        self.play(Write(original_rep_vectors[0].next_to(sentence[0],DOWN,buff=0.5)),Write(original_rep_vectors[1].next_to(sentence[1],DOWN,buff=0.5)),Write(original_rep_vectors[2].next_to(sentence[2],DOWN,buff=0.5)),Write(original_rep_vectors[3].next_to(sentence[3],DOWN,buff=0.5)),run_time=0.734285714)
        transformer = MathTex("T").scale(2.5).shift(DOWN*1)
        self.play(Write(transformer),run_time=0.734285714)
        upgraded = VGroup()
        upgraded_reps = VGroup(Matrix([[0],[0]]).scale(0.6).next_to(sentence[3], DOWN, buff=3.5).set_color(PURE_GREEN),Matrix([[3],[0]]).scale(0.6).next_to(sentence[3], DOWN, buff=3.5).set_color(PURE_GREEN),Matrix([[1],[0]]).scale(0.6).next_to(sentence[3], DOWN, buff=3.5).set_color(PURE_GREEN),Matrix([[2],[0]]).scale(0.6).next_to(sentence[3], DOWN, buff=3.5).set_color(PURE_GREEN))
        for i, vec in enumerate(original_rep_vectors):
            if i == 0:
                self.play(original_rep_vectors[0].animate.next_to(transformer, LEFT, buff=2), run_time=0.183571428)
                rep_to_trans = Arrow(start=original_rep_vectors[0].get_right(), end=transformer.get_left())
                self.play(GrowArrow(rep_to_trans), run_time=0.183571428)
                upgraded_rep = upgraded_reps[i]
                upgraded.add(upgraded_rep)
                trans_to_upgraded = Arrow(start=transformer.get_right(), end=upgraded_rep.get_left())
                self.play(GrowArrow(trans_to_upgraded), Write(upgraded_rep), run_time=0.183571428)
                self.play(FadeOut(original_rep_vectors[0]), upgraded_rep.animate.next_to(sentence[0], DOWN, buff=0.5), run_time=0.183571428)
            else:
                self.play(vec.animate.next_to(transformer, LEFT, buff=2), run_time=0.183571428)
                upgraded_rep = upgraded_reps[i]
                upgraded.add(upgraded_rep)
                self.play(Write(upgraded_rep), run_time=0.183571428)
                self.play(FadeOut(vec), upgraded_rep.animate.next_to(sentence[i], DOWN, buff=0.5), run_time=0.183571428)
        self.play(FadeOut(rep_to_trans, transformer, trans_to_upgraded))
        upgrades = VGroup()
        for i,vec in enumerate(upgraded):
            self.play(vec.animate.scale(0.75),run_time=0.183571428)
            copies = VGroup(vec.copy(),vec.copy(),vec.copy(),vec.copy(),vec.copy())
            self.play(Write(copies),run_time=0.01)
            upgrades.add(vec,*[copy for copy in copies])
        self.wait(1.14)
        self.play(Write(senses[1].shift(LEFT*4.75)), run_time=0.167)
        self.play(Write(senses[2].shift(LEFT*4.5)), run_time=0.167)
        self.play(Write(senses[3].shift(LEFT*4).align_to(senses[0],UP)), run_time=0.167)
        pairs = VGroup()
        for sense_set in senses[1:]:
            for sense in sense_set:
                key_matrix_raw = Matrix([[round(random.random(),1),round(random.random(),1),round(random.random(),1)],[round(random.random(),1),round(random.random(),1),round(random.random(),1)],[round(random.random(),1),round(random.random(),1),round(random.random(),1)]],h_buff=1).scale(0.3).set_color(TEAL_D).next_to(sense,RIGHT,buff=0.9)
                key_label = Text("K",color=TEAL_D).scale(0.25).next_to(key_matrix_raw,UP,buff=0.01)
                key_matrix = VGroup(key_matrix_raw,key_label)
                query_matrix_raw = Matrix([[round(random.random(),1),round(random.random(),1),round(random.random(),1)],[round(random.random(),1),round(random.random(),1),round(random.random(),1)],[round(random.random(),1),round(random.random(),1),round(random.random(),1)]],h_buff=1).scale(0.3).set_color(LIGHT_BROWN).next_to(key_matrix_raw,RIGHT,buff=0.9)
                query_label = Text("Q",color=LIGHT_BROWN).scale(0.25).next_to(query_matrix_raw,UP,buff=0.01)
                query_matrix = VGroup(query_matrix_raw,query_label)
                pairs.add(key_matrix,query_matrix)
                self.play(Write(key_matrix),Write(query_matrix),run_time=0.514)
        upgrade_matrix_prods = VGroup()
        for i,upgrade in enumerate(upgrades[6:]):
                self.play(upgrade.animate.next_to(pairs[i][0],LEFT),run_time=0.3175)
                mult = MathTex(r"\cdot").scale(0.65).next_to(upgrade,RIGHT,buff=0.1)
                upgrade_matrix_prods.add(VGroup(upgrade,mult,pairs[i]))
                self.play(Write(mult),run_time=0.3175)
        values = VGroup()
        for i,prod in enumerate(upgrade_matrix_prods):
            if i % 2 != 0:
                query = Text("query",color=LIGHT_BROWN).scale(0.5).move_to(prod.get_center())
                values.add(query)
                self.play(FadeTransform(prod,query),run_time=0.222222222)
            else:
                key = Text("key",color=TEAL_D).scale(0.5).move_to(prod.get_center())
                values.add(key)
                self.play(FadeTransform(prod,key),run_time=0.222222222)
        softmaxes = VGroup()
        for i,value in enumerate(values):
            if i % 2 == 0:
                softmax = VGroup(MathTex(r"softmax("),MathTex(r"key",color=TEAL_D),MathTex(r"\cdot"),MathTex(r"query",color=LIGHT_BROWN),MathTex(r")")).arrange(RIGHT,buff=0.1).scale(0.65).move_to(VGroup(value,values[i+1]).get_center())
                softmax[3].shift(DOWN*0.05)
                softmaxes.add(softmax)
                self.play(FadeTransform(VGroup(value,values[i+1]),softmax),run_time=0.222222222)
            else:
                continue
        for i,softmax in enumerate(softmaxes):
            self.play(FadeTransform(softmax,weights[i].scale(1.5).move_to(softmax.get_center()).align_to(softmax,LEFT)),run_time=0.222222222)
        self.wait(2.86)
        step_2 = Group(*[mob for mob in self.mobjects])
        self.play(FadeOut(step_2))

        # Putting it together with a math example, step 3
        self.play(Write(steps[2].move_to(ORIGIN)))
        self.wait(2)
        self.play(FadeOut(steps[2]))
        self.add(step_2)
        w = -1
        sense_sets = VGroup(senses[1:])
        for i,weight in enumerate(weights[:9]):
            if i % 3 == 0:
                w += 1
                x = 0
            else:
                x += 1
            dot_prod = MathTex(r"\cdot").next_to(weight,LEFT,buff=0.25)
            sense_sets.add(VGroup(dot_prod,weight))
            self.play(Write(dot_prod),run_time=0.603333333)
        polished_vectors = VGroup(Matrix([[7.47],[1.85]]).scale(0.5).set_color(ORANGE),Matrix([[7.38],[1.11]]).scale(0.5).set_color(ORANGE),Matrix([[8.73],[1.28]]).scale(0.5).set_color(ORANGE),Matrix([[2.76],[0.19]]).scale(0.5).set_color(ORANGE))
        self.play(FadeTransform(sense_sets,polished_vectors[0]))
        self.wait(4.29)
        self.play(polished_vectors[0].animate.next_to(sentence[0],RIGHT,buff=0),FadeOut(upgrades[:6]))
        self.wait(11.14)

        # Putting it together with a math example, the rest
        run_time = 0.12
        for h, sentence_word in enumerate(sentence[1:]):
            y = (h+1) * 6
            [u.move_to(upgrades[0].get_center()) for u in upgrades[:6]]
            self.play(upgrades[:6].animate.scale(2).scale(0.5).move_to(sentence[0].get_center()).shift(DOWN*1), run_time=run_time)
            [u.move_to(upgrades[6].get_center()) for u in upgrades[6:12]]
            self.play(upgrades[6:12].animate.scale(2).scale(0.5).move_to(sentence[1].get_center()).shift(DOWN*1), run_time=run_time)
            [u.move_to(upgrades[12].get_center()) for u in upgrades[12:18]]
            self.play(upgrades[12:18].animate.scale(2).scale(0.5).move_to(sentence[2].get_center()).shift(DOWN*1), run_time=run_time)
            [u.move_to(upgrades[18].get_center()) for u in upgrades[18:24]]
            self.play(upgrades[18:24].animate.scale(2).scale(0.5).move_to(sentence[3].get_center()).shift(DOWN*1), run_time=run_time)
            modified_senses = VGroup()
            if h == 0:
                 self.play(Write(senses[0]), run_time=run_time)
                 self.play(Write(senses[2]), run_time=run_time)
                 self.play(Write(senses[3].align_to(senses[0],UP)), run_time=run_time)
                 modified_senses.add(senses[0],senses[2],senses[3])
            elif h == 1:
                 self.play(Write(senses[0]), run_time=run_time)
                 self.play(Write(senses[1].shift(RIGHT*4.5)), run_time=run_time)
                 self.play(Write(senses[3].align_to(senses[0],UP)), run_time=run_time)
                 modified_senses.add(senses[0],senses[1],senses[3])
            elif h == 2:
                 self.play(Write(senses[0]), run_time=run_time)
                 self.play(Write(senses[1]), run_time=run_time)
                 self.play(Write(senses[2].shift(RIGHT*4)), run_time=run_time)
                 modified_senses.add(senses[0],senses[1],senses[2])
            pairs = VGroup()
            for sense_set in modified_senses:
                for sense in sense_set:
                    key_matrix_raw = Matrix([[round(random.random(),1),round(random.random(),1),round(random.random(),1)],[round(random.random(),1),round(random.random(),1),round(random.random(),1)],[round(random.random(),1),round(random.random(),1),round(random.random(),1)]], h_buff=0.75).scale(0.3).set_color(TEAL_D).next_to(sense, RIGHT, buff=0.9)
                    key_label = Text("K", color=TEAL_D).scale(0.25).next_to(key_matrix_raw, UP, buff=0.01)
                    key_matrix = VGroup(key_matrix_raw, key_label)
                    query_matrix_raw = Matrix([[round(random.random(),1),round(random.random(),1),round(random.random(),1)],[round(random.random(),1),round(random.random(),1),round(random.random(),1)],[round(random.random(),1),round(random.random(),1),round(random.random(),1)]], h_buff=0.75).scale(0.3).set_color(LIGHT_BROWN).next_to(key_matrix_raw, RIGHT, buff=0.9)
                    query_label = Text("Q", color=LIGHT_BROWN).scale(0.25).next_to(query_matrix_raw, UP, buff=0.01)
                    query_matrix = VGroup(query_matrix_raw, query_label)
                    pairs.add(key_matrix, query_matrix)
                    self.play(Write(key_matrix), Write(query_matrix), run_time=run_time)
            upgrade_matrix_prods = VGroup()
            for i, upgrade in enumerate(upgrades[:y]):
                self.play(upgrade.animate.next_to(pairs[i][0], LEFT), run_time=run_time)
                mult = MathTex(r"\cdot").scale(0.75).next_to(upgrade, RIGHT, buff=0.1)
                upgrade_matrix_prods.add(VGroup(upgrade, mult, pairs[i]))
                self.play(Write(mult), run_time=run_time)
            for i, upgrade in enumerate(upgrades[(y+6):]):
                i = y + i
                self.play(upgrade.animate.next_to(pairs[i][0], LEFT), run_time=run_time)
                mult = MathTex(r"\cdot").scale(0.65).next_to(upgrade, RIGHT, buff=0.1)
                upgrade_matrix_prods.add(VGroup(upgrade, mult, pairs[i]))
                self.play(Write(mult), run_time=run_time)
            values = VGroup()
            for i, prod in enumerate(upgrade_matrix_prods):
                if i % 2 != 0:
                    query = Text("query", color=LIGHT_BROWN).scale(0.5).move_to(prod.get_center())
                    values.add(query)
                    self.play(FadeTransform(prod, query), run_time=run_time)
                else:
                    key = Text("key", color=TEAL_D).scale(0.5).move_to(prod.get_center())
                    values.add(key)
                    self.play(FadeTransform(prod, key), run_time=run_time)
            softmaxes = VGroup()
            for i, value in enumerate(values):
                if i % 2 == 0:
                    softmax = VGroup(MathTex(r"softmax("), MathTex(r"key", color=TEAL_D), MathTex(r"\cdot"), MathTex(r"query", color=LIGHT_BROWN), MathTex(r")")).arrange(RIGHT, buff=0.1).scale(0.65).move_to(VGroup(value, values[i+1]).get_center())
                    softmax[3].shift(DOWN * 0.05)
                    softmaxes.add(softmax)
                    self.play(FadeTransform(VGroup(value, values[i+1]), softmax), run_time=run_time)
                else:
                    continue
            for i, softmax in enumerate(softmaxes):
                weights_index = (h * 9) + 9
                self.play(FadeTransform(softmax, weights[weights_index+i].scale(1.5).move_to(softmax.get_center()).align_to(softmax, LEFT)), run_time=run_time)
            w = -1
            sense_sets = VGroup(modified_senses)
            for i, weight in enumerate(weights[weights_index:]):
                if i % 3 == 0:
                    w += 1
                    x = 0
                else:
                    x += 1
                dot_prod = MathTex(r"\cdot").next_to(weight, LEFT, buff=0.2)
                sense_sets.add(VGroup(dot_prod, weight))
                self.play(Write(dot_prod), run_time=run_time)
                if i == 9:
                    break
            self.play(FadeTransform(sense_sets, polished_vectors[h+1]), run_time=run_time)
            self.play(polished_vectors[h+1].animate.next_to(sentence[(h+1)], RIGHT, buff=0), run_time=run_time)
        self.play(FadeOut(upgrades[18:24]))
        final_sentiment_vector = Matrix([[6.59],[1.11]],bracket_h_buff=0.2).scale(2)
        final_sentiment_vector.get_entries()[0].set_color(GREEN)
        final_sentiment_vector.get_entries()[1].set_color(RED)
        self.wait(23.71)
        self.play(FadeTransform(polished_vectors,final_sentiment_vector))
        subtraction = Text("-",font_size=150,color=RED).next_to(final_sentiment_vector.get_rows()[1],LEFT,buff=1)
        score_line = Line(start=final_sentiment_vector.get_left(),end=final_sentiment_vector.get_right(),stroke_width=10).next_to(final_sentiment_vector,DOWN,buff=0.25)
        score = Text("5.48",color=GREEN).next_to(score_line,DOWN,buff=0.5).scale(1.5)
        self.play(Write(subtraction),Write(score_line),Write(score))

        # Conclusion of example with strengths of backpack model
        self.wait(17.43)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        transformer = Rectangle(width=4, height=5.5).shift(LEFT*4.75)
        transformer_label = Text("Transformer",color=BLUE).next_to(transformer,UP)
        self.play(Write(transformer),Write(transformer_label))
        weights = VGroup()
        for i in range(1, 251):
            weight_label = MathTex(f"w_{{{i}}}",color=BLUE).scale(0.5)
            weights.add(weight_label)
        center = transformer.get_center()
        width = transformer.get_width()
        height = transformer.get_height()
        padding = 0.2
        for weight in weights:
            x_offset = np.random.uniform(-width / 2 + padding, width / 2 - padding)
            y_offset = np.random.uniform(-height / 2 + padding, height / 2 - padding)
            weight.move_to(center + np.array([x_offset, y_offset, 0]))
        self.play(LaggedStart(*[Write(weight) for weight in weights], lag_ratio=0.01))
        output_vector = Matrix([[1],[0]],bracket_h_buff=0.2).shift(RIGHT*6.5)
        output_vector.get_entries()[0].set_color(GREEN)
        output_vector.get_entries()[1].set_color(RED)
        transformer_to_output = Arrow(start=transformer.get_right(),end=output_vector.get_left())
        self.play(GrowArrow(transformer_to_output),Write(output_vector))
        self.wait(6.29)
        self.play(FadeOut(transformer_to_output))
        backpack = Rectangle(width=2, height=1.5).shift(RIGHT * 1.45)
        backpack_label = Text("Backpack",color=GREEN).next_to(backpack,UP)
        weights = VGroup()
        for i in range(12):
            weight = MathTex(f"w_{{{i+1}}}",color=GREEN).scale(0.5)
            weight.move_to(backpack.get_center() + UP * (0.5 - (i // 4) * 0.5) + LEFT * (0.75 - (i % 4) * 0.5))
            weights.add(weight)
        transformer_to_backpack = Arrow(start=transformer.get_right(),end=backpack.get_left())
        backpack_to_output = Arrow(start=backpack.get_right(),end=output_vector.get_left())
        self.play(Write(backpack_label), GrowArrow(transformer_to_backpack),Write(backpack), Write(weights), GrowArrow(backpack_to_output))
        self.wait(14.29)
        slider_line = Line(start=LEFT, end=RIGHT, color=PURPLE).set_length(2).next_to(weights[11],DOWN,buff=2)
        knob = Circle(radius=0.1, color=PURPLE, fill_opacity=1).move_to(slider_line.get_start())
        slider_position = ValueTracker(0.91)
        label_top = Text("Nurse", font_size=24, color=RED).next_to(slider_line, UP, buff=0.25)
        label_left = Text("Male", font_size=13).next_to(slider_line.get_left(), DOWN, buff=0.15)
        label_right = Text("Female", font_size=13).next_to(slider_line.get_right(), DOWN, buff=0.15)
        weight_to_slider = Line(start=weights[11].get_bottom(),end=label_top.get_top(),stroke_width=2)
        counter = DecimalNumber(slider_position.get_value(), color=RED).scale(0.75).next_to(slider_line, DOWN)
        def update_knob(knob):
            knob.move_to(slider_line.point_from_proportion(slider_position.get_value()))
        def update_counter(counter):
            value = slider_position.get_value()
            counter.set_value(value)
            counter.set_color(interpolate_color(RED, GREEN, (0.91 - value) / 0.4))
        def update_label(label):
            value = slider_position.get_value()
            label.set_color(interpolate_color(RED, GREEN, (0.91 - value) / 0.4))
        knob.add_updater(update_knob)
        counter.add_updater(update_counter)
        label_top.add_updater(update_label)
        self.play(Write(weight_to_slider), Write(label_top), Write(slider_line), Write(knob), Write(label_left), Write(counter), Write(label_right))
        self.wait(2.57)
        self.play(slider_position.animate.set_value(0.5), run_time=2)
        self.wait(4.29)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

