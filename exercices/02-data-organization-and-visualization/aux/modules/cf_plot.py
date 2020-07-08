import matplotlib as mpl
import matplotlib.pyplot as plt
import cf_data
import cf_radar


colors = [color['color'] for color in list(mpl.rcParams['axes.prop_cycle'])]


def emptyPlot(figure, gridSpec):
    axes = figure.add_subplot(gridSpec[0, 0])
    axes.set_title("Empty Plot", fontsize = 20)
    gridSpec.tight_layout(figure)

    return axes


def hideAxes(axes):
    axes.set_frame_on(False)
    
    [n.set_visible(False) for n in axes.get_xticklabels() + axes.get_yticklabels()]
    [n.set_visible(False) for n in axes.get_xticklines() + axes.get_yticklines()]


def inverseLossesByManufacturer(figure, gridSpec = None, pdData = None, axes = None, legend = True, labels = True):
    if not axes:
        axes = figure.add_subplot(gridSpec[0, 0])
    
    manufacturerIds = cf_data.getManufacturerIds(pdData)
    
    lossMins  = pdData.groupby("manufacturer")["losses"].min().values
    lossMeans = pdData.groupby("manufacturer")["losses"].mean().values
    lossMaxs  = pdData.groupby("manufacturer")["losses"].max().values
    
    minColor  = colors[0]
    meanColor = colors[3]
    maxColor  = colors[2]

    barMins  = axes.bar(manufacturerIds, lossMins,  width = 0.5, align = "center", color = minColor,  alpha = 0.7)
    barMeans = axes.bar(manufacturerIds, lossMeans, width = 0.5, align = "center", color = meanColor, alpha = 0.7, bottom = lossMins)
    barMaxs  = axes.bar(manufacturerIds, lossMaxs,  width = 0.5, align = "center", color = maxColor,  alpha = 0.7, bottom = lossMeans + lossMins)
    
    axes.set_title("Inverse Losses by Manufacturers - Normalized Data", fontsize = 20)

    if labels:
        axes.set_xticks(range(0, 13))
        axes.set_xticklabels(cf_data.getManufacturerLabels(pdData))
        axes.set_xlabel("Manufacturer",   fontsize = 16)
        axes.set_ylabel("Inverse Losses", fontsize = 16)
    else:
        axes.set_xticklabels([])
        axes.set_yticklabels([])

    if legend:
        axes.legend([barMins, barMeans, barMaxs], ["Min", "Mean", "Max"], loc = 2)
    
    if gridSpec:
        gridSpec.tight_layout(figure)
    
    return axes


def inverseRiskinessAndLossesCombinedByManufacturer(figure, gridSpec = None, pdData = None, axes = None, xLabel = True, rotateTicks = False):
    if not axes:
        axes = figure.add_subplot(gridSpec[0, 0])
    
    if rotateTicks:
        plt.xticks(rotation = 70)
    
    manufacturerIds = cf_data.getManufacturerIds(pdData)
    
    riskMins  = pdData.groupby("manufacturer")["riskiness"].min().values
    riskMeans = pdData.groupby("manufacturer")["riskiness"].mean().values
    riskMaxs  = pdData.groupby("manufacturer")["riskiness"].max().values
    
    lossMins  = pdData.groupby("manufacturer")["losses"].min().values
    lossMeans = pdData.groupby("manufacturer")["losses"].mean().values
    lossMaxs  = pdData.groupby("manufacturer")["losses"].max().values
    
    mins = riskMins + lossMins
    means = riskMeans + lossMeans
    maxs = riskMaxs + lossMaxs
    
    minColor  = colors[0]
    meanColor = colors[3]
    maxColor  = colors[2]
    
    barMins  = axes.bar(manufacturerIds, mins,  align = "center", color = minColor,  alpha = 0.7)
    barMeans = axes.bar(manufacturerIds, means, align = "center", color = meanColor, alpha = 0.7, bottom = mins)
    barMaxs  = axes.bar(manufacturerIds, maxs,  align = "center", color = maxColor,  alpha = 0.7, bottom = means + mins)
    
    axes.set_title("Inverse Riskiness and Losses Combined by Manufacturers - Normalized Data", fontsize = 20)
    axes.set_xticks(range(0, 13))
    axes.set_xticklabels(cf_data.getManufacturerLabels(pdData))

    if xLabel:
        axes.set_xlabel("Manufacturer", fontsize = 16)
    
    axes.set_ylabel("Inverse Riskiness", fontsize = 16)
    axes.legend([barMins, barMeans, barMaxs], ["Min", "Mean", "Max"], loc = 2)
    
    if gridSpec:
        gridSpec.tight_layout(figure)
    
    return axes


