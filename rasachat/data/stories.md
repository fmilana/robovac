## go_back_to_base
* go_back_to_base
  - action_reset_slots
  - action_check_entities
  - action_go_back_to_base

## clean
* clean
  - action_reset_slots
  - action_check_entities
  - slot{"location":null,"time":null}
  - utter_where_should_i_clean
* specify_where
  - action_check_entities
  - slot{"location":"by the sink","time":null}
  - action_clean

## clean_there
* clean
  - action_reset_slots
  - action_check_entities
  - slot{"location":"around the table","time":null}
  - action_clean

## clean_there_at_this_time
* clean
  - action_reset_slots
  - action_check_entities
  - slot{"location":"behind the tanks","time":"2 pm"}
  - action_clean

## how_long_left
* how_long_left
  - action_how_long_left

## what_are_you_doing
* what_are_you_doing
  - action_what_am_i_doing

## bin
* bin
  - action_bin

## battery
* battery
  - action_battery

## stop
* stop
  - action_stop

## are_you_at_base
* are_you_at_base
  - action_am_i_at_base

## no
* no
  - utter_okay
