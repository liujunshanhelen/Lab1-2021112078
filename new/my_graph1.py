'''
the graph module
'''
import random
import string
import argparse
import networkx as nx
import matplotlib.pyplot as plt


def get_args():
    '''
    get arguments
    :return:
    '''
    parser = argparse.ArgumentParser(description='如果你没有采用命令行参数输入参数，请在下面重新输入参数')
    parser.add_argument('--path', help='path')
    parser.add_argument('--filename', help='filename')
    args = parser.parse_args()

    i_path = args.path
    i_filename = args.filename
    if not i_path:
        i_path = input('path:')
    if not i_filename:
        i_filename = input('filename:')
    return i_path, i_filename


class Graph:
    '''
    Graph(file_path)
    '''
    def __init__(self, file_path):
        text = self.__read_file(file_path)
        self.__nodes = []
        self.__edges = {}
        self.__weights = {}
        self.__create_graph(text)

    def get_nodes(self):
        '''
        NODES
        :return:
        '''
        return self.__nodes.copy()

    def get_edges(self):
        '''
        EDGES
        :return:
        '''
        return self.__edges.copy()

    def get_weights(self):
        '''
        WEIGHTS
        :return:
        '''
        return self.__weights.copy()

    def draw_graph(self):
        '''
        DRAW
        :return:
        '''
        graph = nx.DiGraph()
        graph.add_nodes_from(self.__nodes)
        for node in self.__nodes:
            edges = self.__edges.get(node)
            if edges is None:
                continue
            for edge in edges:
                graph.add_edge(node, edge, weight=self.__weights[(node, edge)])

        # 绘制图形
        # pos = nx.spring_layout(G)  # 图形布局
        pos = nx.kamada_kawai_layout(graph)
        nx.draw_networkx(graph,
                         pos,
                         with_labels=True,
                         node_color='skyblue',
                         edge_color='gray')
        # 获取边的权重 ：两种不同写法
        # edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
        edge_labels = nx.get_edge_attributes(graph, 'weight')
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
        # 显示图形
        plt.show()

    def get_bridge_words(self, word1, word2):
        '''
        BRIDGE_WORDS
        :param word1:
        :param word2:
        :return:
        '''
        word1 = word1.lower()
        word2 = word2.lower()
        if word1 not in self.__nodes or word2 not in self.__nodes:
            print("No word1 or word2 in the graph!")
            return None
        res = []
        word1_next = self.__edges[word1]
        for word in word1_next:
            word_next = self.__edges[word]
            for word_n in word_next:
                if word_n == word2:
                    res.append(word)
        if len(res) == 0:
            print("No bridge words from word1 to word2!")
            return None

        if len(res) == 1:
            print_str = "The bridge word from word1 to word2 is: "
            print_str += res[0]
        else:
            print_str = "The bridge words from word1 to word2 are: "
            for i in range(len(res) - 2):
                print_str += res[i] + ", "
            print_str += res[-2] + " and " + res[-1]
        print(print_str)
        return res

    def make_sentence(self, sentence):
        '''
        MAKE_SENTENCE
        :param sentence:
        :return:
        '''
        words = sentence.split()  # 假设输入的句子是合法的
        # 小写
        for i, j in enumerate(words):
            words[i] = j.lower()
        res = []
        for i in range(len(words) - 1):
            res.append(words[i])
            if words[i] in self.__nodes and words[i + 1] in self.__nodes:
                bridge_words = self.get_bridge_words(words[i], words[i + 1])
                if bridge_words is not None:
                    res.append(bridge_words[0])
        res.append(words[-1])
        return ' '.join(res)

    def get_shortest_path(self, word1, word2):
        '''
        GET_SHORTEST_PATH
        :param word1:
        :param word2:
        :return:
        '''
        word1 = word1.lower()
        word2 = word2.lower()
        # 广度优先搜索
        if word1 not in self.__nodes or word2 not in self.__nodes:
            print("No word1 or word2 in the graph!")
            return None
        if word1 == word2:
            return [word1, word2]

        visited = [word1]
        queue = [word1]
        path_queue = [[word1]]
        distence = {word1: 0}
        path = {word1: [word1]}
        while queue:
            node = queue.pop(0)
            current_path = path_queue.pop(0)

            for word in self.__edges[node]:
                now_path = current_path.copy()
                now_path.append(word)
                if word not in visited:
                    visited.append(word)
                    queue.append(word)
                    path_queue.append(now_path)

                if (word not in distence
                        or distence[word] > distence[node]
                        + self.__weights[(node, word)]):
                    distence[word] = (distence[node]
                                      + self.__weights[(node, word)])
                    path[word] = now_path
        if word2 not in visited:
            print("No path from word1 to word2!")
            return None
        print(" -> ".join(path[word2]))
        return distence[word2], path[word2]

    def print_get_shortest_path(self, shortest_path):
        '''
        SHORTEST_PATH
        :param shortest_path:
        :return:
        '''
        shortest_path = shortest_path[1]
        # 绘制图形
        graph = nx.DiGraph()
        graph.add_nodes_from(self.__nodes)
        for node in self.__nodes:
            edges = self.__edges.get(node)
            if edges is None:
                continue
            for edge in edges:
                graph.add_edge(node, edge, weight=self.__weights[(node, edge)])

        pos = nx.kamada_kawai_layout(graph)  # 图形布局
        nx.draw(graph,
                pos,
                with_labels=True,
                node_color='skyblue',
                edge_color='gray')  # 先绘制整个图
        nx.draw_networkx_edges(graph,
                               pos,
                               edgelist=[(shortest_path[i],
                                          shortest_path[i + 1])
                                         for i in
                                         range(len(shortest_path) - 1)],
                               edge_color='r', width=2)
        # 再单独标注最短路径的边为红色

        # 显示图形
        plt.show()

    def wander(self, word):
        '''
       WANDER
        :param word:
        :return:
        '''
        word = word.lower()
        if word not in self.__nodes:
            print("No such word in the graph!")
            return None
        res = [word]
        walked_edge = []
        while True:
            next_words = self.__edges[word]
            if len(next_words) == 0:
                break
            # 随机一个
            next_word = next_words[random.randint(0, len(next_words) - 1)]
            if (word, next_word) in walked_edge:
                break
            res.append(next_word)
            walked_edge.append((word, next_word))
            word = next_word
        with open('./wander', 'a', encoding='utf-8')as file:
            file.write(' '.join(res))
            file.write('\n')
        return " ".join(res)

    def __read_file(self, file_path):
        res_list = []
        with open(file_path, "r", encoding='utf-8') as file:  # 打开文件
            data = file.read()
            for i in data:
                if i in [' ', '\r', '\n'] or i in string.punctuation:
                    res_list.append(' ')
                elif i.isalpha():
                    res_list.append(i)
        return ''.join(res_list)

    def __create_graph(self, text):
        words = text.split()
        # print(words)
        for i in range(len(words) - 1):
            # 小写
            self.__add_edge(words[i].lower(), words[i + 1].lower())

    def __add_edge(self, word_from, word_to):
        if word_from not in self.__nodes:
            self.__nodes.append(word_from)
            self.__edges[word_from] = []
        if word_to not in self.__nodes:
            self.__nodes.append(word_to)
            self.__edges[word_to] = []
        if word_to not in self.__edges[word_from]:
            self.__edges[word_from].append(word_to)
            self.__weights[(word_from, word_to)] = 1
        else:
            self.__weights[(word_from, word_to)] += 1
