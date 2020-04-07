import numpy as np
from collections import defaultdict
from typing import Dict, Sequence, Iterable
from PyQt5 import QtWidgets, QtCore
from ..sdb import Surface
from ..sdb.glsl import gen_get_all_recursive
from .scalar import Assembly
from ..sdb.qt import SphereTraceRender, SphereTraceViewer
from ..delegate import Delegate
from .. import v4
from ..qt import application

__all__ = ['view_assembly', 'AssemblyViewer', 'application']

def view_assembly(a: Assembly, all_properties: Dict[Surface, Dict] = None):
    if all_properties is None:
        all_properties = {}
    all_properties = defaultdict(dict, all_properties)

    epsilon = v4.norm(a.surface.get_aabb(np.eye(4)).size)*1e-3

    for surface in a.surface.descendants():
        all_properties[surface].setdefault('edge_width', epsilon*5)

    sdb_glsl = gen_get_all_recursive(a.surface, all_properties)
    viewer = AssemblyViewer(sdb_glsl)
    viewer.epsilon = epsilon
    viewer.show()
    return viewer

class AssemblyViewer(QtWidgets.QWidget):
    def __init__(self, sdb_glsl: str, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        display_widget = SphereTraceRender([sdb_glsl])

        max_steps = QtWidgets.QSpinBox()
        max_steps.setRange(1, 1000)
        max_steps.setValue(display_widget.max_steps)
        max_steps.valueChanged.connect(self.maxStepsChanged)

        sb = QtWidgets.QDoubleSpinBox()
        self._log10epsilon = sb
        sb.setRange(-20, 2)
        sb.setValue(np.log10(display_widget.epsilon))
        sb.valueChanged.connect(self.log10EpsilonChanged)

        hbox = QtWidgets.QHBoxLayout()
        self.setLayout(hbox)
        vbox = QtWidgets.QVBoxLayout()
        hbox.addLayout(vbox)
        vbox.addWidget(max_steps)
        vbox.addWidget(self._log10epsilon)
        vbox.addStretch(1)
        hbox.addWidget(display_widget)

        timer = QtCore.QTimer()
        timer.timeout.connect(display_widget.update)
        #timer.start(0)
        self.timer = timer

        self.display_widget = display_widget

    def maxStepsChanged(self, value):
        self.display_widget.max_steps = value

    def log10EpsilonChanged(self, value):
        self.display_widget.epsilon = 10**value

    def sizeHint(self):
        return QtCore.QSize(640, 480)

    def set_rays(self, rays: Sequence[np.ndarray], colors: Iterable = None):
        self.display_widget.set_rays(rays, colors)

    projection = Delegate('display_widget', 'projection')
    eye_to_world = Delegate('display_widget', 'eye_to_world')

    @property
    def max_steps(self) -> int:
        return self.display_widget.max_steps

    @max_steps.setter
    def max_steps(self, v: int):
        self._max_steps.setValue(v)

    @property
    def epsilon(self) -> float:
        return self.display_widget.epsilon

    @epsilon.setter
    def epsilon(self, v: float):
        self._log10epsilon.setValue(np.log10(v))


