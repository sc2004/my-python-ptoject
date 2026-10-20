"""
演示编解码
    编码:'字符串'.encode('utf-8')
    解码:'字节流'.decode('utf-8')
    乱码原因:编码和解码的编码方式不一致导致
    英文，数字，特殊符号只占1个字节，中文gbk占2个字节，utf-8占3个字节，
    b''对中文编码，会报错
"""
s2 = '你好1'
print(s2.encode())
print(s2.encode('utf-8'))
print(s2.encode('gbk'))

bys = b'\xe4\xbd\xa0\xe5\xa5\xbd1'
print(bys.decode('utf-8'))
print(bys.decode('gbk'))
