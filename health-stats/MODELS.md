# Wire model evidence

Gson annotation names and Kotlin serialization descriptor names, not invented sample responses. Reference/boxed types may be nullable; confirm Kotlin metadata/defaults before enforcing required fields. A serializer optional flag describes this client serializer, not server availability. Source references are relative to the Garmin folder.

## b22.a

Source: `health-stats/sources/b22.a.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `goal` | `optional=True` | 41 |
| `moderate` | `optional=True` | 42 |
| `vigorous` | `optional=True` | 43 |

## b22.b

Source: `health-stats/sources/b22.b.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `steps` | `optional=True` | 36 |

## b22.c

Source: `health-stats/sources/b22.c.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `goal` | `optional=True` | 37 |
| `value` | `optional=True` | 38 |

## b22.d

Source: `health-stats/sources/b22.d.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `"calories"` | `private final c calories;` | 16 |
| `"movement"` | `private final i movement;` | 20 |

## b22.e

Source: `health-stats/sources/b22.e.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `"data"` | `private final d data;` | 14 |

## b22.f

Source: `health-stats/sources/b22.f.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `data` | `optional=False` | 48 |

## b22.g

Source: `health-stats/sources/b22.g.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `uuid` | `optional=False` | 44 |
| `userProfilePk` | `optional=False` | 45 |
| `calendarDate` | `optional=False` | 46 |
| `source` | `optional=False` | 47 |
| `intensityMinutes` | `optional=True` | 48 |
| `movement` | `optional=True` | 49 |

## bx.f

Source: `health-stats/sources/bx.f.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `"calendarDate"` | `private final String calendarDate;` | 18 |
| `"values"` | `private final i values;` | 22 |

## bx.i

Source: `health-stats/sources/bx.i.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `alternate = {"avgDailyLowBodyBattery"}, value = "lowBodyBattery"` | `private final Integer lowBodyBattery;` | 18 |
| `alternate = {"avgDailyHighBodyBattery"}, value = "highBodyBattery"` | `private final Integer highBodyBattery;` | 22 |

## co0.d

Source: `health-stats/sources/co0.d.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `"calendarDate"` | `private final String _calendarDate;` | 19 |
| `"values"` | `private final b values;` | 23 |
| `"abnormalHRAlertCount"` | `private final Integer abnormalHRAlertCount;` | 112 |
| `alternate = {"avgRestingHR"}, value = "restingHR"` | `private final Integer restingHeartRate;` | 116 |
| `"wellnessMaxAvgHR"` | `private final Integer maxHeartRate;` | 120 |

## dc1.a

Source: `health-stats/sources/dc1.a.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `"monitoringEnvironmentValues"` | `private Object[][] monitoringEnvironmentValuesArray;` | 25 |
| `"userProfilePK"` | `private long userProfilePK;` | 29 |
| `"calendarDate"` | `private String calendarDate;` | 33 |
| `"startTimestampGMT"` | `private String startTimestampGMT;` | 37 |
| `"endTimestampGMT"` | `private String endTimestampGMT;` | 41 |
| `"startTimestampLocal"` | `private String startTimestampLocal;` | 45 |
| `"endTimestampLocal"` | `private String endTimestampLocal;` | 49 |
| `"sleepStartTimestampGMT"` | `private String sleepStartTimestampGMT;` | 53 |
| `"sleepEndTimestampGMT"` | `private String sleepEndTimestampGMT;` | 57 |
| `"sleepStartTimestampLocal"` | `private String sleepStartTimestampLocal;` | 61 |
| `"sleepEndTimestampLocal"` | `private String sleepEndTimestampLocal;` | 65 |
| `"tomorrowSleepStartTimestampGMT"` | `private String tomorrowSleepStartTimestampGMT;` | 69 |
| `"tomorrowSleepEndTimestampGMT"` | `private String tomorrowSleepEndTimestampGMT;` | 73 |
| `"tomorrowSleepStartTimestampLocal"` | `private String tomorrowSleepStartTimestampLocal;` | 77 |
| `"tomorrowSleepEndTimestampLocal"` | `private String tomorrowSleepEndTimestampLocal;` | 81 |
| `"averageSpO2"` | `private Double averageSpO2;` | 85 |
| `"lowestSpO2"` | `private Double lowestSpO2;` | 89 |
| `"lastSevenDaysAvgSpO2"` | `private Double lastSevenDaysAvgSpO2;` | 93 |
| `"latestSpO2"` | `private Double latestSpO2;` | 97 |
| `"latestSpO2TimestampGMT"` | `private String latestSpO2TimestampGMT;` | 101 |
| `"latestSpO2TimestampLocal"` | `private String latestSpO2TimestampLocal;` | 105 |
| `"avgSleepSpO2"` | `private Double avgSleepSpO2;` | 109 |
| `"avgTomorrowSleepSpO2"` | `private Double avgTomorrowSleepSpO2;` | 113 |
| `"spO2SingleValues"` | `private Object[][] spO2SingleValuesArray;` | 117 |
| `"spO2HourlyAverages"` | `private Object[][] spO2HourlyAveragesArray;` | 121 |

## i41.a

Source: `health-stats/sources/i41.a.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `"lowUpper"` | `private Integer lowUpper;` | 22 |
| `"balancedLow"` | `private Integer balancedLow;` | 26 |
| `"balancedUpper"` | `private Integer balancedUpper;` | 30 |
| `"markerValue"` | `private Double markerValue;` | 34 |
| `lowUpper` | `optional=True` | 52 |
| `balancedLow` | `optional=True` | 53 |
| `balancedUpper` | `optional=True` | 54 |
| `markerValue` | `optional=True` | 55 |