def inverseRiskinessByManufacturer(figure, gridSpec = None, pdData = None, axes = None, legend = True, labels = True):
    if not axes:
        axes = figure.add_subplot(gridSpec[0, 0])
    
    manufacturerIds = cf_data.getManufacturerIds(pdData)

    riskMins  = pdData.groupby("manufacturer")["riskiness"].min().values
    riskMeans = pdData.groupby("manufacturer")["riskiness"].mean().values
    riskMaxs  = pdData.groupby("manufacturer")["riskiness"].max().values

    minColor  = colors[0]
    meanColor = colors[3]
    maxColor  = colors[2]

    barMins  = axes.bar(manufacturerIds, riskMins,  width = 0.5, align = "center", color = minColor,  alpha = 0.7)
    barMeans = axes.bar(manufacturerIds, riskMeans, width = 0.5, align = "center", color = meanColor, alpha = 0.7, bottom = riskMins)
    barMaxs  = axes.bar(manufacturerIds, riskMaxs,  width = 0.5, align = "center", color = maxColor,  alpha = 0.7, bottom = riskMeans + riskMins)
    
    axes.set_title(("Inverse Riskiness by Manufacturers - Normalized Data"), fontsize = 20)

    if labels:
        axes.set_xticks(range(0, 13))
        axes.set_xticklabels(cf_data.getManufacturerLabels(pdData))
        axes.set_xlabel("Manufacturer", fontsize = 16)
        axes.set_ylabel("Inverse Riskiness", fontsize = 16)
    else:
        axes.set_xticklabels([])
        axes.set_yticklabels([])

    if legend:
        axes.legend([barMins, barMeans, barMaxs], ["Min", "Mean", "Max"], loc = 2)
    
    if gridSpec:
        gridSpec.tight_layout(figure)
    
    return axes


def mpgByManufacturer(figure, gridSpec = None, pdData = None, axes = None):
    if not axes:
        axes = figure.add_subplot(gridSpec[0, 0])
    
    data = cf_data.getNumericData(pdData)
    
    axes.set_title("MPG by Manufacturers", fontsize = 20)
    axes.scatter(data["manufacturer"], data["highway mpg"], c = colors[3], s = 500, alpha = 0.4)
    axes.scatter(data["manufacturer"], data["city mpg"],    c = colors[0], s = 500, alpha = 0.4)
    axes.set_xticks(range(0, 13))
    axes.set_xticklabels(cf_data.getManufacturerLabels(pdData))
    axes.set_xlabel("Manufacturer", fontsize = 16)
    axes.set_ylabel("MPG",          fontsize = 16)

    patchCity    = mpl.patches.Patch(color = colors[0], alpha = 0.7, label = "City")
    patchHighway = mpl.patches.Patch(color = colors[3], alpha = 0.7, label = "Highway")
    axes.legend(handles = [patchCity, patchHighway], loc = 2)
    
    if gridSpec:
        gridSpec.tight_layout(figure)
    
    return axes


