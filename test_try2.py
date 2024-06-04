import my_graph
import pickle
import random

def test_bridge():
    # i_path, i_filename = getArgs()
    g = my_graph.graph('test.txt')  # 读取时自动生成图 —— 需求1
    with open('data.pkl', 'wb') as f0:
        pickle.dump(g, f0)

    print('test3: please input 2 words:\n')
    word1 = input('word1:\n')
    word2 = input('word2:\n')
    g.get_bridge_words(word1, word2)  # 输出桥接词 —— 需求3
    print()