## i41.b

Source: `health-stats/sources/i41.b.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `"userProfilePk"` | `private String userProfilePk;` | 21 |
| `"hrvSummary"` | `private f hrvSummary;` | 25 |
| `"hrvReadings"` | `private List<c> hrvReadings;` | 29 |
| `"startTimestampGMT"` | `private String startTimestampGMT;` | 33 |
| `"endTimestampGMT"` | `private String endTimestampGMT;` | 37 |
| `"startTimestampLocal"` | `private String startTimestampLocal;` | 41 |
| `"endTimestampLocal"` | `private String endTimestampLocal;` | 45 |
| `"sleepStartTimestampGMT"` | `private String sleepStartTimestampGMT;` | 49 |
| `"sleepEndTimestampGMT"` | `private String sleepEndTimestampGMT;` | 53 |
| `"sleepStartTimestampLocal"` | `private String sleepStartTimestampLocal;` | 57 |
| `"sleepEndTimestampLocal"` | `private String sleepEndTimestampLocal;` | 61 |

## i41.c

Source: `health-stats/sources/i41.c.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `"hrvValue"` | `private int hrvValue;` | 17 |
| `"readingTimeGMT"` | `private String readingTimeGMT;` | 21 |
| `"readingTimeLocal"` | `private String readingTimeLocal;` | 25 |

## i41.e

Source: `health-stats/sources/i41.e.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `"hrvSummaries"` | `private List<f> hrvSummaries;` | 23 |

## i41.f

Source: `health-stats/sources/i41.f.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `"calendarDate"` | `private String calendarDate;` | 28 |
| `"weeklyAvg"` | `private Integer weeklyAvg;` | 32 |
| `"lastNightAvg"` | `private Integer lastNightAvg;` | 36 |
| `"lastNight5MinHigh"` | `private Integer lastNight5MinHigh;` | 40 |
| `"baseline"` | `private i41.a baseline;` | 44 |
| `"status"` | `private String status;` | 48 |
| `"feedbackPhrase"` | `private String feedbackPhrase;` | 52 |
| `"createTimeStamp"` | `private String createTimeStamp;` | 56 |
| `calendarDate` | `optional=True` | 74 |
| `weeklyAvg` | `optional=True` | 75 |
| `lastNightAvg` | `optional=True` | 76 |
| `lastNight5MinHigh` | `optional=True` | 77 |
| `baseline` | `optional=True` | 78 |
| `status` | `optional=True` | 79 |
| `feedbackPhrase` | `optional=True` | 80 |
| `createTimeStamp` | `optional=True` | 81 |

## jp0.a

Source: `health-stats/sources/jp0.a.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `"calendarDate"` | `private final String calendarDate;` | 20 |
| `"valueInML"` | `private final Double valueInML;` | 24 |
| `"goalInML"` | `private final Double goalInML;` | 28 |

## jp0.b

Source: `health-stats/sources/jp0.b.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `"userId"` | `private Integer userId;` | 29 |
| `"calendarDate"` | `private String calendarDate;` | 33 |
| `"lastEntryTimestampLocal"` | `private String lastEntryTimestampLocal;` | 37 |
| `"valueInML"` | `private Double valueInML;` | 41 |
| `"goalInML"` | `private Double goalInML;` | 45 |
| `"sweatLossInML"` | `private Double sweatLossInML;` | 49 |
| `"activityIntakeInML"` | `private Double activityIntakeInML;` | 53 |
| `"baseGoalInML"` | `private Double baseGoalInML;` | 57 |
| `"hydrationMeasurementUnit"` | `private String hydrationMeasurementUnit;` | 61 |
| `"hydrationAutoGoalEnabled"` | `private Boolean hydrationAutoGoalEnabled;` | 65 |
| `"hydrationContainers"` | `private List<op0.a> hydrationContainers;` | 69 |

