

# def wew(nama,kota):
#     print("Halo nama saya")
#     #print(f"Halo nama saya {nama}, dari {kota}")

# wew("nd","ds")

# for i in range(5):
#     print(i)

abjad = ["a","b","c","d"]

array_dalam_array = [
    ["a","b","c","d"],
    [
        ["a","b","c","d"],
        ["a","b","c","d"],
        ["a","b","c","d"]
    ],
    ["a","b","c","d"],
    ["a","b","c","d"]
]
# for i in abjad:
#     print(i)


a = 0
for i in range(10):
    a += i
    print(a)

print(a)



for huruf in abjad:
    print(huruf)
    
for huruf in array_dalam_array:
    print(huruf)

for huruf in array_dalam_array[1][1]:
    print(huruf)