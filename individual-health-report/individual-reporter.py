import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bidi.algorithm import get_display
import arabic_reshaper
from colour import Color
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from matplotlib import font_manager
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
import matplotlib.image as image
from matplotlib.offsetbox import OffsetImage,AnchoredOffsetbox
import warnings

all_them_years = [1395, 1396, 1397, 1401]
xyagut = font_manager.FontProperties(fname='/Users/HQ/Downloads/X/X Yagut.ttf')
logo = mpimg.imread('logo.jpg')
now = pd.read_excel('1401.xlsx')
now = now.fillna(0.0)
positions = [[0, 0], [0, 1],
             [1, 0], [1, 1],
             [2, 0], [2, 1],
             [3, 0], [3, 1],
             [4, 0], [4, 1],
             [5, 0], [5, 1],
             [6, 0], [6, 1],
             [7, 0], [7, 1]]

units = {}
units['d3']     = 'ng/ml'
units['sgpt']   = 'Iu/l'
units['sgot']   = 'Iu/l'
units['ldl']    = 'mg/dl'
units['hdl']    = 'mg/dl'
units['tgc']    = 'mg/dl'
units['chol']   = 'mg/dl'
units['ur.a']   = 'mg/dl'
units['cr']     = 'mg/dl'
units['urea']   = 'mg/dl'
units['fbs']    = 'mg/dl'
units['A1c']    = 'g/dl'
units['hb']    = 'g/dl'
units['bmi']    = ''

ranges = {}
ranges['d3']    = [121, 100, 100, 30, 10, 0]
ranges['sgpt']  = [200, 100, 100, 40, 0, 0]
ranges['sgot']  = [200, 100, 100, 40, 0, 0]
ranges['ldl']   = [200, 160, 130, 0, 0, 0]
ranges['hdl']   = [100, 100, 90, 35, 30, 0]
ranges['tgc']   = [1200, 190, 180, 0, 0, 0]
ranges['chol']  = [300, 250, 190, 130, 0, 0]
ranges['ur.a']  = [10, 8.5, 8.2, 3.6, 2, 2]
ranges['cr']    = [4.2, 1.4, 0.6, 0, 0, 0]
ranges['urea']  = [60, 45, 17, 15, 10, 10]
ranges['fbs']   = [500, 126, 110, 70, 50, 50]
ranges['A1c']   = [22, 10, 8, 6, 5.9, 0]
ranges['hb']   = [22, 10, 8, 6, 5.9, 0]
ranges['bmi']   = [50, 10, 10, 10, 10, 10]

titles = {}
titles['d3']     = get_display(arabic_reshaper.reshape('ویتامین D3'))
titles['sgpt']   = get_display(arabic_reshaper.reshape('آنزیم کبدی SGPT'))
titles['sgot']   = get_display(arabic_reshaper.reshape('آنزیم کبدی SGOT'))
titles['ldl']    = get_display(arabic_reshaper.reshape('مقدار چربی مضر برای قلب (LDL)'))
titles['hdl']    = get_display(arabic_reshaper.reshape('مقدار چربی مفید برای قلب (HDL)'))
titles['tgc']    = get_display(arabic_reshaper.reshape('تری گلیسرید خون (چربی نشاسته)'))
titles['chol']   = get_display(arabic_reshaper.reshape('میزان چربی خون (کلسترول)'))
titles['ur.a']   = get_display(arabic_reshaper.reshape('اسید اوریک خون'))
titles['cr']     = get_display(arabic_reshaper.reshape('کراتینین خون'))
titles['urea']   = get_display(arabic_reshaper.reshape('اوره خون'))
titles['fbs']    = get_display(arabic_reshaper.reshape('قند خون ناشتا'))
titles['A1c']    = get_display(arabic_reshaper.reshape('معدل قند سه‌ماهه'))
titles['hb']    = get_display(arabic_reshaper.reshape('غلظت هموگلوبین خون (Hgb)'))
titles['bmi']    = get_display(arabic_reshaper.reshape('شاخص توده بدنی (BMI)'))

