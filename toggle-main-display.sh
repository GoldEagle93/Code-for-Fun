#!/bin/bash

# Set PATH to include Homebrew binaries
export PATH="/opt/homebrew/bin:/usr/local/bin:$PATH"

# Display IDs and resolutions
INTERNAL_ID="37D8832A-2D66-02CA-B9F7-8F30A301B230"
EXTERNAL_ID="6F8964A3-6212-48CD-867C-87C38102DFCD"
INTERNAL_RES="1728x1117"
EXTERNAL_RES="1728x1117"
EXTENDED_RES="2560x1440"
ARRANGEMENT="-1728,212"

# Debug: Print displayplacer output
echo "Running displayplacer list..."
displayplacer list > /tmp/displayplacer_output.txt
echo "Output saved to /tmp/displayplacer_output.txt"

# Check if external display is present
EXTERNAL_PRESENT=$(grep "Persistent screen id: $EXTERNAL_ID" /tmp/displayplacer_output.txt)
if [[ -z "$EXTERNAL_PRESENT" ]]; then
    echo "Error: External display ($EXTERNAL_ID) not detected."
    exit 1
fi

# Check if external display is enabled
EXTERNAL_ENABLED=$(grep -A 12 "Persistent screen id: $EXTERNAL_ID" /tmp/displayplacer_output.txt | grep "Enabled" | awk '{print $2}')
if [[ "$EXTERNAL_ENABLED" != "true" ]]; then
    echo "Error: External display is not enabled."
    exit 1
fi

# Check if currently mirroring (look for combined ID or same resolution/origin)
MIRROR_STATE=$(grep "id:$INTERNAL_ID+$EXTERNAL_ID" /tmp/displayplacer_output.txt)
if [[ -n "$MIRROR_STATE" ]]; then
    echo "Currently mirroring, switching to extended mode (external as main)..."
    # displayplacer "id:$EXTERNAL_ID res:$EXTERNAL_RES hz:60 scaling:on origin:(0,0) degree:0" "id:$INTERNAL_ID res:$INTERNAL_RES hz:120 scaling:on origin:(1728,0) degree:0"
    displayplacer "id:$EXTERNAL_ID res:$EXTENDED_RES hz:60 scaling:on origin:(0,0) degree:0" "id:$INTERNAL_ID res:$INTERNAL_RES hz:120 scaling:on origin:($ARRANGEMENT) degree:0"
else
    echo "Not mirroring, switching to mirroring (internal as main)..."
    displayplacer "id:$INTERNAL_ID+$EXTERNAL_ID res:$INTERNAL_RES hz:120 color_depth:8 enabled:true scaling:on origin:(0,0) degree:0"
fi