import math

AVG_POWER_PER_DAY = 19.7e3      # [kWh]
AVG_POWER_PER_HOUR = AVG_POWER_PER_DAY / 24
FLUCTUATION = 0.25              # [ul]
PHASE_SHIFT = 7                 # [hours]

powerSum = 0

for hour in range(24):
    k = math.cos((hour * math.pi + 2 * PHASE_SHIFT) / 12)
    power = AVG_POWER_PER_HOUR * (FLUCTUATION * k + 1)
    print('%d:00' % hour + '\t%.2f W' % power)

    powerSum += power

print('Total power:', powerSum)