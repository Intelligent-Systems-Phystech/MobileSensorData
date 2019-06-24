# Организация сбора данных сенсоров мобильного телефона

**Scientific purpose:** to analyse invariant property and composition of movements hypothesis.

**Engineering purpose:** to create human movement IMU signals database that is to be NIST standard in the orientation field.

### Collecting data

All experiments have to be performed in Sensor Kinetics Pro application. **Links**: [Android](https://play.google.com/store/apps/details?id=com.innoventions.sensorkineticspro&hl=ru), [iOS](https://apps.apple.com/us/app/sensor-kinetics-pro/id623633248)

0. Uncheck Time/Date Stamp parameter in settings.

1. Record data in Multi-Sensor mode with `max rate` set to FASTEST.

2. Save data.
  - Press `More/Files&Sharing'
  - Appplication directory will be opened.
  - Press **Save** icon to save data.
  - Enter `filename` according to **File naming** rule described below.
  - Skip saving logs.
  - Tap to created `.msc` file.
  - Press `Share` and `Convert to CSV`.
  - `.csv` file for each sensor will be created in application directory.
 
 3. Send `.csv` files.
 
##### File naming
Data file have to be named according to this expression:
> **[game]**\_**[g]**\_**[h]**\_**[w]**\_**[ss]**\_**[note]**\_**[sensor]**.csv

 * **[game** - name of played game
 * **[g]** - gender (**m** - male/**f** - female)
 * **[h]** - height (cm)
 * **[w]** - weight (kg)
 * **[ss]** - shoe size (eu)
 * **[note]** - additional information about person: *slim-jim, normal, athletic, fat,  limps* (optional)
 * **[sensor]** - sensor abbreviation: *accm, grvm, gyrm, lacm, magm, rotm*. Added automatically while converting data to `.csv` in SensorKinetics.

**Example**
Accelerometer data of game "Stairs" played by female with 157cm height, 47kg weight and 36eu shoe size: 
> Stairs_f_157_47_36_accm.csv
