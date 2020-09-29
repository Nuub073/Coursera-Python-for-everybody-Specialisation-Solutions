text = "X-DSPAM-Confidence:    0.8475";
piece=text.find("0")
fg=text[piece :] 
print(float(fg)) 