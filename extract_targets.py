
def target(filename, animation):
    return "media/videos/%s/480p15/%s.mp4: $(PYTHON)\n\tmanim -pql %s.py $(basename $(notdir $@))\n" % (filename, animation, filename)

if __name__ == "__main__":
    from glob import glob

    targets = {}

    all_targets = []
    for filename in [x.replace(".py", "") for x in glob("*.py")]:
        lines = [x.strip() for x in open("%s.py" % filename, 'r').readlines()]
        animations = [x.split("(")[0].replace("class ", "") for x in lines if x.startswith("class")]
        targets[filename] = animations
        all_targets += ["media/videos/%s/480p15/%s.mp4" % (filename, x) for x in animations]

    for filename in targets:
        for animation in targets[filename]:
            print(target(filename, animation))

    print("all: " + " ".join(all_targets))

    
