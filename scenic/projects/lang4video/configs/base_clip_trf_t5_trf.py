# Copyright 2024 The Scenic Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Base config for CLIP + T5 w Transformers."""

import ml_collections
from scenic.projects.lang4video.configs import base_clip
from scenic.projects.lang4video.configs import base_clip_t5


def get_config(run_local: str = '') -> ml_collections.ConfigDict:
  """Returns the experiment configuration."""
  config = base_clip_t5.get_config(run_local)

  config.experiment_name = 'clip_trf_t5_trf'

  del config.model.image_encoder.config_name
  del config.model.text_encoder.config_name

  config.model.num_heads = 12
  config.model.head_dim = 64
  config.model.mlp_dim = 2048
  config.model.num_layers = 1
  config.model.dropout_rate = 0.0
  config.model.activations = ('gelu', 'linear')

  config.model.image_encoder_name = 'sequential'
  config.model.image_encoder.encoders = ml_collections.ConfigDict()
  config.model.image_encoder.encoders.a = ml_collections.ConfigDict()
  config.model.image_encoder.encoders.a.encoder_name = 'clip'
  config.model.image_encoder.encoders.a.encoder = ml_collections.ConfigDict()
  config.model.image_encoder.encoders.a.encoder.config_name = 'vit_b32'
  config.model.image_encoder.encoders.a.encoder.return_all_tokens = True
  config.model.image_encoder.encoders.b = ml_collections.ConfigDict()
  config.model.image_encoder.encoders.b.encoder_name = 'transformer'
  config.model.image_encoder.encoders.b.encoder = ml_collections.ConfigDict()
  config.model.image_encoder.encoders.b.encoder.num_heads = config.model.get_ref(
      'num_heads')
  config.model.image_encoder.encoders.b.encoder.head_dim = config.model.get_ref(
      'head_dim')
  config.model.image_encoder.encoders.b.encoder.mlp_dim = config.model.get_ref(
      'mlp_dim')
  config.model.image_encoder.encoders.b.encoder.num_layers = config.model.get_ref(
      'num_layers')
  config.model.image_encoder.encoders.b.encoder.dropout_rate = config.model.get_ref(
      'dropout_rate')
  config.model.image_encoder.encoders.b.encoder.activations = config.model.get_ref(
      'activations')

  config.model.text_encoder_name = 'sequential'
  config.model.text_encoder.encoders = ml_collections.ConfigDict()
  config.model.text_encoder.encoders.a = ml_collections.ConfigDict()
  config.model.text_encoder.encoders.a.encoder_name = 't5'
  config.model.text_encoder.encoders.a.encoder = ml_collections.ConfigDict()
  config.model.text_encoder.encoders.a.encoder.config_name = 'base'
  config.model.text_encoder.encoders.a.encoder.return_all_tokens = True
  config.model.text_encoder.encoders.b = ml_collections.ConfigDict()
  config.model.text_encoder.encoders.b.encoder_name = 'transformer'
  config.model.text_encoder.encoders.b.encoder = ml_collections.ConfigDict()
  config.model.text_encoder.encoders.b.encoder.num_heads = config.model.get_ref(
      'num_heads')
  config.model.text_encoder.encoders.b.encoder.head_dim = config.model.get_ref(
      'head_dim')
  config.model.text_encoder.encoders.b.encoder.mlp_dim = config.model.get_ref(
      'mlp_dim')
  config.model.text_encoder.encoders.b.encoder.num_layers = config.model.get_ref(
      'num_layers')
  config.model.text_encoder.encoders.b.encoder.dropout_rate = config.model.get_ref(
      'dropout_rate')
  config.model.text_encoder.encoders.b.encoder.activations = config.model.get_ref(
      'activations')

  # The following configurations are meant to be used by DMVR datasets but also
  # as input to other parts of the config.

  config.dataset_configs.min_resize = base_clip.get_clip_image_size(
      config.model.image_encoder.encoders.a.encoder.config_name)
  config.dataset_configs.crop_size = base_clip.get_clip_image_size(
      config.model.image_encoder.encoders.a.encoder.config_name)

  return config
