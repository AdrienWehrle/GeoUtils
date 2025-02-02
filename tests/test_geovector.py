import geoutils as gu

GLACIER_OUTLINES_URL = "http://public.data.npolar.no/cryoclim/CryoClim_GAO_SJ_1990.zip"


class TestVector:
    glacier_outlines = gu.Vector(GLACIER_OUTLINES_URL)

    def test_init(self) -> None:

        vector = gu.Vector(GLACIER_OUTLINES_URL)

        assert isinstance(vector, gu.Vector)

    def test_copy(self) -> None:

        vector2 = self.glacier_outlines.copy()

        assert vector2 is not self.glacier_outlines

        vector2.ds = vector2.ds.query("NAME == 'Ayerbreen'")

        assert vector2.ds.shape[0] < self.glacier_outlines.ds.shape[0]

    def test_query(self) -> None:

        vector2 = self.glacier_outlines.query("NAME == 'Ayerbreen'")

        assert vector2 is not self.glacier_outlines

        assert vector2.ds.shape[0] < self.glacier_outlines.ds.shape[0]

    def test_bounds(self) -> None:

        bounds = self.glacier_outlines.bounds

        assert bounds.left < bounds.right
        assert bounds.bottom < bounds.top

        assert bounds.left == self.glacier_outlines.ds.total_bounds[0]
        assert bounds.bottom == self.glacier_outlines.ds.total_bounds[1]
        assert bounds.right == self.glacier_outlines.ds.total_bounds[2]
        assert bounds.top == self.glacier_outlines.ds.total_bounds[3]
