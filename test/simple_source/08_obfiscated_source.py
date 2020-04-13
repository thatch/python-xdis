# Code which has opportunities for obfuscation
mangled_global = "This is a mangled global"
def obfuscated_fn(a):
    msg = "mangled local variable"
    var = lambda a: msg + a # mangled closure
    return mangled_global

assert obfuscated_fn("Another")
