# harmonic_osc.py
"""
Provides position basis eigenfunctions of the harmonic oscillator,
and the Oscillator class.
"""

import numpy as np
import scipy as sp

from sc_qubits.core.qubit_base import QuantumSystem


def harm_osc_wavefunction(n, x, losc):
    """For given quantum number n=0,1,2,... return the value of the harmonic oscillator wave function
    :math:`\\psi_n(x) = N H_n(x/l_{osc}) \\exp(-x^2/2l_{osc})`, N being the proper normalization factor.

    Parameters
    ----------
    n: int
        index of wave function, n=0 is ground state
    x: float or ndarray
        coordinate(s) where wave function is evaluated
    losc: float
        oscillator length, defined via <0|x^2|0> = losc^2/2

    Returns
    -------
    float
        value of harmonic oscillator wave function
    """
    return ((2.0 ** n * sp.special.gamma(n + 1.0) * losc) ** (-0.5) * np.pi ** (-0.25) *
            sp.special.eval_hermite(n, x / losc) * np.exp(-(x * x) / (2 * losc * losc)))


# —Oscillator class—————————————————————————————————————————————————————————————————————————————————————————————————————

class Oscillator(QuantumSystem):
    """General class for mode of an oscillator/resonator."""

    def __init__(self, omega, truncated_dim=None):
        self._sys_type = 'Oscillator'
        self.omega = omega
        self.truncated_dim = truncated_dim

    def eigenvals(self, evals_count=6):
        """Returns list of eigenvalues.

        Parameters
        ----------
        evals_count: int, optional
            number of desired eigenvalues (Default value = 6)

        Returns
        -------
        ndarray
        """
        evals = [self.omega * n for n in range(evals_count)]
        return np.asarray(evals)

    def hilbertdim(self):
        """Returns Hilbert space dimension

        Returns
        -------
        int
        """
        return self.truncated_dim
