
def p(text, pre="info"):
    """Create log output"""
    x = ""
    if pre:
        x += f"[{pre.upper()}] "
    x += text

class Demo:

    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return dict(
            name=self.name
        )