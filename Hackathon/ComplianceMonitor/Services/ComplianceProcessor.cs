using ComplianceMonitor.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ComplianceMonitor.Services
{
    public class ComplianceProcessor
    {
        private readonly ILLMService _llmService;

        public ComplianceProcessor(ILLMService llmService)
        {
            _llmService = llmService;
        }

        public async Task<List<ComplianceSummary>> ProcessAsync(string fullText)
        {
            var chunks = ChunkText(fullText);
            var summaries = new List<ComplianceSummary>();

            foreach (var (title, content) in chunks)
            {
                var summary = await _llmService.AnalyzeChunkAsync(title, content);
                summaries.Add(summary);
            }

            return summaries;
        }

        private List<(string Title, string Content)> ChunkText(string text)
        {
            var paragraphs = text.Split("\n\n", StringSplitOptions.RemoveEmptyEntries);
            var chunks = new List<(string, string)>();

            for (int i = 0; i < paragraphs.Length; i += 3)
            {
                var title = $"Section {i / 3 + 1}";
                var content = string.Join("\n\n", paragraphs.Skip(i).Take(3));
                chunks.Add((title, content));
            }

            return chunks;
        }
    }
}
