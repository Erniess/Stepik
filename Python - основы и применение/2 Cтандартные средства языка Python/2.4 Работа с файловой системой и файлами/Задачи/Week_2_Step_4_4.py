# Вам дается текстовый файл, содержащий некоторое количество непустых строк.
# На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.

filename = 'dataset_24465_4.txt'
with open(filename) as f, open('newfile.txt', 'w') as out_file:
    out_file.write('\n'.join(reversed([i.rstrip() for i in f.readlines()])))