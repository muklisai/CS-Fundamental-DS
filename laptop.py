laptop=5000000
uang_sekarang=3000000
tabungan_A=1000000
tabungan_B=1000000
suku_bunga=0.06
lama_menabung=7

saldo_A=tabungan_A+(tabungan_A*suku_bunga*lama_menabung)
saldo_B=tabungan_B*(1+suku_bunga)**lama_menabung

total_uang=uang_sekarang+saldo_A+saldo_B

if total_uang >= laptop:
  print('Total uang Andi: Rp',round(total_uang),', cukup untuk membeli laptop')
else:
  print('Total uang Andi: Rp',round(total_uang),' tidak cukup untuk membeli laptop')