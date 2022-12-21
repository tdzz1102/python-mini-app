"""
    https://docs.python.org/ja/3/reference/compound_stmts.html#with
    with文の使い方

"""

# with文を持つ要素はコンテキストマネージャ担当
class Context:
    def __enter__(self):
        print('enter関数が呼ばれた')
    
    def __exit__(self, _type, _value, _traceback):
        print(f"exit関数が呼ばれ, type=f{_type}, value=f{_value}, traceback=f{_traceback}")
        
        # 例外を抑制し、with文の次の文を実行
        return True

with Context() as c:
    raise FileNotFoundError("how are you?")
    print('到達不可領域')

print("fine, thank you!")