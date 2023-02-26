import os

num_start = input("Entrez le numéro de départ : ")
num_start = int(num_start)

for i, filename in enumerate(os.listdir('.')):
    if os.path.isfile(filename) and filename != os.path.basename(__file__):
        new_filename = f"{num_start + i}_{filename}"
        os.rename(filename, new_filename)
        print(f"{filename} renommé en {new_filename}")

