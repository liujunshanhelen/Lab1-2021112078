import my_graph
import pickle
import random
def test_get_bridge_words_words_exist_with_bridge_words():
    # i_path, i_filename = getArgs()
    g = my_graph.graph('test.txt')  # 读取时自动生成图 —— 需求1
    with open('data.pkl', 'wb') as f0:
        pickle.dump(g, f0)
    bridge_words = g.get_bridge_words("To", "new")
    assert bridge_words is not None
    assert len(bridge_words) == 2
    assert "explore" in bridge_words
    assert "seek" in bridge_words

