# 第三题： RNA到蛋白质序列的翻译（RNA to Protein Sequence Translation）  

def protein(rna):
    CDEWARS = ""
    for i in range(0, len(rna), 3):
        m = rna[i:i+3]
        n = PROTEIN_DICT[m]
        if n == "Stop":
            break
        CDEWARS += n
    return CDEWARS
