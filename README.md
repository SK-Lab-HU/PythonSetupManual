# Python セットアップマニュアル(Windows)
- [Python セットアップマニュアル(Windows)](#python-セットアップマニュアルwindows)
  - [Pythonのインストール](#pythonのインストール)
  - [VSCODEのダウンロード\&インストール](#vscodeのダウンロードインストール)
- [Pythonの実行](#pythonの実行)
- [基本構文](#基本構文)
  - [ターミナルに出力](#ターミナルに出力)
  - [変数に代入](#変数に代入)
  - [四則演算](#四則演算)
  - [条件構文](#条件構文)
  - [ループ構文](#ループ構文)
  - [関数](#関数)
  - [クラス](#クラス)
- [グラフの描画](#グラフの描画)
  - [散布図の作成](#散布図の作成)

## Pythonのインストール

1. Python公式ページにアクセスする。([Python公式サイト](https://www.python.org/downloads/))

2. 黄色いDownload PythonボタンをクリックしてPythonをダウンロードする。

![](images/python_org.png)

3. ダウンロード完了後、ファイルを開くと以下のような画面になる。この時、Add python..exe to PATHにチェックが入っていることを確認する。Install Nowを押すとインストールが始まるのでしばらく待つ。

![](images/python_install.png)

4. Setup was successful と表示されたらPythonのインストールは完了。

## VSCODEのダウンロード&インストール

1. 公式ページからwindows用のvscodeをダウンロード、インストールする。([VSCODEダウンロードページ](https://code.visualstudio.com/download))

2. Windows用をダウンロードする。

3. ダウンロードしたファイルを開き、インストールする。

# Pythonの実行

1. 上記でダウンロードしたVSCODEを開くと、以下のようなスタートアップ画面が表示される。

![](images/vscode_startup.png)

2. Open folder をクリックして、VSCODEで開くフォルダを選択する。(慣れるまではDesktopを選択するとわかりやすい。)

![](images/openfolder.png)

3. フォルダを選択した後は、画面左上の新規ファイル作成ボタンを押す。(画像では４つのアイコンのうち一番左)

![](images/newfile.png)

4. 以下のようにpythonファイル（拡張子が.pyのファイル) を作成する。名前は任意。

![](images/newfile2.png)

5. 左側の四角が４つあるアイコンを選び、拡張機能をインストールする。（初回のみ）pythonと検索すると一番上に出てくるものを選択して、installをクリックするだけ。（30秒程度で終了する。）

![](images/extention.png)

6. 以下のようにpythonコードを書き、右上の三角の再生ボタンを押してコードを実行する。

![](images/pythoncode.png)

下部に出てくるのターミナル（黒い画面）に12345と表示されたら成功。

![](images/pythonterminal.png)


# 基本構文

## ターミナルに出力

ターミナルに結果を出力する際に使用する。
Matlabのdisplayに値する。

```Python
print(1)
```

## 変数に代入

Pythonは動的型付なのでデータタイプの指定は不要。（明示的に指定することはできる）

```Python
#整数型
x1 = 10
#浮動小数点数
x2 = 10.203
#文字列型
s1 = "string"
s2 = "20.24"
#ブーリアン型
b1 = True
b2 = False
#配列
l1 = [1,2,3]
#辞書
d1 = {1:"1の値",2,"2の値"}

###型アノテーションを明示的に書く場合。
# 整数型
x1: int = 10
# 浮動小数点数
x2: float = 10.203
# 文字列型
s1: str = "string"
s2: str = "20.24"
# ブーリアン型
b1: bool = True
b2: bool = False
# 配列
l1: list[int] = [1,2,3]
# 辞書
d1: dict[int,str] = {1:"1の値",2:"2の値"}
```
## 四則演算

```Python
# 足し算
x1 = 5 
x2 = 4 
x3 = x1 + x2

### 9 になる。
print(x3) 

# 引き算
x1 = 5 
x2 = 4 
x3 = x2 - x1

### -1 になる。
print(x3)

# 掛け算
x1 = 5 
x2 = 4 
x3 = x1 * x2

### 20 になる。
print(x3)

# 割り算
x1 = 20
x2 = 4 
x3 = x1 / x2

### 5 になる。
print(x3)


# Mod
x1 = 5
x2 = 4 
x3 = x1 % x2

### 1 になる。
print(x3)

```


## 条件構文
ifなどの構文

```Python
a = 1 
b = 2

# 以下の場合は　trueがプリントされる。
if a + b > 2:
    print("true")
elif a + b == 2:
    print("a+b=2")
else:
    print("false")
```

## ループ構文

```Python
#0から99をターミナルに出力(iは任意の変数名)
for i in range(100):
    print(i)

#ループで配列の値を取り出す。
#以下の場合は1から7までの整数が表示される。
arr = [1,2,3,4,5,6,7]
for i in arr:
    print(i)

#while ループ
#True部分がFalseになるまで実行される。
#以下の場合は無限に1を出力。
while True:
    print(1)

#以下の場合は1から7までprintされてループが終了。
# += の記号はvalue = value +　1 と同義
value = 1
while value < 8:
    print(value)
    value += 1
```

## 関数

```Python

#入力値に1を足して返す関数。
def func1(input1: int) -> int:
    return input1 + 1

#上記は以下のように省略して書くことができる。
def func1(input1):
    return input1 + 1
```

## クラス

OOPでpythonを書く場合に使用。(発展版)

```Python

class Cell:
    def __init__(self) -> None:
        self.cell_id = 0
        self.cell_length = 0

    def get_cell_id(self) -> int:
        return self.cell_id

    def get_cell_length(self) -> int:
        return self.cell_length

    def set_cell_id(self, cell_id: int) -> None:
        self.cell_id = cell_id

    def set_cell_length(self, cell_length: int) -> None:
        self.cell_length = cell_length

    def __repr__(self) -> str:
        return f"Cell {self.cell_id} with length {self.cell_length}"

```


# グラフの描画

pythonのグラフ描画モジュール'matplotlib'をインストールする。(初回のみ)

公式ドキュメントは以下
[matplotlib公式ドキュメント](https://matplotlib.org/stable/plot_types/index.html)

ターミナルで以下コマンドを実行。

```bash
pip install matplotlib numpy pandas
```

もし失敗したら、pipをpip3に変えて実行する。

```bash
pip3 install matplotlib numpy pandas
```

## 散布図の作成

以下のコードをコピー&ペーストして実行すると下図がpythonファイルと同じディレクトリに出力される。

```Python
import matplotlib.pyplot as plt
import numpy as np

# 以下は　[10, 11, 12, 13, 14, 15, 16, 17, 18, 19] と同じ
time:list[int] = [i for i in range(10,20)]

# 以下は適当な指数関数にtimeを代入したもの
OD600:list[float] = [np.exp(i*0.12) for i in time]


fig = plt.figure(figsize=[5,5])
plt.scatter(time, OD600,s=30, c='tab:blue', marker='o', label='sample1')
plt.xlabel("time(h)")
plt.ylabel("OD600(-)")
plt.grid()
plt.legend()

fig.savefig("OD600.png", dpi=500)

```

実行結果

![](images/OD600.png)

# ボックスプロット

以下スクリプトで、複数系列のボックスプロットを生成できる。
それぞれのデータはリスト型で定義する。

```Python
import numpy as np 
import matplotlib.pyplot as plt

data1,data2,data3,data4,data5 = [np.random.normal(np.random.randint(3,15), np.random.randint(1,10), np.random.randint(1000,1500)) for i in range(5)]

fig = plt.figure(figsize=[8,6])

# ボックスプロットを作成
plt.boxplot([data1,data2,data3,data4,data5],sym="")

# データポイントをプロット（外れ値を含む）
for i, data in enumerate([data1,data2,data3,data4,data5], start=1):
    x = np.random.normal(i, 0.04, size=len(data))  # データポイントのX座標を少しずらす
    plt.plot(x, data, 'o', alpha=0.1)  

# 各プロットにラベルを追加する
plt.xticks([1, 2, 3, 4,5], [f'series1 (n={len(data1)})', f'series2 (n={len(data2)})', f'series3 (n={len(data3)})', f'series4 (n={len(data4)})', f'series5 (n={len(data5)})'])

# グラフを表示
plt.xlabel('Exposure time (min)')
plt.ylabel(r'$cell\:length\: (px)$')
plt.grid(True)

fig.savefig("cell_lengths.png",dpi = 500)
```

実行結果


![](images/cell_lengths.png)
