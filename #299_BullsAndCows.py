secret = "1123"
guess = "0111"

bulls = 0
cows = 0
for i in range(len(secret)):
    if secret[i] == guess[i]:
        bulls += 1
        secret = secret[:i] + '-' + secret[i + 1:]
        guess = guess[:i] + '+' + guess[i + 1:]

for i in range(len(secret)):
    if guess[i] in secret:
        cows += 1
        secret = secret.replace(guess[i], '-', 1)
print(f'{bulls}A{cows}B')
