# Project Summary: Star Wars Light Sensor Music System

## Overview
Built a light-sensor controlled music system on a SLATE Experimenter's Board that plays different Star Wars themes based on ambient light levels using MicroPython.

---

## Hardware Configuration

### SLATE Experimenter's Board (Stensat Group LLC, 2022)
- **Speaker:** Pin 1
- **LED 1:** Pin 0 (available but not currently used)
- **Light Sensor:** Pin 26
- **Pin Range:** 0-15 (pins only go up to 15)
- **Programming:** MicroPython with `machine` library

### Light Sensor Behavior
- **Covered/Dark:** ~1.50V (higher voltage)
- **Flashlight/Bright:** ~1.30V (lower voltage)
- **Note:** Sensor operates inversely - darker = higher voltage, brighter = lower voltage
- **Threshold Set:** 1.4V

---

## Project Structure

### Three Python Files Created:

#### 1. `imperial_march.py`
- Dark Side theme (Darth Vader)
- Lower octave notes for ominous sound
- Uses frequencies: C_low (131Hz) through G_mid (392Hz)
- Function: `build_imperial_march()` returns notes, durations, and pauses
- Function: `perform_melody()` plays the song
- Function: `stop_speaker()` for cleanup
- ~15 seconds playtime, 29 notes total
- Speaker on Pin 1

#### 2. `star_wars_theme.py`
- Heroes/Light Side theme (Main fanfare)
- Higher octave notes for heroic sound
- Uses frequencies: C (262Hz) through A2 (880Hz)
- Function: `create_star_wars_theme()` returns notes, durations, and pauses
- Function: `play_song()` plays the song
- Function: `cleanup()` for cleanup
- ~15 seconds playtime with heroic fanfare
- Speaker on Pin 1

#### 3. `main.py`
- Main control program
- Imports both song modules
- Reads light sensor on Pin 26
- Threshold logic: 1.4V
  - `> 1.4V` (darker/covered) → Imperial March
  - `< 1.4V` (brighter/flashlight) → Star Wars Theme
- Continuous loop checking sensor every 2 seconds after each song
- Proper error handling and cleanup

---

## Key Technical Details

### MicroPython Syntax Used:
```python
from machine import Pin, PWM, ADC
speaker = PWM(Pin(SPEAKER_PIN))
speaker.freq(frequency)
speaker.duty_u16(30000)  # Volume control
light_sensor = ADC(Pin(26))
voltage = (light_sensor.read_u16() / 65535) * 3.3
```

### Song Structure:
Each song uses three parallel arrays:
1. **Notes array:** Musical note names as strings
2. **Durations array:** How long each note plays (seconds)
3. **Pauses array:** Gap between notes for smooth flow (seconds)

### Smooth Transitions:
- Variable pause lengths between notes (0.0s to 0.2s)
- Some notes flow directly together (0.0s pause)
- Strategic pauses for dramatic effect
- Prevents "blocky" sound by varying timing

---

## Testing Results

### Light Sensor Pin Discovery:
Tested pins 26, 27, 28:
- **Pin 26:** Responsive to light changes (0.16V-1.60V range) ✓
- **Pin 27:** Constant ~3.0V (voltage reference)
- **Pin 28:** Constant ~1.8V (different sensor)

### Threshold Determination:
- Initial threshold: 1.7V (too high, never reached)
- Tested range: 1.30V (bright) to 1.50V (dark)
- Final threshold: 1.4V (optimal for switching)

---

## Previous Work Completed

### Earlier Assignments (Separate Projects):
1. **traffic_light.py** - Basic TrafficLight class with phase cycling
2. **upgraded_traffic_light.py** - Added start() and set_cycle() methods
3. **enum_traffic_light.py** - Used Enum for phases instead of strings
4. **traffic_light_forecast.py** - Added forecast() method
5. **traffic_light_property.py** - Property validation for yellow_s
6. **school_zone_light.py** - Inheritance subclass example

All saved in: `C:\Users\osman\PycharmProjects\`

---

## How to Run

1. Ensure all three files in same directory on SLATE board
2. Files must be named exactly (case-sensitive):
   - `imperial_march.py`
   - `star_wars_theme.py`
   - `main.py`
3. Run `main.py` in Thonny
4. Cover sensor with hand → Imperial March plays
5. Shine flashlight on sensor → Star Wars Theme plays
6. Press Ctrl+C to stop

---

## Video Recording Setup

For demonstration:
- Show console output displaying light levels
- Cover sensor to trigger Imperial March (Dark Side)
- Uncover/flash sensor to trigger Star Wars Theme (Light Side)
- Display shows which theme is playing and why
- Demonstrates threshold logic and sensor input/output

---

## Important Notes

- MicroPython environment (not standard Python)
- No localStorage/sessionStorage in this context
- Speaker uses PWM for tone generation
- Light sensor ADC reads 16-bit values converted to voltage
- Inverse light sensor behavior is normal for this board
- All code is original implementations inspired by musical structure