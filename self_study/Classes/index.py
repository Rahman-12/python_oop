# Class for an Energy Meter

class EnergyMeter:
    rate_per_kwh = 0.30  # 30 pence per kWh (shared default for all meters)

    def __init__(self, meter_id: str):
        self.meter_id = meter_id   # stored on this specific meter
        self._readings = []        # starts empty for this meter only

    def add_reading(self, kwh: float) -> None:
        if kwh <= 0:
            raise ValueError("Reading must be positive")
        self._readings.append(kwh)  # updates this meter's internal list

    def total_kwh(self) -> float:
        return sum(self._readings)  # calculates based on this meter's data

    def bill(self) -> float:
        # uses instance data + class default
        return self.total_kwh() * self.rate_per_kwh

    def __repr__(self) -> str:
        return f"EnergyMeter({self.meter_id!r}, total={self.total_kwh():.2f} kWh)"


m = EnergyMeter("MPAN-123")
# EnergyMeter('MPAN-123', total=0.00 kWh)
print("After __init__:", m)

m.add_reading(4.2)
print("After first reading:", m.total_kwh())  # 4.2

m.add_reading(3.8)
print("After second reading:", m.total_kwh())  # 8.0

print("Current rate:", m.rate_per_kwh)        # 0.3 (class default)
print("Bill now (£):", m.bill())              # 8.0 * 0.3 = 2.4
