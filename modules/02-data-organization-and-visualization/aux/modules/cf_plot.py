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


def inverseLossesByManufacturer(figure, gridSpec = None, pdData = None, axes = None, legend = True, labels = True, rotateTicks = False):
    if not axes:
        axes = figure.add_subplot(gridSpec[0, 0])

    if rotateTicks:
        plt.xticks(rotation = 70)
    
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
    
    axes.set_title("Inverse Losses by Manufacturers\n(Normalized Data)", fontsize = 20)

    if labels:
        axes.set_xticks(range(0, 13))
        axes.set_xticklabels(cf_data.getManufacturerLabels(pdData))
        axes.set_xlabel("Manufacturer",   fontsize = 16)
        axes.set_ylabel("Inverse Losses", fontsize = 16)
    else:
        axes.set_xticklabels([])
        axes.set_yticklabels([])

    if legend:
        axes.legend([barMaxs, barMeans, barMins], ["Max", "Mean", "Min"], loc = 2)
    
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
    
    axes.set_title("Inverse Riskiness and Losses Combined by Manufacturers\n(Normalized Data)", fontsize = 20)
    axes.set_xticks(range(0, 13))
    axes.set_xticklabels(cf_data.getManufacturerLabels(pdData))

    if xLabel:
        axes.set_xlabel("Manufacturer", fontsize = 16)
    
    axes.set_ylabel("Inverse Riskiness", fontsize = 16)
    axes.legend([barMaxs, barMeans, barMins], ["Max", "Mean", "Min"], loc = 2)
    
    if gridSpec:
        gridSpec.tight_layout(figure)
    
    return axes


def inverseRiskinessByManufacturer(figure, gridSpec = None, pdData = None, axes = None, legend = True, labels = True, rotateTicks = False):
    if not axes:
        axes = figure.add_subplot(gridSpec[0, 0])

    if rotateTicks:
        plt.xticks(rotation = 70)
    
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
    
    axes.set_title(("Inverse Riskiness by Manufacturers\n(Normalized Data)"), fontsize = 20)

    if labels:
        axes.set_xticks(range(0, 13))
        axes.set_xticklabels(cf_data.getManufacturerLabels(pdData))
        axes.set_xlabel("Manufacturer", fontsize = 16)
        axes.set_ylabel("Inverse Riskiness", fontsize = 16)
    else:
        axes.set_xticklabels([])
        axes.set_yticklabels([])

    if legend:
        axes.legend([barMaxs, barMeans, barMins], ["Max", "Mean", "Min"], loc = 2)
    
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

    manufacturerIds = cf_data.getManufacturerIds(pdData)
    
    minData  = pdData.groupby("manufacturer", sort = True)["price"].min()
    meanData = pdData.groupby("manufacturer", sort = True)["price"].mean()
    maxData  = pdData.groupby("manufacturer", sort = True)["price"].max()

    axes.set_title("Price by Manufacturers", fontsize = 20)
    axes.plot(manufacturerIds, minData,  c = colors[2], linewidth = 4, alpha = 0.7)
    axes.plot(manufacturerIds, meanData, c = colors[3], linewidth = 4, alpha = 0.7)
    axes.plot(manufacturerIds, maxData,  c = colors[4], linewidth = 4, alpha = 0.7)
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


def radarByManufacturer(
    figure, 
    gridSpec = None, 
    pdData = None, 
    titleAxes = None, 
    legendAxes = None, 
    innerAxes = None, 
    geometry = None, 
    rotate = True):
    
    radarColors = [0, 1, 2]

    dataMin  = pdData.groupby("manufacturer", sort = True).min()
    dataMean = pdData.groupby("manufacturer", sort = True).mean()
    dataMax  = pdData.groupby("manufacturer", sort = True).max()
    
    projection = cf_radar.RadarAxes(spokeCount = len(dataMean.columns))
    
    if geometry:
        (rowNum, colNum) = geometry
    else:
        (rowNum, colNum) = gridSpec.get_geometry()
    
    if not innerAxes:
        subplots = [x for x in gridSpec]
        innerAxes = []

        for(i, m) in enumerate(subplots[colNum:]):
            if i % colNum != 0:
                innerAxes.append(plt.subplot(m, projection = projection))
    
    if not titleAxes:
        titleAxes = figure.add_subplot(gridSpec[0, :])
    
    if legendAxes is None:
        legendAxes = figure.add_subplot(gridSpec[0:, 0])
    
    if legendAxes != False:
        patchMin  = mpl.patches.Patch(color = colors[radarColors[2]], alpha = 0.7, label = "Min")
        patchMean = mpl.patches.Patch(color = colors[radarColors[1]], alpha = 0.7, label = "Mean")
        patchMax  = mpl.patches.Patch(color = colors[radarColors[0]], alpha = 0.7, label = "Max")
        legendAxes.legend(handles=[patchMax, patchMean, patchMin], loc = 10)
        hideAxes(legendAxes)
    
    titleAxes.set_title("Radar - 7 Dimensions for 12 Manufacturers", fontsize = 20)
    hideAxes(titleAxes)
    
    for i, manufacturer in enumerate(cf_data.getManufacturerNames(pdData)):
        axes = innerAxes[i]
        axes.set_title(
            manufacturer.title(), 
            size = 'large', 
            position = (0.5, 1.3), 
            horizontalalignment = 'center', 
            verticalalignment = 'center')
        
        for(color, alpha, data) in zip(radarColors, [0.2, 0.3, 0.4], [dataMax, dataMean, dataMin]):
            axes.fill(
                axes.radar_theta,
                data.loc[manufacturer], 
                color = colors[color], 
                alpha = alpha)
            
            axes.plot(axes.radar_theta, data.loc[manufacturer], color = colors[color])
        
        axes.setVarLabels([x.replace(" ", "\n") for x in dataMean.columns])
        axes.set_yticklabels([])
        axes.patch.set_facecolor('#CDCED1')
        axes.patch.set_alpha(0.5)
        
    
    if gridSpec:
        gridSpec.tight_layout(figure)
    
    return [titleAxes, legendAxes, innerAxes]