## jq1.a

Source: `health-stats/sources/jq1.a.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `totalStepsAverage` | `optional=True` | 126 |
| `totalStepsWeeklyAverage` | `optional=True` | 127 |

## jq1.b

Source: `health-stats/sources/jq1.b.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `userProfileId` | `optional=True` | 46 |
| `calendarDate` | `optional=True` | 47 |
| `totalSteps` | `optional=True` | 48 |
| `totalKilocalories` | `optional=True` | 49 |
| `wellnessDistanceMeters` | `optional=True` | 50 |
| `dailyStepGoal` | `optional=True` | 51 |
| `wellnessStartTimeGmt` | `optional=True` | 52 |
| `wellnessStartTimeLocal` | `optional=True` | 53 |
| `wellnessEndTimeGmt` | `optional=True` | 54 |
| `wellnessEndTimeLocal` | `optional=True` | 55 |

## jq1.e

Source: `health-stats/sources/jq1.e.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `totalSteps` | `optional=True` | 114 |
| `totalDistance` | `optional=True` | 115 |
| `stepGoal` | `optional=True` | 116 |

## jq1.j

Source: `health-stats/sources/jq1.j.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `totalSteps` | `optional=True` | 114 |
| `wellnessDataDaysCount` | `optional=True` | 115 |
| `totalDistance` | `optional=True` | 116 |

## jq1.k

Source: `health-stats/sources/jq1.k.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `payload` | `optional=True` | 33 |

## km1.a

Source: `health-stats/sources/km1.a.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `"endGMT"` | `private long endGMT;` | 16 |
| `"startGMT"` | `private long startGMT;` | 20 |
| `"value"` | `private Integer value;` | 24 |

## km1.a0

Source: `health-stats/sources/km1.a0.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `"version"` | `private final long version;` | 17 |
| `"userProfilePK"` | `private final long userProfilePk;` | 21 |
| `"calendarDate"` | `private final String calendarDate;` | 25 |
| `"deviceId"` | `private final long deviceId;` | 29 |
| `"timestampGmt"` | `private final String timestampGmt;` | 33 |
| `"baseline"` | `private final Integer baseline;` | 37 |
| `"actual"` | `private final Integer actual;` | 41 |
| `"feedback"` | `private final String feedback;` | 45 |
| `"trainingFeedback"` | `private final String trainingFeedback;` | 49 |
| `"sleepHistoryAdjustment"` | `private final String sleepHistoryAdjustment;` | 53 |
| `"hrvAdjustment"` | `private final String hrvAdjustment;` | 57 |
| `"napAdjustment"` | `private final String napAdjustment;` | 61 |
| `"preferredActivityTracker"` | `private final Boolean preferredActivityTracker;` | 65 |
| `"displayedForTheDay"` | `private final Boolean displayedForTheDay;` | 69 |
| `"recommendedBedtimeStartMins"` | `private final Integer recommendedBedtimeStartMins;` | 73 |
| `"recommendedBedtimeEndMins"` | `private final Integer recommendedBedtimeEndMins;` | 77 |

## km1.b

Source: `health-stats/sources/km1.b.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `"userProfilePK"` | `private final long userProfilePK;` | 18 |
| `"deviceId"` | `private final long deviceId;` | 22 |
| `"calendarDate"` | `private final String calendarDate;` | 26 |
| `"napTimeSec"` | `private final Integer napTimeSec;` | 30 |
| `"napStartTimestampGMT"` | `private final String napStartTimestampGMT;` | 34 |
| `"napEndTimestampGMT"` | `private final String napEndTimestampGMT;` | 38 |
| `"napFeedback"` | `private final String napFeedback;` | 42 |
| `"napSource"` | `private final Integer napSource;` | 46 |
| `"napStartTimeOffset"` | `private final Integer napStartTimeOffset;` | 50 |
| `"napEndTimeOffset"` | `private final Integer napEndTimeOffset;` | 54 |

## km1.c

