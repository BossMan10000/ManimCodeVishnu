IMAGES := $(wildcard *.*)
media/videos/Dictionary/480p15/Dictionary.mp4: $(IMAGES) Dictionary1.py
	manim -pql Dictionary.py $(basename $(notdir $@))

media/videos/Dictionary/480p15/Dictionary.mp4: $(IMAGES) Dictionary2.py
	manim -pql Dictionary.py $(basename $(notdir $@))

media/videos/HidenstateIntuition/480p15/HidenstateIntuition.mp4: $(IMAGES) HiddenhidenStateIntuition.py
	manim -pql HidenstateIntuition.py $(basename $(notdir $@))

media/videos/HidenstateIntuition/480p15/HidenstateIntuition.mp4: $(IMAGES) yhat.py
	manim -pql HidenstateIntuition.py $(basename $(notdir $@))

media/videos/RNNs/480p15/RNNs.mp4: $(IMAGES) IntrotoRNNs.py
	manim -pql RNNs.py $(basename $(notdir $@))

media/videos/RNNs/480p15/RNNs.mp4: $(IMAGES) TokenEncoding.py
	manim -pql RNNs.py $(basename $(notdir $@))

media/videos/RNNs/480p15/RNNs.mp4: $(IMAGES) HiddenStateIntuition.py
	manim -pql RNNs.py $(basename $(notdir $@))

media/videos/RNNs/480p15/RNNs.mp4: $(IMAGES) Hidden_State_Computations.py
	manim -pql RNNs.py $(basename $(notdir $@))

media/videos/RNNs/480p15/RNNs.mp4: $(IMAGES) Example.py
	manim -pql RNNs.py $(basename $(notdir $@))

media/videos/SLSA/480p15/SLSA.mp4: $(IMAGES) IntrotoSLSAIntuition.py
	manim -pql SLSA.py $(basename $(notdir $@))

media/videos/SLSA/480p15/SLSA.mp4: $(IMAGES) Sselfattentionscore.py
	manim -pql SLSA.py $(basename $(notdir $@))

media/videos/SLSA/480p15/SLSA.mp4: $(IMAGES) Example1.py
	manim -pql SLSA.py $(basename $(notdir $@))

media/videos/SLSA/480p15/SLSA.mp4: $(IMAGES) ValueMatrixAttention.py
	manim -pql SLSA.py $(basename $(notdir $@))

media/videos/Backpack/480p15/Backpack.mp4: $(IMAGES) Backpack_Model.py
	manim -pql Backpack.py $(basename $(notdir $@))

media/videos/CBOW/480p15/CBOW.mp4: $(IMAGES) CBoW.py
	manim -pql CBOW.py $(basename $(notdir $@))

media/videos/Overview/480p15/Overview.mp4: $(IMAGES) Overview.py
	manim -pql Overview.py $(basename $(notdir $@))

all: media/videos/Dictionary/480p15/Dictionary1.mp4 media/videos/Dictionary/480p15/Dictionary2.mp4 media/videos/HidenstateIntuition/480p15/HiddenhidenStateIntuition.mp4 media/videos/HidenstateIntuition/480p15/yhat.mp4 media/videos/RNNs/480p15/IntrotoRNNs.mp4 media/videos/RNNs/480p15/TokenEncoding.mp4 media/videos/RNNs/480p15/HiddenStateIntuition.mp4 media/videos/RNNs/480p15/Hidden_State_Computations.mp4 media/videos/RNNs/480p15/Example.mp4 media/videos/SLSA/480p15/IntrotoSLSAIntuition.mp4 media/videos/SLSA/480p15/Sselfattentionscore.mp4 media/videos/SLSA/480p15/Example1.mp4 media/videos/SLSA/480p15/ValueMatrixAttention.mp4 media/videos/Backpack/480p15/Backpack_Model.mp4 media/videos/CBOW/480p15/CBoW.mp4 media/videos/Overview/480p15/Overview.mp4
