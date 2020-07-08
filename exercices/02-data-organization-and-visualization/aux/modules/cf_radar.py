import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.projections import register_projection
from matplotlib.projections.polar import PolarAxes
from matplotlib.spines import Spine
import numpy as np


class RadarAxes(PolarAxes):

    name = 'radar'

    def __init__(
        self, 
        figure = None, 
        rect = None, 
        spokeCount = 0, 
        radarPatchType = "polygon", 
        radarSpineType = "circle", 
        *args, 
        **kwargs):

        self.spokeCount = spokeCount
        self.radarPatchType = radarPatchType
        self.radarSpineType = radarSpineType
        
        resolution = kwargs.pop("resolution", 1)
        
        if figure == None:
            figure = plt.gcf()
        
        if rect == None:            
            rect = figure.bbox_inches
        
        self.radar_theta = (1.75 * np.pi * np.linspace(0, 1 - 1.0 / self.spokeCount, self.spokeCount))
        self.radar_theta += np.pi / 2

        super(RadarAxes, self).__init__(figure, rect, *args, **kwargs)

    def drawPatch(self):
        if self.radarPatchType == 'polygon':
            return self.drawPolyPatch()

        elif self.radarPatchType == 'circle':
            return drawCirclePatch()

    def drawPolyPatch(self):
        verts = unitPolyVerts(self.radar_theta)

        return plt.Polygon(verts, closed = True, edgecolor = 'k')

    def fill(self, *args, **kwargs):
        closed = kwargs.pop('closed', True)

        return super(RadarAxes, self).fill(closed = closed, *args, **kwargs)

    def plot(self, *args, **kwargs):
        lines = super(RadarAxes, self).plot(*args, **kwargs)

        for line in lines:
            self._close_line(line)

    def setVarLabels(self, labels):
        self.set_thetagrids(self.radar_theta * 180 / np.pi, labels)

    def _as_mpl_axes(self):
        return RadarAxes, {
            'spokeCount':     self.spokeCount,
            'radarPatchType': self.radarPatchType,
            'radarSpineType': self.radarSpineType
        }

    def _close_line(self, line):
        x, y = line.get_data()

        if x[0] != x[-1]:
            x = np.concatenate((x, [x[0]]))
            y = np.concatenate((y, [y[0]]))
            line.set_data(x, y)

    def _gen_axes_patch(self):
        return self.drawPatch()

    def _gen_axes_spines(self):
        if self.radarPatchType == 'circle':
            return PolarAxes._genAxesSpines(self)
            
        spine_type = 'circle'
        verts = unitPolyVerts(self.radar_theta)
        verts.append(verts[0])
        path = Path(verts)
        spine = Spine(self, self.radarSpineType, path)
        spine.set_transform(self.transAxes)

        return {'polar': spine}


def drawCirclePatch(self):
    return plt.Circle((0.5, 0.5), 0.5)


def unitPolyVerts(theta):
    x0, y0, r = [0.5] * 3
    verts = [(r * np.cos(t) + x0, r * np.sin(t) + y0) for t in theta]
    
    return verts