Source: `health-stats/sources/km1.c.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `"skinTempCalibrationDays"` | `private Integer skinTempCalibrationDays;` | 21 |
| `"dailySleepDTO"` | `private v dailySleep;` | 25 |
| `"sleepMovement"` | `private List<s> sleepMovement;` | 29 |
| `"sleepLevels"` | `private List<s> sleepLevels;` | 33 |
| `"breathingDisruptionData"` | `private List<km1.a> breathingVariationsData;` | 37 |
| `"restlessMomentsCount"` | `private Integer restlessMomentsCount;` | 41 |
| `"sleepRestlessMoments"` | `private List<z> sleepRestlessMoments;` | 45 |
| `"wellnessSpO2SleepSummaryDTO"` | `private lm1.c wellnessSpO2SleepSummary;` | 49 |
| `"wellnessSpO2EventDTOList"` | `private List<lm1.b> wellnessSpO2EventList;` | 53 |
| `"wellnessEpochSPO2DataDTOList"` | `private List<lm1.a> wellnessEpochSPO2DataList;` | 57 |
| `"wellnessEpochRespirationDataDTOList"` | `private List<n> wellnessEpochRespirationDataDTOList;` | 61 |
| `"wellnessEpochRespirationAveragesList"` | `private List<m> wellnessEpochRespirationAveragesList;` | 65 |
| `"respirationVersion"` | `private Integer respirationVersion;` | 69 |
| `"sleepStress"` | `private List<z> sleepStressList;` | 73 |
| `"sleepHeartRate"` | `private List<z> sleepHeartRateList;` | 77 |
| `"restingHeartRate"` | `private final Integer restingHeartRate;` | 81 |
| `"sleepBodyBattery"` | `private List<z> sleepBodyBatteryList;` | 85 |
| `"bodyBatteryChange"` | `private Integer bodyBatteryChange;` | 89 |
| `"skinTempDataExist"` | `private boolean skinTempDataExist;` | 93 |
| `"skinTempData"` | `private List<o> skinTempDataList;` | 97 |
| `"avgSkinTempDeviationC"` | `private Double avgSkinTempDeviationC;` | 101 |
| `"avgSkinTempDeviationF"` | `private Double avgSkinTempDeviationF;` | 105 |
| `"hrvData"` | `private List<z> hrvDataList;` | 109 |
| `"hrvStatus"` | `private String hrvStatus;` | 113 |
| `"avgOvernightHrv"` | `private Integer avgOvernightHrv;` | 117 |

## km1.m

Source: `health-stats/sources/km1.m.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `"epochEndTimestampGmt"` | `private long epochEndTimestampGmt;` | 16 |
| `"respirationAverageValue"` | `private Double respirationAverageValue;` | 20 |
| `"respirationHighValue"` | `private Double respirationHighValue;` | 24 |
| `"respirationLowValue"` | `private Double respirationLowValue;` | 28 |

## km1.n

Source: `health-stats/sources/km1.n.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `"startTimeGMT"` | `private long startTimeGMT;` | 16 |
| `"respirationValue"` | `private Double respirationValue;` | 20 |

## km1.o

Source: `health-stats/sources/km1.o.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `"value"` | `private final Double value;` | 16 |
| `"startGMT"` | `private final Long startGMT;` | 20 |
| `"deviationCelsius"` | `private final Double deviationCelsius;` | 24 |
| `"deviationFahrenheit"` | `private final Double deviationFahrenheit;` | 28 |

## km1.p

Source: `health-stats/sources/km1.p.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `"userId"` | `private final Long userId;` | 20 |
| `"calendarDate"` | `private final String calendarDate;` | 24 |
| `"deviceId"` | `private final Long deviceId;` | 28 |
| `"isPreferredActivityTracker"` | `private final Boolean isPreferredActivityTracker;` | 32 |
| `"sleepNeedBaselineMins"` | `private final Integer sleepNeedBaselineMins;` | 36 |
| `"optimalSleepWindowStartMins"` | `private final Integer optimalSleepWindowStartMins;` | 40 |
| `"optimalSleepWindowEndMins"` | `private final Integer optimalSleepWindowEndMins;` | 44 |
| `"status"` | `private final String status;` | 48 |
| `"optimalSleepWindowMidpointMins"` | `private final Integer optimalSleepWindowMidpointMins;` | 52 |
| `"lastSleepMidpointMins"` | `private final Integer lastSleepMidpointMins;` | 56 |

## km1.s

Source: `health-stats/sources/km1.s.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `"activityLevel"` | `private double sleepActivityLevel;` | 20 |
| `"startGMT"` | `private DateTime sleepStartTimestampGMT;` | 24 |
| `"endGMT"` | `private DateTime sleepEndTimestampGMT;` | 29 |

