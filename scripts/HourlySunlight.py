import math

# The average hours of sunlight should reflect cosine
DAYLIGHT_AVG_SHORT = 7.2        # [hours]
DAYLIGHT_AVG_LONG = 16.8        # [hours]

SUNLIGHT_HOURS_PER_YEAR = 2205
DAYLIGHT_HOURS_PER_YEAR = 4383

# 50.3% of daylight is sunny on average
# Remaining 49.7% is cloudy, shady, or low sun intensity
SUNNY_PER_DAYLIGHT = 0.503      # [percentage]

# Sun angle
SUN_ANGLE_HIGH = 60             # [deg]
SUN_ANGLE_LOW = 13              # [deg]

DAYS_PER_MONTH = 365.25 / 12

# BEGIN CALCULATIONS
daylightAmp = (DAYLIGHT_AVG_LONG - DAYLIGHT_AVG_SHORT) / 2
daylightMid = daylightAmp + DAYLIGHT_AVG_SHORT
sunlightAmp = (SUN_ANGLE_HIGH - SUN_ANGLE_LOW) / 2
sunAngleMid = sunlightAmp + SUN_ANGLE_LOW

sumDaylight = 0
sumSunlight = 0

for month in range(12):
    k = math.cos(month * math.pi / 6 + math.pi)

    daylight = (daylightAmp * k + daylightMid) * DAYS_PER_MONTH
    sunlight = SUNNY_PER_DAYLIGHT * daylight

    print('%.2f' % daylight)
    # print('%.2f' % daylight + '\t%.2f' % sunlight)
    sumDaylight += daylight
    sumSunlight += sunlight

print('Total daylight hours: %.2f' % sumDaylight)
print('Total sunlight hours: %.2f' % sumSunlight)