def priceByManufacturer(figure, gridSpec = None, pdData = None, axes = None):
    if not axes:
        axes = figure.add_subplot(gridSpec[0, 0])

    minData  = pdData.groupby("manufacturer", sort = True)["price"].min()
    meanData = pdData.groupby("manufacturer", sort = True)["price"].mean()
    maxData  = pdData.groupby("manufacturer", sort = True)["price"].max()
    make_ids = cf_data.getManufacturerIds(pdData)

    axes.set_title("Price by Manufacturers", fontsize = 20)
    axes.plot(make_ids, minData,  c = colors[2], linewidth = 4, alpha = 0.7)
    axes.plot(make_ids, meanData, c = colors[3], linewidth = 4, alpha = 0.7)
    axes.plot(make_ids, maxData,  c = colors[4], linewidth = 4, alpha = 0.7)
    axes.set_xticks(range(-1, 13))
    axes.set_xticklabels([" "] + cf_data.getManufacturerLabels(pdData))
    axes.set_xlabel("Manufacturer", fontsize = 16)
    axes.set_ylabel("Price",        fontsize = 16)

    patchLow =  mpl.patches.Patch(color = colors[2], alpha = 0.7, label = "Low")
    patchMean = mpl.patches.Patch(color = colors[3], alpha = 0.7, label = "Mean")
    patchHigh = mpl.patches.Patch(color = colors[4], alpha = 0.7, label = "High")
    axes.legend(handles = [patchHigh, patchMean, patchLow], loc = 2)
    
    if gridSpec:
        gridSpec.tight_layout(figure)

    return axes


##################################################



def getManufacturerAutoRadarPlot(
    figure, 
    gs = None, 
    pddata = None, 
    title_axes = None, 
    legend_axes = None, 
    inner_axes = None, 
    geometry = None, rotate=True):
    
    radar_colors = [1, 2, 0]
    min_data = pddata.groupby("manufacturer", sort=True).min()
    max_data = pddata.groupby("manufacturer", sort=True).max()
    mean_data = pddata.groupby("manufacturer", sort=True).mean()
    projection = cf_radar.RadarAxes(spoke_count=len(mean_data.columns))
    
    if geometry:
        (row_num, col_num) = geometry
    else:
        (row_num, col_num) = gs.get_geometry()
    
    if not inner_axes:
        subplots = [x for x in gs]
        inner_axes = []

        for(i, m) in enumerate(subplots[col_num:]):
            if i % col_num != 0:
                inner_axes.append(plt.subplot(m, projection = projection))
    
    if not title_axes:
        title_axes = figure.add_subplot(gs[0, :])
    
    if legend_axes is None:
        legend_axes = figure.add_subplot(gs[0:, 0])
    
    if legend_axes != False:
        max_patch = mpl.patches.Patch(color = colors[radar_colors[0]], alpha = 0.7, label = "Max")
        mean_patch = mpl.patches.Patch(color = colors[radar_colors[1]], alpha = 0.7, label = "Mean")
        min_patch = mpl.patches.Patch(color = colors[radar_colors[2]], alpha = 0.7, label="Min")
        legend_axes.legend(handles=[max_patch, mean_patch, min_patch], loc = 10)
        hideAxes(legend_axes)
    
    title_axes.set_title("Plot Radar with 7 Dimensions for 12 Manufacturers", fontsize = 16)
    hideAxes(title_axes)
    
    for i, manufacturer in enumerate(manufacturer.getManufacturerNames(pddata)):
        axes = inner_axes[i]
        axes.set_title(
            manufacturer.title(), 
            size = 'large', 
            position=(0.5, 1.2), 
            horizontalalignment = 'center', 
            verticalalignment = 'center')
        
        for(color, alpha, data) in zip(radar_colors, [0.2, 0.3, 0.4], [max_data, mean_data, min_data]):
            axes.fill(
                axes.radar_theta,
                data.loc[manufacturer], 
                color = colors[color], 
                alpha = alpha)
            
            axes.plot(axes.radar_theta, data.loc[manufacturer], color=colors[color])
        
        axes.set_varlabels([x.replace(" ", "\n") for x in mean_data.columns])
        axes.set_yticklabels([])
    
    if gs:
        gs.tight_layout(figure)
    
    return [title_axes, legend_axes, inner_axes]
