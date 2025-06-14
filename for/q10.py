# word = "programming"
# chr_count = {}

# for chr in word:
#     if chr in chr_count:
#         chr_count[chr] +=1
#     else:
#         chr_count[chr] = 1
    
# for chr , count in chr_count.items():
#     print(chr + ':', count)

word = " imran khan"

chr_count = {}

for chr in word:
    if chr in chr_count:
        chr_count[chr] +=1
    else:
        chr_count[chr] = 1
for chr , count in chr_count.items():
    print(chr  + ":", count)