import pympi
import glob

elan_files = glob.glob("./media/*.eaf")
annotations = []

for elan_file in elan_files:
    current_file = pympi.Elan.Eaf(elan_file)

    current_tiers = current_file.get_tier_ids_for_linguistic_type('refT', parent=None)

    for tier in current_tiers:
        utterances = current_file.get_annotation_data_for_tier(tier)
        for number, annotation in enumerate(utterances):
            segment = [elan_file.partition("/media/")[2].partition(".eaf")[0], tier.split("@",1)[1], (annotation[0] / 1000), ((annotation[1] - annotation[0]) / 1000)]
            annotations.append(segment)

annotations = sorted(annotations, key = lambda x: (x[0], x[2]))

# annotations

with open('./ikdp/data/protocol1.train.mdtm', 'w') as f:
    for ann in annotations:
        #f.write('%s %s %s speaker NA unknown %s\n' % (ann[0], round(ann[2], 3), round(ann[3], 3), ann[1]))
        f.write('%s 1 %s %s speaker NA unknown %s\n' % (ann[0], ann[2], ann[3], ann[1]))
