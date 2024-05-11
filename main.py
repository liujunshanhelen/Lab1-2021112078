import my_graph

if __name__ == "__main__":
    g = my_graph.graph("test.txt")  # 读取时自动生成图 —— 需求1
    print(g.get_nodes())
    print(g.get_edges())
    print(g.get_weights())
    print()

    g.draw_graph()  # 绘制图形 —— 需求2

    g.get_bridge_words("To", "out")  # 输出桥接词 —— 需求3
    print()

    print(g.make_sentence("Seek to explore new and exciting synergies"))  # 生成句子 —— 需求4
    print()
    shortest_path=g.get_shortest_path("To", "and")
    print(shortest_path)  # 输出最短路径 —— 需求5
    g.print_get_shortest_path(shortest_path)
    print()

    print(g.wander("to"))  # 随机游走 —— 需求6
    print(g.wander("to"))
    print(g.wander("to"))
    print(g.wander("to"))
    print(g.wander("to"))



