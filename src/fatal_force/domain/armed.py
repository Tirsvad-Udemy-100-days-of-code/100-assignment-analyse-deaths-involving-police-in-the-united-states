"""@brief How many victims were armed, unarmed or of unknown armament."""

from dataclasses import dataclass

_PERCENT = 100.0


@dataclass(frozen=True, slots=True)
class ArmedShares:
    """@brief Counts of victims by armament; armed is everything but the rest.

    @param total The number of victims.
    @param armed Victims with a weapon label other than unarmed or unknown.
    @param unarmed Victims labelled unarmed.
    @param unknown Victims whose armament is unknown.
    """

    total: int
    armed: int
    unarmed: int
    unknown: int

    def _percent(self, count: int) -> float:
        """@brief Express a count as a percentage of the total.

        @param count The count to express.
        @return The percentage, or 0.0 when there are no victims.
        """
        return _PERCENT * count / self.total if self.total else 0.0

    @property
    def armed_percent(self) -> float:
        """@brief Percentage of armed victims."""
        return self._percent(self.armed)

    @property
    def unarmed_percent(self) -> float:
        """@brief Percentage of unarmed victims."""
        return self._percent(self.unarmed)

    @property
    def unknown_percent(self) -> float:
        """@brief Percentage of victims with unknown armament."""
        return self._percent(self.unknown)
