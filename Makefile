IMAGES := $(wildcard *.*)
media/videos/Dictionary/480p15/Dictionary1.mp4: $(IMAGES) Dictionary.py
	./venv/bin/python3 -m manim -pql Dictionary.py $(basename $(notdir $@))

media/videos/Dictionary/480p15/Dictionary2.mp4: $(IMAGES) Dictionary.py
	./venv/bin/python3 -m manim -pql Dictionary.py $(basename $(notdir $@))

media/videos/HidenstateIntuition/480p15/HiddenhidenStateIntuition.mp4: $(IMAGES) HidenstateIntuition.py
	./venv/bin/python3 -m manim -pql HidenstateIntuition.py $(basename $(notdir $@))

media/videos/HidenstateIntuition/480p15/yhat.mp4: $(IMAGES) HidenstateIntuition.py
	./venv/bin/python3 -m manim -pql HidenstateIntuition.py $(basename $(notdir $@))

media/videos/RNNs/480p15/IntrotoRNNs.mp4: $(IMAGES) RNNs.py
	./venv/bin/python3 -m manim -pql RNNs.py $(basename $(notdir $@))

media/videos/RNNs/480p15/TokenEncoding.mp4: $(IMAGES) RNNs.py
	./venv/bin/python3 -m manim -pql RNNs.py $(basename $(notdir $@))

media/videos/RNNs/480p15/HiddenStateIntuition.mp4: $(IMAGES) RNNs.py
	./venv/bin/python3 -m manim -pql RNNs.py $(basename $(notdir $@))

media/videos/RNNs/480p15/Hidden_State_Computations.mp4: $(IMAGES) RNNs.py
	./venv/bin/python3 -m manim -pql RNNs.py $(basename $(notdir $@))

media/videos/RNNs/480p15/Example.mp4: $(IMAGES) RNNs.py
	./venv/bin/python3 -m manim -pql RNNs.py $(basename $(notdir $@))

media/videos/SLSA/480p15/IntrotoSLSAIntuition.mp4: $(IMAGES) SLSA.py
	./venv/bin/python3 -m manim -pql SLSA.py $(basename $(notdir $@))

media/videos/SLSA/480p15/Sselfattentionscore.mp4: $(IMAGES) SLSA.py
	./venv/bin/python3 -m manim -pql SLSA.py $(basename $(notdir $@))

media/videos/SLSA/480p15/Example1.mp4: $(IMAGES) SLSA.py
	./venv/bin/python3 -m manim -pql SLSA.py $(basename $(notdir $@))

media/videos/SLSA/480p15/ValueMatrixAttention.mp4: $(IMAGES) SLSA.py
	./venv/bin/python3 -m manim -pql SLSA.py $(basename $(notdir $@))

media/videos/Backpack/480p15/Backpack_Model.mp4: $(IMAGES) Backpack.py
	./venv/bin/python3 -m manim -pql Backpack.py $(basename $(notdir $@))

media/videos/CBOW/480p15/CBoW.mp4: $(IMAGES) CBOW.py
	./venv/bin/python3 -m manim -pql CBOW.py $(basename $(notdir $@))

media/videos/Overview/480p15/Overview.mp4: $(IMAGES) Overview.py
	./venv/bin/python3 -m manim -pql Overview.py $(basename $(notdir $@))

all: media/videos/Dictionary/480p15/Dictionary1.mp4 media/videos/Dictionary/480p15/Dictionary2.mp4 media/videos/HidenstateIntuition/480p15/HiddenhidenStateIntuition.mp4 media/videos/HidenstateIntuition/480p15/yhat.mp4 media/videos/RNNs/480p15/IntrotoRNNs.mp4 media/videos/RNNs/480p15/TokenEncoding.mp4 media/videos/RNNs/480p15/HiddenStateIntuition.mp4 media/videos/RNNs/480p15/Hidden_State_Computations.mp4 media/videos/RNNs/480p15/Example.mp4 media/videos/SLSA/480p15/IntrotoSLSAIntuition.mp4 media/videos/SLSA/480p15/Sselfattentionscore.mp4 media/videos/SLSA/480p15/Example1.mp4 media/videos/SLSA/480p15/ValueMatrixAttention.mp4 media/videos/Backpack/480p15/Backpack_Model.mp4 media/videos/CBOW/480p15/CBoW.mp4 media/videos/Overview/480p15/Overview.mp4
