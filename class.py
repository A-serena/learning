# クラスの練習

# 最初にクラスを定義する
class Car:
    def run(self):
        print("RUN")

    def stop(self):
        print("STOP")

class Cat:
    family = '猫'  # クラス変数なので self は不要
    
    def say(self):
        print("meow")
    
    def growl(self):
        print("fuu")
    
    # なんでこれが一番最後に定義されてるんだろう 別にここでは関係ない？
    def __init__(self,nam): # これは初期化メソッド らしい
        self.name = nam # インスタンス変数なので self は必要
        #クラス内での変数へのアクセスなので self.変数名 ←この変数はなに変数？
#どれがどれを指してるかを見るために変数名変えてたら nam と nam が同じだったので記録用にそのままにしてる


test = Car() 
"""
Carクラスを変数testに代入して、クラスのインスタンス(実体)を生成 これでクラスは実体化される
クラスという抽象的な定義をもとに1つの実体を作る操作
"""
test.run() #run関数を呼び出して処理をさせる
test.stop() #stop関数を呼び出して処理をさせる


neko = Cat(1) 
"""
23行目と同じことをしたいけど
TypeError: __init__() missing 1 required positional argument: 'name'
が出る → 数字なり文字列なり入れたら通った まあそりゃ通るだろうけど
(self,nam) だから1つ引数を与えなくちゃいけないのは分かるけど、
本来どんな値を入れてほしいのかわからない name だから猫の名前？
"""
neko.say()
neko.growl()

#test.say() # test(Car) の中には say 関数がないので AttributeError: 'Car' object has no attribute 'say'


"""
以下シェルに投げる時のそれ

Cat.family
tama = Cat('たま')
tama.family
tama.name

dora = Cat('ドラえもん')
dora.family
dora.name
"""