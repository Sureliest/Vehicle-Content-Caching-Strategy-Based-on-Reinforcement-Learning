# set number of nodes
set opt(nn) 196.0

# set activity file
set opt(af) $opt(config-path)
append opt(af) //home/zwl/eclipse_workspace/center_controller/mapdata/grid/grid.activity.tcl

# set mobility file
set opt(mf) $opt(config-path)
append opt(mf) //home/zwl/eclipse_workspace/center_controller/mapdata/grid/grid.mobility.tcl

# set start/stop time
set opt(start) 0.0
set opt(stop) 309.0

# set floor size
set opt(x) 1659
set opt(y) 1933
set opt(min-x) -12
set opt(min-y) -12
