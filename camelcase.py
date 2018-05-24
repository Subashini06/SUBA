def camelCase(st):
  output = ''.join(x for x in st.title() if x.isalpha())
  return output[0].upper() + output[1:]
s=str(input("Enter the sting:"))
r=camelCase(s)
print(r)
