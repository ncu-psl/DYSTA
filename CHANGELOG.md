# Changelog
## [V1.7](https://github.com/ncu-psl/DYSTA/releases/tag/v1.7)
[Full Changelog](https://github.com/ncu-psl/DYSTA/compare/ncu-psl:v1.6...v1.7)
1. 修正 python boolOp 轉換成 big-O AST 時出現的錯誤
2. 新增 examples/WhileTest.c

## [V1.6](https://github.com/ncu-psl/DYSTA/releases/tag/v1.6)
[Full Changelog](https://github.com/ncu-psl/DYSTA/compare/ncu-psl:v1.5...v1.6)
1. 支援 for node 中 target node 可以放入 tuple/list，例如:
```python
for a, b in k:
    pass
```

2. 支援 for node 中 iter node 可以放入 attribute，可支援的語法以ENBF表示為:
```
ITER ::= CALL | NAME | ATTRIBUTE ;

CALL ::= NAME , '(' , ARGS , ')' ;

ARGS ::= ARG , { ',' , ARG } ;

ARG ::= CALL | NAME | ATTRIBUTE ;

ATTRIBUTE ::= VALUE , '.' , ATTR ;

VALUE ::= NAME | ATTRIBUTE ;

ATTR ::= CALL | NAME ;

NAME ::= id ;

// ::= 表示 左式可被展成右式
// {} 內的元素可以可以省略或重複出現
// | 表示 或
```

3. 修正一些 bugs

## [V1.5](https://github.com/ncu-psl/DYSTA/releases/tag/v1.5)
[Full Changelog](https://github.com/ncu-psl/DYSTA/compare/ncu-psl:v1.4...v1.5)
1. 修正無法分析 a ** b (a的b次方)的語法。

2. 支援各種置於 For statemnt 中 itertation 節點的 function call
```py
import math
def module16():
    result = []
    for i in dir(math):
        if 'exam' in i:
            result.append(i)
    print(result)
```
    這樣的程式經過時間複雜度分析後可以得到
```json
{
    "compilation node": "O(1)",
    "module16": "O(#dir(math))"
}
```
    輸出結果為了避免跟計算dir(math)所需的時間複雜度搞混，
    在 function 前面加一個#表示這個 function output 的 list 或是 tuple 的大小。

    可支援的 function call 以 EBNF 來表示
```
FUNCALL ::= CALL | ATTRIBUTE ;

CALL ::= NAME , '(' , ARGS , ')' ;

ARGS ::= ARG , { ',' , ARG } ;

ARG ::= CALL | NAME | ATTRIBUTE ;

ATTRIBUTE ::= VALUE , '.' , ATTR ;

VALUE ::= NAME | ATTRIBUTE ;

ATTR ::= CALL | NAME ;

NAME ::= id ;

// ::= 表示 左式可被展成右式
// {} 內的元素可以可以省略或重複出現
// | 表示 或
```