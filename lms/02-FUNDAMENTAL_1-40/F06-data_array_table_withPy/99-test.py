treasure_box = {'rope': {'coin': 1, 'pcs': 2},
                'apple': {'coin': 2, 'pcs': 10},
                'torch': {'coin': 2, 'pcs': 6},
                'gold coin': {'coin': 5, 'pcs': 50},
                'knife': {'coin': 1, 'pcs': 30}}

print(type(treasure_box))

def display_stuff(ptreasure_box):
    ## type your code
    for k, v in ptreasure_box.items():
        print("you have {} {}pcs".format(k, v))


#display_stuff(treasure_box)


def total_silver(treasure_box):
    total_coin = 0

    for k, v in treasure_box.items():
        coin = v['coin'] * v['pcs']
        print("{} : {}coins/pcs * {}pcs = {} coins".format(k, v['coin'] , v['pcs'], coin))
        total_coin += coin
    print('total_coin : ', total_coin)




total_silver(treasure_box)