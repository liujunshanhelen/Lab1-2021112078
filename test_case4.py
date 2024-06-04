import my_graph
import pickle
def test_get_bridge_words_word1_empty():
    g = my_graph.graph('test.txt')  # 读取时自动生成图 —— 需求1
    with open('data.pkl', 'wb') as f0:
        pickle.dump(g, f0)
    bridge_words =g.get_bridge_words("", "new")
    assert bridge_words is None
