#!/usr/bin/env bash

# Temporary, waiting on ReadyMade TUI
# depends on kwin

sudo echo "#!/usr/bin/env bash

kwin readymade" > /usr/bin/run-readymade

chmod +x /usr/bin/run-readymade
