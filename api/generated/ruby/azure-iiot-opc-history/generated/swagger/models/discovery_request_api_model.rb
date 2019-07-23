# encoding: utf-8
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator 1.0.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.

module azure.iiot.opc.history
  module Models
    #
    # Discovery request
    #
    class DiscoveryRequestApiModel
      # @return [String] Id of discovery request
      attr_accessor :id

      # @return [DiscoveryMode] Discovery mode to use. Possible values include:
      # 'Off', 'Local', 'Network', 'Fast', 'Scan'
      attr_accessor :discovery

      # @return [DiscoveryConfigApiModel] Scan configuration to use
      attr_accessor :configuration


      #
      # Mapper for DiscoveryRequestApiModel class as Ruby Hash.
      # This will be used for serialization/deserialization.
      #
      def self.mapper()
        {
          client_side_validation: true,
          required: false,
          serialized_name: 'DiscoveryRequestApiModel',
          type: {
            name: 'Composite',
            class_name: 'DiscoveryRequestApiModel',
            model_properties: {
              id: {
                client_side_validation: true,
                required: false,
                serialized_name: 'id',
                type: {
                  name: 'String'
                }
              },
              discovery: {
                client_side_validation: true,
                required: false,
                serialized_name: 'discovery',
                type: {
                  name: 'Enum',
                  module: 'DiscoveryMode'
                }
              },
              configuration: {
                client_side_validation: true,
                required: false,
                serialized_name: 'configuration',
                type: {
                  name: 'Composite',
                  class_name: 'DiscoveryConfigApiModel'
                }
              }
            }
          }
        }
      end
    end
  end
end
