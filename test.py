response = 'Your one-time PIN is 571321【和多号副号:152****7845】'
code =  response.split('is')[1].strip()[:6]
print(code)