## km1.v

Source: `health-stats/sources/km1.v.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `"highestSpO2Value"` | `private Integer highestSpO2Value;` | 26 |
| `"averageSpO2HRSleep"` | `private Integer averageSpO2HRSleep;` | 30 |
| `"avgHeartRate"` | `private final Double avgHeartRate;` | 34 |
| `"spo2Threshold"` | `private Integer spo2Threshold;` | 38 |
| `"deviceRemCapable"` | `private boolean deviceRemCapable;` | 42 |
| `"sleepFromDevice"` | `private boolean sleepFromDevice;` | 46 |
| `"averageRespirationValue"` | `private Double averageRespirationValue;` | 50 |
| `"sleepScores"` | `private jm1.c sleepScores;` | 54 |
| `"lowestRespirationValue"` | `private Double lowestRespirationValue;` | 58 |
| `"highestRespirationValue"` | `private Double highestRespirationValue;` | 63 |
| `"sleepNeed"` | `private final a0 sleepNeed;` | 68 |
| `"nextSleepNeed"` | `private final a0 nextSleepNeed;` | 72 |
| `"dailyNapDTOS"` | `private final List<km1.b> dailyNapDTOS;` | 76 |
| `"breathingDisruptionSeverity"` | `private final String breathingDisruptionSeverity;` | 80 |
| `"sleepAlignment"` | `private final p sleepAlignment;` | 84 |
| `"sleepScoreFeedback"` | `private String sleepScoreFeedback;` | 88 |
| `"sleepScoreInsight"` | `private String sleepScoreInsight;` | 92 |
| `"sleepScorePersonalizedInsight"` | `private String sleepScorePersonalizedInsight;` | 96 |
| `"sleepVersion"` | `private Integer sleepVersion;` | 100 |
| `"userNote"` | `private String userNote;` | 104 |
| `"id"` | `private long id;` | 108 |
| `"userProfilePK"` | `private long userProfilePK;` | 112 |
| `"calendarDate"` | `private String calendarDate;` | 116 |
| `"sleepTimeSeconds"` | `private int sleepTimeSeconds;` | 120 |
| `"napTimeSeconds"` | `private int napTimeSeconds;` | 124 |
| `"sleepWindowConfirmed"` | `private boolean sleepWindowConfirmed;` | 128 |
| `"sleepWindowConfirmationType"` | `private String sleepWindowConfirmedType;` | 132 |
| `"sleepStartTimestampGMT"` | `private long sleepStartTimestampGMT;` | 136 |
| `"sleepEndTimestampGMT"` | `private long sleepEndTimestampGMT;` | 140 |
| `"sleepStartTimestampLocal"` | `private long sleepStartTimestampLocal;` | 144 |
| `"sleepEndTimestampLocal"` | `private long sleepEndTimestampLocal;` | 148 |
| `"retro"` | `private Boolean retro;` | 152 |
| `"autoSleepStartTimestampGMT"` | `private Long autoSleepStartTimestampGMT;` | 156 |
| `"autoSleepEndTimestampGMT"` | `private Long autoSleepEndTimestampGMT;` | 160 |
| `"sleepQualityTypePK"` | `private String sleepQualityTypePk;` | 164 |
| `"sleepResultTypePK"` | `private String sleepResultTypePK;` | 168 |
| `"unmeasurableSleepSeconds"` | `private int unmeasurableSleepSeconds;` | 172 |
| `"deepSleepSeconds"` | `private int deepSleepSeconds;` | 176 |
| `"lightSleepSeconds"` | `private int lightSleepSeconds;` | 180 |
| `"remSleepSeconds"` | `private int remSleepSeconds;` | 184 |
| `"awakeSleepSeconds"` | `private int awakeSleepSeconds;` | 188 |
| `"awakeCount"` | `private Integer awakeCount;` | 192 |
| `"avgSleepStress"` | `private Double avgSleepStress;` | 196 |
| `"averageSpO2Value"` | `private Integer averageSpO2Value;` | 200 |
| `"lowestSpO2Value"` | `private Integer lowestSpO2Value;` | 204 |

## km1.z

Source: `health-stats/sources/km1.z.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `"value"` | `private final int value;` | 16 |
| `"startGMT"` | `private final long startGMT;` | 20 |

