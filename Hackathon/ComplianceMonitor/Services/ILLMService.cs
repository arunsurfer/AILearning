using ComplianceMonitor.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

namespace ComplianceMonitor.Services
{
    public interface ILLMService
    {
        Task<ComplianceSummary> AnalyzeChunkAsync(string chunkTitle, string chunkContent);
    }
}
