import my_graph
import pickle

def test_get_bridge_words_word_not_exist():
    g = my_graph.graph('test.txt')  # 读取时自动生成图 —— 需求1
    with open('data.pkl', 'wb') as f0:
        pickle.dump(g, f0)
    bridge_words = g.get_bridge_words("To", "invalid")
    assert bridge_words is None