## kr1.a

Source: `health-stats/sources/kr1.a.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `"calendarDate"` | `private String _calendarDate;` | 23 |
| `"values"` | `private final b values;` | 27 |
| `"highStressDuration"` | `private final Integer highStressDuration;` | 117 |
| `"lowStressDuration"` | `private final Integer lowStressDuration;` | 121 |
| `"overallStressLevel"` | `private final Integer overallStressLevel;` | 125 |
| `"restStressDuration"` | `private final Integer restStressDuration;` | 129 |
| `"mediumStressDuration"` | `private final Integer mediumStressDuration;` | 133 |

## kw.o

Source: `health-stats/sources/kw.o.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `"startDate"` | `private String startDate;` | 23 |
| `"endDate"` | `private String endDate;` | 27 |
| `"bloodPressureMeasurements"` | `private List<pw.a> bloodPressureMeasurements;` | 31 |

## l42.a

Source: `health-stats/sources/l42.a.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `"dateWeightList"` | `private List<c> dateWeightList;` | 22 |
| `"endDate"` | `private String endDate;` | 26 |
| `"startDate"` | `private String startDate;` | 30 |
| `"totalAverage"` | `private g totalAverage;` | 34 |

## l42.b

Source: `health-stats/sources/l42.b.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `"latestWeight"` | `private c latestWeight;` | 22 |
| `"maxWeight"` | `private Double maxWeight;` | 26 |
| `"minWeight"` | `private Double minWeight;` | 30 |
| `"numOfWeightEntries"` | `private int numberOfWeightEntries;` | 34 |
| `"summaryDate"` | `private String summaryDate;` | 38 |

## l42.c

Source: `health-stats/sources/l42.c.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `"calendarDate"` | `private final String calendarDate;` | 21 |
| `"date"` | `private final String date;` | 25 |
| `"samplePk"` | `private final long samplePk;` | 29 |
| `"timestampGMT"` | `private final String timestampGmt;` | 33 |
| `"weightDelta"` | `private final Double weightDelta;` | 37 |

## l42.e

Source: `health-stats/sources/l42.e.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `"weeklyWeightSummaries"` | `private List<f> weeklyWeightSummaryList;` | 20 |
| `"previousWeekAverageDTO"` | `private g previousWeekAverageDTO;` | 24 |
| `"nextWeekAverageDTO"` | `private g nextWeekAverageDTO;` | 28 |
| `"weightAverageDTO"` | `private g weightAverageDto;` | 32 |

## l42.f

Source: `health-stats/sources/l42.f.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `"averageWeight"` | `private g weightAverageDto;` | 20 |
| `"endDate"` | `private String endDate;` | 24 |
| `"startDate"` | `private String startDate;` | 28 |
| `"minWeight"` | `private Double minWeight;` | 32 |
| `"maxWeight"` | `private Double maxWeight;` | 36 |
| `"weightDelta"` | `private Double weightDelta;` | 40 |

## l42.g

Source: `health-stats/sources/l42.g.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `"bmiCount"` | `private Integer bmiCount;` | 18 |
| `"bodyFatCount"` | `private Integer bodyFatCount;` | 22 |
| `"bodyWaterCount"` | `private Integer bodyWaterCount;` | 26 |
| `"boneMassCount"` | `private Integer boneMassCount;` | 30 |
| `"from"` | `private String from;` | 34 |
| `"metabolicAgeCount"` | `private Integer metabolicAgeCount;` | 38 |
| `"muscleMassCount"` | `private Integer muscleMassCount;` | 42 |
| `"physiqueRatingCount"` | `private Integer physiqueRatingCount;` | 46 |
| `"until"` | `private String until;` | 50 |
| `"visceralFatCount"` | `private Integer visceralFatCount;` | 54 |
| `"weightCount"` | `private Integer weightCount;` | 58 |

## l42.h

Source: `health-stats/sources/l42.h.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `"caloricIntake"` | `private Integer caloricIntake;` | 18 |
| `"date"` | `private String date;` | 22 |
| `"timestampGMT"` | `private String timestampGMT;` | 26 |
| `"version"` | `private Long version;` | 30 |

## l42.i

Source: `health-stats/sources/l42.i.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `"bmi"` | `private Double bmi;` | 17 |
| `"bodyFat"` | `private Double bodyFat;` | 21 |
| `"date"` | `private String date;` | 25 |
| `"dateTimestamp"` | `private String dateTimestamp;` | 29 |
| `"gmtTimestamp"` | `private String gmtTimestamp;` | 33 |
| `"sourceType"` | `private String sourceType;` | 37 |
| `"unitKey"` | `private String unitKey;` | 41 |
| `"value"` | `private Double value;` | 45 |

