from __future__ import annotations

import unittest
from decimal import Decimal
from fractions import Fraction

from src.amador_kernel import AmadorKernel
from src.amador_kernel.kahler_ricci import CohomologicalObstructionError, KahlerRicciEngine
from src.amador_kernel.ps_kl_optimizer import ProjectivePSKLOptimizer
from src.amador_kernel.strominger_conifold import HullStromingerConifold
from src.amador_kernel.spectral_toeplitz import ToeplitzSpectralTriple
from src.amador_kernel.colombeau_levi_civita import DiffeomorphismInvariantColombeau
from src.amador_kernel.cohesive_topos import CohesiveToposHN
from src.amador_kernel.symplectic_thermodynamics import KoopmanAmadorThermodynamics


class TestAmadorKernel(unittest.TestCase):
    def test_kahler_ricci_closure(self):
        engine = KahlerRicciEngine(c1_BC=0.0, volume=1.0)
        self.assertTrue(engine.validate())
        self.assertTrue(engine.check_a_priori_bounds())
        self.assertAlmostEqual(engine.evolve_potential(0.5, 1.0), 0.5 + 0.5 * 0.6931471805599453, places=12)

        with self.assertRaises(CohomologicalObstructionError):
            KahlerRicciEngine(c1_BC=1e-6).validate()

    def test_ps_kl_projection_and_saddle(self):
        opt = ProjectivePSKLOptimizer(n=12, gamma=0.1)
        self.assertEqual(opt.project_to_ker_d_ev([3.0, 1.0, 2.0]), [1.0, -1.0, 0.0])
        self.assertTrue(opt.strict_saddle_check([], [-1.0]))
        self.assertGreaterEqual(opt.polyak_lojasiewicz(1.0, 0.2), 0.0)

    def test_conifold_stability(self):
        conifold = HullStromingerConifold(alpha_prime=0.1)
        self.assertTrue(conifold.validate_stability())
        self.assertTrue(conifold.check_anomaly_cancellation())
        self.assertGreater(conifold.dynamic_recaling(0.5), 0.0)

    def test_spectral_toeplitz(self):
        triple = ToeplitzSpectralTriple(sigma=2.0)
        self.assertTrue(triple.verify_commutation_relations())
        self.assertEqual(triple.dynamic_spectral_dimension(1.0), 0.0)
        self.assertEqual(triple.dynamic_spectral_dimension(2.5), 2.0)
        self.assertEqual(triple.dynamic_spectral_dimension(10.0), 4.0)

    def test_colombeau_finite_part(self):
        colombeau = DiffeomorphismInvariantColombeau(rho=Decimal("1e-3"))
        self.assertEqual(
            colombeau.extract_finite_part({Fraction(0, 1): Decimal("2.0")}),
            Decimal("2.0"),
        )
        self.assertTrue(colombeau.unit_preserved())

    def test_cohesive_topos(self):
        topo = CohesiveToposHN()
        self.assertTrue(topo.validate_orbifold())
        self.assertIn("delta^i", topo.daseinization())

    def test_symplectic_thermodynamics(self):
        thermo = KoopmanAmadorThermodynamics(temperature=Decimal("1.0"))
        self.assertEqual(thermo.entropy_balance(), Decimal("0.00000000"))

    def test_kernel_execution_report(self):
        kernel = AmadorKernel()
        report = kernel.execute_canonical_operator({
            "c1_BC": 0.0,
            "volume": 1.0,
            "n": 12,
            "gamma": 0.1,
            "rho": Decimal("1e-3"),
            "temperature": Decimal("1.0"),
            "alpha_prime": 1e-3,
            "spectral_dimension": 2.0,
        })
        self.assertIn(report.status, {"VALID", "WARNING"})
        self.assertIn("kahlers_ricci_closure", report.verified_lemmas)


if __name__ == "__main__":
    unittest.main()
