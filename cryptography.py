
while True:
    msg = input("メッセージ: ")
    result_cryptography = " "
    i = len(msg) - 1

    while i>=0:
        result_cryptography = result_cryptography + msg[i]
        i = i-1

    print("コード結果: "+ result_cryptography)    
