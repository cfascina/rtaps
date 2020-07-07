import pandas as pd


limited_columns = [
    "make",
    "price",
    "city mpg",
    "highway mpg",
    "horsepower",
    "weight",
    "riskiness",
    "losses"
]


def getManufacturerNames(data):
    return sorted(list(pd.Series(data["make"]).unique()))


def getManufacturerLabels(data):
    return [x.title() for x in getManufacturerNames(data)]


def mapManufacturerId(data):
    return {x: i for (i, x) in enumerate(getManufacturerNames(data))}


def getManufacturerIds(data):
    return sorted(mapManufacturerId(data).values())


def getRawData():
    data_file = "aux/datasets/automobile.csv"

    return pd.read_csv(data_file)


def getManufacturerData(make, pdData):
    return pdData[(pdData["make"] == make)]


def getManufacturerCount(pdData, lower_bound = 0):
    counts = []
    filtered_makes = []

    for manufacturer in getAllManufacturers():
        data = getManufacturerData(manufacturer, pdData)
        count = len(data.index)

        if count >= lower_bound:
            filtered_makes.append(manufacturer)
            counts.append(count)

    return(filtered_makes, list(zip(filtered_makes, counts)))


def getLimitedData(cols = None, lower_bound = None):
    if not cols:
        cols = limited_columns
        
    data = getRawData()[cols]

    if lower_bound:
        (makes, _) = getManufacturerCount(data, lower_bound)
        data = data[data["make"].isin(makes)]

    return data


def normalizeColumn(colName, pdData, inverted = False):
    pdData[colName] -= pdData[colName].min()
    pdData[colName] /= pdData[colName].max()

    if inverted:
        pddata[col_name] = 1 - pdData[colName]


def normalizeColumns(colNames, pdData):
    for name in colNames:
        normalizeColumn(name, pdData)


def invertNormalizedColumns(colNames, pdData):
    for name in colNames:
        normalizeColumn(name, pdData, inverted = True)


def getAllManufacturers():
    return pd.Series(getRawData()["make"]).unique()


def getNumericData(pdData):
    return pdData.replace({"make": mapManufacturerId(pdData)})
