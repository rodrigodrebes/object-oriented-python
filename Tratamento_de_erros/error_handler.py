from meu_erro import MeuErroPersonalizado


def error_handler_method(error):
    if isinstance(error, MeuErroPersonalizado):
        print("tratar meu erro personalizado")
        return
        
    if isinstance(error, ZeroDivisionError):
        print("tratar divisão por zero")
        return
    
    if isinstance(error, Exception):
        print("tratar caso geral")
        return