# 第一题：淘气还是乖孩子（Naughty or Nice）
def naughty_or_nice(data):
    nau=0
    nic=0
    for mouth ,keys in data.items():
        for key , value in keys.items():
            if value=='Naughty':
                nau+=1
            elif value=='Nice':
                nic+=1
    if nic >= nau:
        return "Nice!"
    else:
        return "Naughty!"
