import io

f=open('myopencv.py','rb')
print type(f)

a='b'
result=io.BytesIO(a)
print result.read()
print result.flush()
print result.seek(0)
print result.read()