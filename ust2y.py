
import csv, datetime as dt
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, matplotlib.dates as md
plt.rcParams['text.parse_math']=False
rows=list(csv.DictReader(open('/workspace/theidmletter-charts/ust_2026.csv')))
d=[(dt.datetime.strptime(r['Date'],'%m/%d/%Y'),float(r['2 Yr'])) for r in rows if r.get('2 Yr')]
d=sorted(x for x in d if x[0]>=dt.datetime(2026,9,1))
print(d[0], d[-1], max(d,key=lambda x:x[1]), len(d))
NAVY='#0B1F3A'; GOLD='#C9A227'
fig,ax=plt.subplots(figsize=(10,6.2),dpi=150); fig.patch.set_facecolor(NAVY); ax.set_facecolor(NAVY)
x=[a for a,_ in d]; y=[b for _,b in d]
ax.plot(x,y,color=GOLD,lw=2.8)
wk=[p for p in d if p[0]>=dt.datetime(2026,11,13)]
ax.plot([p[0] for p in wk],[p[1] for p in wk],color='white',lw=3.4)
s,e=wk[0],wk[-1]
ax.scatter([s[0],e[0]],[s[1],e[1]],color='white',zorder=5,s=40)
ax.annotate(f"{s[1]:.2f}%  Nov 13",(s[0],s[1]),xytext=(-150,8),textcoords='offset points',color='white',fontsize=13,fontweight='bold')
ax.annotate(f"{e[1]:.2f}%  Nov 20",(e[0],e[1]),xytext=(-60,-48),textcoords='offset points',color='white',fontsize=13,fontweight='bold')
for sp in ax.spines.values(): sp.set_visible(False)
ax.tick_params(colors='#C8CFDA',labelsize=12); ax.grid(axis='y',color='#26385A',lw=0.8)
ax.xaxis.set_major_formatter(md.DateFormatter('%b %d'))
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v,_: f"{v:.2f}%"))
fig.text(0.05,0.93,"Fed hike odds rose. The 2-year yield fell 25bp.",color='white',fontsize=19,fontweight='bold')
fig.text(0.05,0.875,"US 2-year Treasury par yield, daily, Sep 1 - Nov 20, 2026",color=GOLD,fontsize=13)
fig.text(0.05,0.03,"Source: U.S. Treasury par yield curve, 20 Nov 2026. Hike odds: CME FedWatch via CNBC, 20 Nov 2026",color='#C8CFDA',fontsize=10)
fig.text(0.95,0.03,"@TheIDMLetter",color=GOLD,fontsize=10,ha='right',alpha=0.8)
plt.subplots_adjust(left=0.1,right=0.95,top=0.83,bottom=0.12)
fig.savefig('/workspace/theidmletter-charts/ust2y_hike_odds_20261121.png',facecolor=NAVY)
