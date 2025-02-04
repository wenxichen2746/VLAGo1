// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from unitree_ros:msg/BmsState.idl
// generated code does not contain a copyright notice

#include "unitree_ros/msg/detail/bms_state__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_unitree_ros
const rosidl_type_hash_t *
unitree_ros__msg__BmsState__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x75, 0xc8, 0xf3, 0x98, 0x23, 0xe6, 0xce, 0x57,
      0xa6, 0x63, 0xa9, 0xd6, 0xd7, 0xfc, 0x5e, 0x39,
      0x44, 0x41, 0x0e, 0xfd, 0x0e, 0xc8, 0x75, 0xad,
      0xd7, 0xea, 0xa7, 0x25, 0xed, 0xfe, 0x91, 0x85,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char unitree_ros__msg__BmsState__TYPE_NAME[] = "unitree_ros/msg/BmsState";

// Define type names, field names, and default values
static char unitree_ros__msg__BmsState__FIELD_NAME__version_h[] = "version_h";
static char unitree_ros__msg__BmsState__FIELD_NAME__version_l[] = "version_l";
static char unitree_ros__msg__BmsState__FIELD_NAME__bms_status[] = "bms_status";
static char unitree_ros__msg__BmsState__FIELD_NAME__soc[] = "soc";
static char unitree_ros__msg__BmsState__FIELD_NAME__current[] = "current";
static char unitree_ros__msg__BmsState__FIELD_NAME__cycle[] = "cycle";
static char unitree_ros__msg__BmsState__FIELD_NAME__bq_ntc[] = "bq_ntc";
static char unitree_ros__msg__BmsState__FIELD_NAME__mcu_ntc[] = "mcu_ntc";
static char unitree_ros__msg__BmsState__FIELD_NAME__cell_vol[] = "cell_vol";

static rosidl_runtime_c__type_description__Field unitree_ros__msg__BmsState__FIELDS[] = {
  {
    {unitree_ros__msg__BmsState__FIELD_NAME__version_h, 9, 9},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_UINT8,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {unitree_ros__msg__BmsState__FIELD_NAME__version_l, 9, 9},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_UINT8,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {unitree_ros__msg__BmsState__FIELD_NAME__bms_status, 10, 10},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_UINT8,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {unitree_ros__msg__BmsState__FIELD_NAME__soc, 3, 3},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_UINT8,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {unitree_ros__msg__BmsState__FIELD_NAME__current, 7, 7},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT32,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {unitree_ros__msg__BmsState__FIELD_NAME__cycle, 5, 5},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_UINT16,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {unitree_ros__msg__BmsState__FIELD_NAME__bq_ntc, 6, 6},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT8_ARRAY,
      2,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {unitree_ros__msg__BmsState__FIELD_NAME__mcu_ntc, 7, 7},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT8_ARRAY,
      2,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {unitree_ros__msg__BmsState__FIELD_NAME__cell_vol, 8, 8},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_UINT16_ARRAY,
      10,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
unitree_ros__msg__BmsState__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {unitree_ros__msg__BmsState__TYPE_NAME, 24, 24},
      {unitree_ros__msg__BmsState__FIELDS, 9, 9},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "#  This message is a fork from https://github.com/unitreerobotics/unitree_ros_to_real/tree/master/unitree_legged_msgs\n"
  "uint8 version_h\n"
  "uint8 version_l\n"
  "uint8 bms_status\n"
  "uint8 soc                  # SOC 0-100%\n"
  "int32 current              # mA\n"
  "uint16 cycle\n"
  "int8[2] bq_ntc             # x1 degrees centigrade\n"
  "int8[2] mcu_ntc            # x1 degrees centigrade\n"
  "uint16[10] cell_vol        # cell voltage mV";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
unitree_ros__msg__BmsState__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {unitree_ros__msg__BmsState__TYPE_NAME, 24, 24},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 398, 398},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
unitree_ros__msg__BmsState__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *unitree_ros__msg__BmsState__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
