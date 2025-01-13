try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a/b
# except:
#     print("Ocorreu um problema")
# except Exception as erro:
#     print(f"Problema encontrado: {erro.__class__}")
except (ValueError, TypeError):
    print("Tivemos um problema com os tipos de dados que você digitou.")
except ZeroDivisionError:
    print("Não é possivel dividir um número por zero!")
except KeyboardInterrupt:
    print("O usúario preferiu não informar os dados.")
except Exception as erro:
    print(f"O erro encontrado foi {erro.__cause__}")
else:
    print(f"Resultado: {r:.2f}")
finally:
    print("Encerrando programa! Volte Sempre!")