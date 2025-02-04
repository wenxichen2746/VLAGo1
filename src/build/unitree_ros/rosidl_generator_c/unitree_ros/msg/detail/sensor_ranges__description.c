// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from unitree_ros:msg/SensorRanges.idl
// generated code does not contain a copyright notice

#include "unitree_ros/msg/detail/sensor_ranges__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_unitree_ros
const rosidl_type_hash_t *
unitree_ros__msg__SensorRanges__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x6b, 0x56, 0x9a, 0xe4, 0x82, 0xf7, 0x08, 0x9c,
      0xa5, 0x2f, 0xf0, 0x67, 0xe3, 0x4a, 0x8e, 0x1f,
      0xd7, 0x96, 0xde, 0x20, 0xb6, 0xe0, 0x6d, 0x2b,
      0x74, 0xe9, 0xa4, 0x0c, 0x2f, 0xa4, 0xd8, 0x6e,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char unitree_ros__msg__SensorRanges__TYPE_NAME[] = "unitree_ros/msg/SensorRanges";

// Define type names, field names, and default values
static char unitree_ros__msg__SensorRanges__FIELD_NAME__front[] = "front";
static char unitree_ros__msg__SensorRanges__FIELD_NAME__left[] = "left";
static char unitree_ros__msg__SensorRanges__FIELD_NAME__right[] = "right";

static rosidl_runtime_c__type_description__Field unitree_ros__msg__SensorRanges__FIELDS[] = {
  {
    {unitree_ros__msg__SensorRanges__FIELD_NAME__front, 5, 5},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {unitree_ros__msg__SensorRanges__FIELD_NAME__left, 4, 4},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {unitree_ros__msg__SensorRanges__FIELD_NAME__right, 5, 5},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
unitree_ros__msg__SensorRanges__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {unitree_ros__msg__SensorRanges__TYPE_NAME, 28, 28},
      {unitree_ros__msg__SensorRanges__FIELDS, 3, 3},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "float32 front\n"
  "float32 left\n"
  "float32 right ";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
unitree_ros__msg__SensorRanges__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {unitree_ros__msg__SensorRanges__TYPE_NAME, 28, 28},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 42, 42},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
unitree_ros__msg__SensorRanges__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *unitree_ros__msg__SensorRanges__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