im = image.imread('/Users/HQ/Library/Mobile Documents/com~apple~CloudDocs/Documents/Family/Dads-Jobs/water-and-sewage/logo.jpg')
def place_image(im, loc=2, bbox_to_anchor=(50,1300), ax=None, zoom=1, **kw):
    if ax==None: ax=plt.gca()
    imagebox = OffsetImage(im, zoom=zoom*0.72)
    ab = AnchoredOffsetbox(loc=2, bbox_to_anchor=bbox_to_anchor, child=imagebox, frameon=False, **kw)
    ax.add_artist(ab)

for i in range(0,296):
# for i in range(0,5):
    figname = now.iloc[i][4] + ' ' + now.iloc[i][3] #str(i+1)
    old_full_name = ''
    print('processing %s'%(figname))
    for old_report in sorted(os.listdir('/Users/HQ/Library/Mobile Documents/com~apple~CloudDocs/Documents/Family/Dads-Jobs/water-and-sewage/old/')):
        if not old_report.startswith('.') and old_report.endswith('.xlsx') and not old_report.startswith('~'):
            old_data = pd.read_excel('old/%s'%(old_report), 'نتایج آزمایش')
            old_name = pd.read_excel('old/%s'%(old_report), 'نمودار')
            old_first_name, old_last_name = old_name.iloc[0][4].split()[0], old_name.iloc[0][4].split()[1]
            if now.iloc[i][4] == old_first_name and\
                (now.iloc[i][3] == old_last_name or now.iloc[i][3] in old_last_name or old_last_name in now.iloc[i][3]):
                fullname_old = old_first_name + old_last_name
                fullname_new = now.iloc[i][4] + now.iloc[i][3]
                match_found = True
                old_full_name = get_display(arabic_reshaper.reshape(old_first_name + ' ' + old_last_name))

                metrics = {}
                metrics['hb'] = [j for j in old_data['Hgb']] + [now['HB'][i]]
                metrics['fbs'] = [j for j in old_data['FBS']] + [now['FBS'][i]]
                metrics['A1c'] = [now['HbA1C'][i]]
                metrics['cr'] = [j for j in old_data['Cr']] + [now['Cr'][i]]
                metrics['urea'] = [j for j in old_data['Urea']] + [now['Urea'][i]]
                metrics['ur.a'] = [j for j in old_data['Ur. A']] + [now['Uric Acid'][i]]
                metrics['chol'] = [j for j in old_data['Chol']] + [now['CHOL'][i]]
                metrics['tgc'] = [j for j in old_data['TGC']] + [now['TG'][i]]
                metrics['hdl'] = [j for j in old_data['HDL']] + [now['HDL'][i]]
                metrics['ldl'] = [j for j in old_data['LDL']] + [now['LDL'][i]]
                metrics['sgot'] = [j for j in old_data['SGOT']] + [now['AST'][i]]
                metrics['sgpt'] = [j for j in old_data['SGPT']] + [now['ALT'][i]]
                metrics['d3'] = [j for j in old_data['D3']] + [now['Vit D3'][i]]
                metrics['bmi'] = [round(old_name.iloc[1][9], 1)] + [round(now['BMI'][i], 1)]
                
                break
            else:
                match_found = False
    if not match_found:
        metrics = {}
        metrics['hb']   = [now['HB'][i]]
        metrics['fbs']  = [now['FBS'][i]]
        metrics['A1c']  = [now['HbA1C'][i]]
        metrics['cr']   = [now['Cr'][i]]
        metrics['urea'] = [now['Urea'][i]]
        metrics['ur.a'] = [now['Uric Acid'][i]]
        metrics['chol'] = [now['CHOL'][i]]
        metrics['tgc']  = [now['TG'][i]]
        metrics['hdl']  = [now['HDL'][i]]
        metrics['ldl']  = [now['LDL'][i]]
        metrics['sgot'] = [now['AST'][i]]
        metrics['sgpt'] = [now['ALT'][i]]
        metrics['d3']   = [now['FBS'][i]]
        metrics['bmi']  = [round(now['BMI'][i], 1)]

    fig, axes = plt.subplots(8, 2, sharex=True, sharey=False, figsize=(10,20))

    report1 = get_display(arabic_reshaper.reshape('نام و نام خانوادگی: %s %s'%(now.iloc[i][4], now.iloc[i][3])))
    report2 = get_display(arabic_reshaper.reshape('وضعیت عمومی: قد: %d سانتی‌متر، وزن: %d کیلوگرم، BMI:‌ %d'%(now['قد (CM)'][i], now['وزن(Kg)'][i], round(now['BMI'][i], 1))))
    report3 = get_display(arabic_reshaper.reshape('فشار خون: بالا: %d پایین: %d '%(now[' Bp Systolic'][i], now['Bp Diastolic'][i])))
    report4 = get_display(arabic_reshaper.reshape('نتیجه معاینه تخصصی: %s'%(now['توضیحات مربوط به ارزیابی نهایی'][i])))
    report5 = get_display(arabic_reshaper.reshape('در نمودارهای زیر رنگ سبز طبیعی، رنگ زرد در معرض خطر و نیاز به مراقبت و رنگ قرمز ناحیه خطرناک می‌باشد.'))

    counter = 2
    for i in metrics:
        years = all_them_years[-len(metrics[i]):]
        axes[positions[counter][0], positions[counter][1]].plot(years, metrics[i], marker='o', color='blue', markersize=10)
        axes[positions[counter][0], positions[counter][1]].set_ylim(ranges[i][-1],ranges[i][0])
        axes[positions[counter][0], positions[counter][1]].set_xlim(1394, 1402)
        axes[positions[counter][0], positions[counter][1]].set_title(titles[i], fontproperties=xyagut)
        axes[positions[counter][0], positions[counter][1]].set_ylabel(units[i])

        background = image.imread('/Users/HQ/Library/Mobile Documents/com~apple~CloudDocs/Documents/Family/Dads-Jobs/water-and-sewage/gradients/%s.png'%(i))
        axes[positions[counter][0], positions[counter][1]].imshow(background, aspect='auto', extent=[1394, 1402, ranges[i][-1],ranges[i][0]])

        for x, y, s in zip(years, metrics[i], metrics[i]):
            offset = (ranges[i][0] - ranges[i][-1])*.04
            axes[positions[counter][0], positions[counter][1]].text(x, y+offset, s, size=12)
        counter += 1

    axes[positions[0][0], positions[0][1]].axis('off')
    axes[positions[1][0], positions[1][1]].axis('off')
    axes[positions[-1][0], positions[-1][1]].set_xlabel(get_display(arabic_reshaper.reshape('سال')), fontproperties=xyagut, size=15)
    axes[positions[-2][0], positions[-2][1]].set_xlabel(get_display(arabic_reshaper.reshape('سال')), fontproperties=xyagut, size=15)
    
    warnings.filterwarnings("ignore")
    fig.text(1.0, 0.98, report1, size=15, ha='right', fontproperties=xyagut)
    fig.text(1.0, 0.96, report2, size=15, ha='right', fontproperties=xyagut)
    fig.text(1.0, 0.94, report3, size=15, ha='right', fontproperties=xyagut)
    fig.text(1.0, 0.92, report4, size=15, ha='right', fontproperties=xyagut)
    fig.text(1.0, 0.90, report5, size=15, ha='right', fontproperties=xyagut)
    fig.tight_layout()
    place_image(im, loc=2, bbox_to_anchor=(50,1400), ax=axes[2][0], pad=0, zoom=0.2)
    plt.draw()
    plt.savefig(figname+'.pdf', dpi=300, bbox_inches='tight')
    # plt.show()
    plt.clf()
