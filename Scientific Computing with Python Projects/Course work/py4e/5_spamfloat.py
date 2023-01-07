str = 'X-DSPAM-Confidence:0.8475'
colindex = str.find(":")
figure = float(str[colindex+1:])
print(figure)
