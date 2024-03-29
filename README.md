# PlotGallary


Please refer to [IPCC Visual Style Guide for Authors](https://www.ipcc.ch/site/assets/uploads/2019/04/IPCC-visual-style-guide.pdf)

This is a collection of fancy plots that is useful in my work!

basic.py: matplotlib configurations for producing publification-level graphs

density_scatter_plot.py: producing color coded density for scatter plot like below:

<p align="center"><img src="gallary/density_scatter_demo.png" width="50%">

hydrograph.ipynb:


Colored boxplot with legend:
```python
fig, ax = plt.subplots()
bp1 = ax.boxplot(data1, positions=[1,4], notch=True, widths=0.35,
                 patch_artist=True, boxprops=dict(facecolor="C0"))
bp2 = ax.boxplot(data2, positions=[2,5], notch=True, widths=0.35,
                 patch_artist=True, boxprops=dict(facecolor="C2"))

ax.legend([bp1["boxes"][0], bp2["boxes"][0]], ['A', 'B'], loc='upper right')

ax.set_xlim(0,6)
plt.show()
```

Radar Graph:
```python
fig,ax= radarChart(np.array(names)[inames],
                    [np.array(cc_meso)[inames],np.array(cc_smap)[inames],np.array(cc_noah)[inames]],
          save=True);
```

Something like this:
<img src="gallary/radar-demo.png">