## l42.j

Source: `health-stats/sources/l42.j.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `"bmi"` | `private final Double bmi;` | 16 |
| `"bodyFat"` | `private final Double bodyFat;` | 20 |
| `"bodyWater"` | `private final Double bodyWater;` | 24 |
| `"boneMass"` | `private final Integer boneMass;` | 28 |
| `"metabolicAge"` | `private final Double metabolicAge;` | 32 |
| `"muscleMass"` | `private final Integer muscleMass;` | 36 |
| `"physiqueRating"` | `private final Integer physiqueRating;` | 40 |
| `"visceralFat"` | `private final Integer visceralFat;` | 44 |
| `"weight"` | `private final Double weight;` | 48 |
| `"sourceType"` | `private String sourceType;` | 52 |

## l42.k

Source: `health-stats/sources/l42.k.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `"dailyWeightSummaries"` | `private List<b> dailyWeightSummaries;` | 20 |
| `"previousDateWeight"` | `private c previousDateWeight;` | 24 |
| `"totalAverage"` | `private g totalAverage;` | 28 |

## o61.p

Source: `health-stats/sources/o61.p.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `"userId"` | `private final long userId;` | 14 |
| `"generic"` | `private final q generic;` | 18 |
| `"cycling"` | `private final q cycling;` | 22 |
| `"rowing"` | `private final q rowing;` | 26 |
| `"heatAltitudeAcclimation"` | `private final x61.e heatAltitudeAcclimation;` | 30 |

## oz1.b

Source: `health-stats/sources/oz1.b.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `"timestampLocal"` | `private final String timestampLocal;` | 21 |
| `"acuteLoad"` | `private final Integer acuteLoad;` | 25 |
| `"hrvWeeklyAverage"` | `private final Integer hrvWeeklyAverage;` | 29 |
| `"primaryActivityTracker"` | `private final Boolean primaryActivityTracker;` | 33 |
| `"minutesSinceLastDive"` | `private Integer minutesSinceLastDive;` | 37 |
| `"acwrFactorFeedback"` | `private final String acwrFactorFeedback;` | 41 |
| `"acwrFactorPercent"` | `private final Integer acwrFactorPercent;` | 45 |
| `"calendarDate"` | `private final String calendarDate;` | 49 |
| `"deviceId"` | `private final Long deviceId;` | 53 |
| `"feedbackLong"` | `private final String feedbackLong;` | 57 |
| `"feedbackShort"` | `private final String feedbackShort;` | 61 |
| `"hrvFactorFeedback"` | `private final String hrvFactorFeedback;` | 65 |
| `"hrvFactorPercent"` | `private final Integer hrvFactorPercent;` | 69 |
| `"inputContext"` | `private final String inputContext;` | 73 |
| `"level"` | `private final String level;` | 77 |
| `"recoveryTime"` | `private final Integer recoveryTime;` | 81 |
| `"recoveryTimeFactorFeedback"` | `private final String recoveryTimeFactorFeedback;` | 85 |
| `"recoveryTimeFactorPercent"` | `private final Integer recoveryTimeFactorPercent;` | 89 |
| `"score"` | `private final Float score;` | 93 |
| `"sleepHistoryFactorFeedback"` | `private final String sleepHistoryFactorFeedback;` | 97 |
| `"sleepHistoryFactorPercent"` | `private final Integer sleepHistoryFactorPercent;` | 101 |
| `"sleepScore"` | `private final Integer sleepScore;` | 105 |
| `"sleepScoreFactorFeedback"` | `private final String sleepScoreFactorFeedback;` | 109 |
| `"sleepScoreFactorPercent"` | `private final Integer sleepScoreFactorPercent;` | 113 |
| `"stressHistoryFactorFeedback"` | `private final String stressHistoryFactorFeedback;` | 117 |
| `"stressHistoryFactorPercent"` | `private final Integer stressHistoryFactorPercent;` | 121 |
| `"timestamp"` | `private final String timestamp;` | 125 |
| `"userProfilePK"` | `private final Integer userProfilePK;` | 129 |
| `"validSleep"` | `private final Boolean validSleep;` | 133 |

## pw.a

