# Խնդիր 7: Սահմանել ենթածրագիր, որը ստանում է տեքստ և
#          հաշվում է, թե տեքստի քանի տոկոսն են կազմում 
#          բացատները։ Օրինակ, եթե տեքստի երկարությունը 
#          200 նիշ է, իսկ դրանցից 48-ը բացատներ են, ապա 
#          պետք է վերադարձնել 24 թիվը։

def space_percentile(text):
    length = len(text)
    if length == 0:
        return 0

    spaces = text.count(' ')
    return spaces * 100 / length
