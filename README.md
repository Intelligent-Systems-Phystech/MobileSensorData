# Coordination of mobile sensor data collection

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
 
### File naming
Data file have to be named according to this expression:
> **[game]**\_**[g]**\_**[h]**\_**[w]**\_**[ss]**\_**[note]**\_**[sensor]**.csv

 * **[game]** - name of played game
 * **[g]** - gender (**m** - male/**f** - female)
 * **[h]** - height (cm)
 * **[w]** - weight (kg)
 * **[ss]** - shoe size (eu)
 * **[note]** - additional information about person: *slim-jim, normal, athletic, fat,  limps* (optional)
 * **[sensor]** - sensor abbreviation: *accm, grvm, gyrm, lacm, magm, rotm*. Added automatically while converting data to `.csv` in SensorKinetics.

**Example**
Accelerometer data of game "Stairs" played by female with 157cm height, 47kg weight and 36eu shoe size: 
> Stairs_f_157_47_36_accm.csv


### Games

A. Hold the phone in your right hand (for right-handed)  
B. Put the phone in your right front pocket (for hight-handed).


1. **Stairs**
 * Place yourself in a corridor near U-shaped stairs.
 * Switch the software, act as usual (for example, be calm).
 * Wait one second between the following items.

  1. Go 12 steps forward and back again.
  2. Pick up a plastic bag with a bottle of water 1 Liter.
  3. Run 12 steps forward and back again.
  4. Run with a bag.
  5. Go upstairs 3 ladders up and down again.
  6. Go with a bag.
  
  
2. **Slam**
  1. Walking with a turn: 20 steps, a turn of 90 degrees, 20 steps, turn again (three squares (left and right))
  2. Walking square eight (walk around the perimeter of the second and fourth quarter of the coordinate plane)
  
3. **Phone**
 * The application should not be minimized because the sensor readings are not recorded in the background.
  1. Simulate writing а message (10 s)
  2. Simulate a telephone conversation (30 s)

4. **Dormitory**
  1. Sit down/up a chair (5 times)
  2. Raise / put a mug on the table (5 times)
  3. Open and close the door (1 time)
  4. Lie down on the bed and get out of bed (1 time)