Source: `health-stats/sources/pw.a.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `"version"` | `private long version;` | 25 |
| `"systolic"` | `private Double systolic;` | 29 |
| `"diastolic"` | `private Double diastolic;` | 33 |
| `"pulse"` | `private Double pulse;` | 37 |
| `"multiMeasurement"` | `private Boolean multiMeasurement;` | 41 |
| `"notes"` | `private String notes;` | 45 |
| `"sourceType"` | `private String sourceType;` | 49 |
| `"measurementTimestampLocal"` | `private String measurementTimestampLocal;` | 53 |
| `"measurementTimestampGMT"` | `private String measurementTimestampGmt;` | 57 |
| `"categoryName"` | `private String categoryName;` | 61 |

## yw1.a

Source: `health-stats/sources/yw1.a.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `from` | `optional=False` | 37 |
| `until` | `optional=False` | 38 |
| `aggregatedResults` | `optional=False` | 39 |

## yw1.e

Source: `health-stats/sources/yw1.e.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `avgSpeed` | `optional=False` | 39 |
| `avgPower` | `optional=False` | 40 |
| `calories` | `optional=False` | 41 |
| `distance` | `optional=False` | 42 |
| `steps` | `optional=False` | 43 |
| `duration` | `optional=False` | 44 |
| `moderateIntensityMinutes` | `optional=False` | 45 |
| `vigorousIntensityMinutes` | `optional=False` | 46 |
| `movingDuration` | `optional=False` | 47 |
| `totalSets` | `optional=False` | 48 |

## yw1.f

Source: `health-stats/sources/yw1.f.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `avg` | `optional=False` | 36 |
| `count` | `optional=False` | 37 |
| `max` | `optional=False` | 38 |
| `min` | `optional=False` | 39 |
| `sum` | `optional=False` | 40 |

## yw1.g

Source: `health-stats/sources/yw1.g.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `countOfActivities` | `optional=False` | 37 |
| `date` | `optional=False` | 38 |
| `stats` | `optional=False` | 39 |

## yw1.h

Source: `health-stats/sources/yw1.h.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `id` | `optional=False` | 38 |
| `key` | `optional=False` | 39 |
| `visible` | `optional=False` | 40 |
| `sport` | `optional=False` | 41 |
| `maxValue` | `optional=False` | 42 |
| `minValue` | `optional=False` | 43 |

## yw1.i

Source: `health-stats/sources/yw1.i.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `typeId` | `optional=False` | 45 |
| `activityId` | `optional=False` | 46 |
| `activityName` | `optional=False` | 47 |
| `activityType` | `optional=False` | 48 |
| `value` | `optional=False` | 49 |
| `status` | `optional=False` | 50 |
| `prStartTimeGmt` | `optional=False` | 51 |
| `activityStartDateTimeLocalFormatted` | `optional=False` | 52 |
| `prStartTimeLocal` | `optional=False` | 53 |

## yw1.j

Source: `health-stats/sources/yw1.j.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `userId` | `optional=False` | 33 |
| `generic` | `optional=False` | 34 |
| `cycling` | `optional=False` | 35 |

## yw1.l

Source: `health-stats/sources/yw1.l.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `from` | `optional=False` | 36 |
| `series` | `optional=False` | 37 |
| `until` | `optional=False` | 38 |
| `updatedDate` | `optional=False` | 39 |
| `value` | `optional=False` | 40 |

## yw1.s

Source: `health-stats/sources/yw1.s.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `"calendarDate"` | `private final String calendarDate;` | 14 |
| `"exerciseSummaries"` | `private final List<t> exerciseSummaries;` | 18 |

## yw1.t

Source: `health-stats/sources/yw1.t.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `"category"` | `private final String category;` | 14 |
| `"subCategory"` | `private final String subCategory;` | 18 |
| `"totalReps"` | `private final Integer totalReps;` | 22 |
| `"totalSets"` | `private final Integer totalSets;` | 26 |
| `"activeSets"` | `private final Integer activeSets;` | 30 |
| `"totalTimeInSeconds"` | `private final Double totalTimeInSeconds;` | 34 |
| `"totalVolume"` | `private final Double totalVolume;` | 38 |
| `"maxWeight"` | `private final Double maxWeight;` | 42 |

## yw1.v

Source: `health-stats/sources/yw1.v.java`

| Wire annotation/name | Type/declaration or serializer optional | Line |
|---|---|---|
| `calendarDate` | `optional=False` | 34 |
| `vo2MaxValue` | `optional=False` | 35 |
| `vo2MaxPreciseValue` | `optional=False` | 36 |
