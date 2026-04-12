#!/usr/bin/env python3
"""
Transform the Toronto Places HTML file to use Leaflet.js instead of SVG map
"""

# Read the original file
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the line numbers for the SVG map section
svg_start = None
svg_end = None

for i, line in enumerate(lines):
    if '<!-- ===== Interactive SVG Map =====' in line:
        svg_start = i
    if svg_start and '</section>' in line and 'map-section' in ''.join(lines[max(0,i-5):i+1]):
        svg_end = i + 1
        break

print(f"SVG section: lines {svg_start} to {svg_end}")

# Create the new map section
new_map_section = '''  <!-- ===== Interactive Leaflet Map ===== -->
  <section class="map-section">
    <div class="map-frame">
      <div id="map"></div>
    </div>
  </section>

'''

# Replace the SVG section with Leaflet map
new_lines = lines[:svg_start] + [new_map_section] + lines[svg_end:]

# Write the new file
with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Map section replaced successfully!")
