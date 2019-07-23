// <auto-generated>
// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License. See License.txt in the project root for
// license information.
//
// Code generated by Microsoft (R) AutoRest Code Generator 1.0.0.0
// Changes may cause incorrect behavior and will be lost if the code is
// regenerated.
// </auto-generated>

namespace Microsoft.Azure.IIoT.Opc.History.Models
{
    using Newtonsoft.Json;
    using Newtonsoft.Json.Converters;
    using System.Runtime;
    using System.Runtime.Serialization;

    /// <summary>
    /// Defines values for SecurityAssessment.
    /// </summary>
    [JsonConverter(typeof(StringEnumConverter))]
    public enum SecurityAssessment
    {
        [EnumMember(Value = "Unknown")]
        Unknown,
        [EnumMember(Value = "Low")]
        Low,
        [EnumMember(Value = "Medium")]
        Medium,
        [EnumMember(Value = "High")]
        High
    }
    internal static class SecurityAssessmentEnumExtension
    {
        internal static string ToSerializedValue(this SecurityAssessment? value)
        {
            return value == null ? null : ((SecurityAssessment)value).ToSerializedValue();
        }

        internal static string ToSerializedValue(this SecurityAssessment value)
        {
            switch( value )
            {
                case SecurityAssessment.Unknown:
                    return "Unknown";
                case SecurityAssessment.Low:
                    return "Low";
                case SecurityAssessment.Medium:
                    return "Medium";
                case SecurityAssessment.High:
                    return "High";
            }
            return null;
        }

        internal static SecurityAssessment? ParseSecurityAssessment(this string value)
        {
            switch( value )
            {
                case "Unknown":
                    return SecurityAssessment.Unknown;
                case "Low":
                    return SecurityAssessment.Low;
                case "Medium":
                    return SecurityAssessment.Medium;
                case "High":
                    return SecurityAssessment.High;
            }
            return null;
        }
    }
}
