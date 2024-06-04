import my_graph
#from my_graph import getArgs
import pickle
import random

if __name__ == "__main__":
   # i_path, i_filename = getArgs()
    g = my_graph.graph('test.txt')  # 读取时自动生成图 —— 需求1
    with open('data.pkl','wb')as f0:
        pickle.dump(g, f0)
    print(g.get_nodes())
    print(g.get_edges())
    print(g.get_weights())
    print()

    g.draw_graph()  # 绘制图形 —— 需求2

    print('test3: please input 2 words:\n')
    word1 = input('word1:\n')
    word2 = input('word2:\n')
    g.get_bridge_words(word1, word2)  # 输出桥接词 —— 需求3
    print()

    sentence = input('test4:input setence:\n')
    print(g.make_sentence(sentence))
    print()

    print('输入两个节点，求最短路径')   # 输出最短路径 —— 需求5
    node1 = input('node1:')
    node2 = input('node2:')
    shortest_path=g.get_shortest_path(node1, node2)
    print(shortest_path)
    if(shortest_path != None):
        g.print_get_shortest_path(shortest_path)

    var = input('展示所有点到一个节点的最短距离，请输入节点信息：')
    for node in g.get_nodes():
        print(g.get_shortest_path(var, node))
    print()

    r = random.choice(g.get_nodes())
    print(g.wander(r))  # 随机游走 —— 需求6




