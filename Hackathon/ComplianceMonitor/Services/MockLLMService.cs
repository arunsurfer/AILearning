using ComplianceMonitor.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ComplianceMonitor.Services
{
    public class MockLLMService : ILLMService
    {
        public Task<ComplianceSummary> AnalyzeChunkAsync(string chunkTitle, string chunkContent)
        {
            throw new NotImplementedException();
        }
    }
}
