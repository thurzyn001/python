dis = float(input('Digite uma distância em metros: '))
print(f'''
{dis / 1000:.5f} Km
{dis / 100:.5f} Hm
{dis / 10:.5f} Dam
{dis:.5f} m
{dis * 10:.5f} Dm
{dis * 100:.5f} Cm
{dis * 1000:.5f} Mm
    ''')