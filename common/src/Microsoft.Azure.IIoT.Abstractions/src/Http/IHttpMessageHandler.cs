﻿// ------------------------------------------------------------
//  Copyright (c) Microsoft Corporation.  All rights reserved.
//  Licensed under the MIT License (MIT). See License.txt in the repo root for license information.
// ------------------------------------------------------------

namespace Microsoft.Azure.IIoT.Http {
    using System.Net;
    using System.Net.Http;
    using System.Net.Http.Headers;
    using System.Threading;
    using System.Threading.Tasks;

    /// <summary>
    /// Handles requests and responses in the client chain, but 
    /// injectable using dependency injection, e.g Autofac.
    /// </summary>
    public interface IHttpMessageHandler : IHttpHandler {

        /// <summary>
        /// Relative order to other handlers
        /// </summary>
        int Order { get; }

        /// <summary>
        /// Handle request
        /// </summary>
        /// <param name="resourceId"></param>
        /// <param name="headers"></param>
        /// <param name="content"></param>
        /// <param name="cancellationToken"></param>
        Task OnRequestAsync(string resourceId, HttpRequestHeaders headers,
            HttpContent content, CancellationToken cancellationToken);

        /// <summary>
        /// Handle response
        /// </summary>
        /// <param name="resourceId"></param>
        /// <param name="statusCode"></param>
        /// <param name="headers"></param>
        /// <param name="content"></param>
        /// <param name="cancellationToken"></param>
        Task OnResponseAsync(string resourceId, HttpStatusCode statusCode,
            HttpResponseHeaders headers, HttpContent content,
            CancellationToken cancellationToken);
    }
}