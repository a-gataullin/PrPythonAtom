from flask import Flask, request, jsonify

app = Flask(__name__)

class PrefixTree:
    #TODO реализация класса prefix tree, методы как на лекции + метод дать топ 10 продолжений. Скажем на строку кросс выдаем кроссовки, кроссовочки итп. Как хранить топ? 
    #Решать вам. Можно, конечно, обходить все ноды, но это долго. Дешевле чуток проиграть по памяти, зато отдавать быстро (скажем можно взять кучу)
    #В терминальных (конечных) нодах может лежать json с топ актерами.
    def __init__(self):
        self.root = [{}]
        
    def add(self, string, json, rating):               # node = [dict_of_nodes, top_10, min_rating, JSON]
        if self.check(string):
            return
        
        wrk_dict = self.root
        for i in string:
            if i in wrk_dict[0]:
                wrk_dict = wrk_dict[0][i]
                if len(wrk_dict[1]) == 10:
                    if rating > wrk_dict[2]:
                        wrk_dict[1].pop(wrk_dict[2])
                        wrk_dict[1][rating] = [string, json]                    
                else:
                    wrk_dict[1][rating] = [string, json]
                    
                wrk_dict[2] = min(wrk_dict[1].keys())
            else:
                wrk_dict[0][i] = [{}, {rating: [string, json]}, rating]                
                wrk_dict = wrk_dict[0][i]
        wrk_dict.append(True)
     
    def check(self, string):
        wrk_dict = self.root
        for i in string:
            if i in wrk_dict[0]:
                wrk_dict = wrk_dict[0][i]
            else:
                return False
        if len(wrk_dict) != 3:
            return True
        return False
    
    def get_top(self, string):
        wrk_dict = self.root
        for i in string:
            if i in wrk_dict[0]:
                wrk_dict = wrk_dict[0][i]
            else:
                return False
        top_10 = []
        for k in reversed(wrk_dict[1]):
            top_10.append(wrk_dict[1][k])
            
pr_tree = PrefixTree()
def init_prefix_tree(filename):
    #TODO в данном методе загружаем данные из файла. Предположим вормат файла "Строка, чтобы положить в дерево" \t "json значение для ноды" \t частота встречаемости
    with open(filename) as file:
        for line in file:
            string, json, rating = line.split()
            pr_tree.add(string, json, rating)
        
@app.route("/get_sudgest/<string>", methods=['GET', 'POST'])
def return_sudgest(string):
    #TODO по запросу string вернуть json, c топ-10 саджестами, и значениями из нод
    json = jsonify(pr_tree.get_top(string))
    return json



@app.route("/")
def hello():
    #TODO должна возвращаться инструкция по работе с сервером
    hello = "Загружаем данные из файла. Предположим вормат файла Строка, чтобы положить в дерево json значение для ноды частота встречаемости. Составляется префиксное дерево и по адресу с саджестом /get_sudgest/саджест показывается топ 10 запросов"
    return hello

if __name__ == "__main__":
    app.run()
