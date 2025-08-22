using ComplianceMonitor.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

namespace ComplianceMonitor.Services
{
    public class OpenAILLMService : ILLMService
    {
        private readonly HttpClient _httpClient;
        private readonly string _apiKey;

        public OpenAILLMService(string apiKey)
        {
            _httpClient = new HttpClient();
            _apiKey = apiKey;
        }

        public async Task<ComplianceSummary> AnalyzeChunkAsync(string chunkTitle, string chunkContent)
        {
            var prompt = $@"
You are a legal compliance analyst. Summarize the following regulation section and extract any compliance deadlines.

Title: {chunkTitle}
Content: {chunkContent}
";

            var requestBody = new
            {
                model = "gpt-4",
                messages = new[]
                {
                new { role = "system", content = "You analyze legal regulations and extract summaries and deadlines." },
                new { role = "user", content = prompt }
            }
            };

            var request = new HttpRequestMessage(HttpMethod.Post, "https://api.openai.com/v1/chat/completions")
            {
                Content = new StringContent(JsonSerializer.Serialize(requestBody), Encoding.UTF8, "application/json")
            };
            request.Headers.Add("Authorization", $"Bearer {_apiKey}");

            var response = await _httpClient.SendAsync(request);
            var result = await response.Content.ReadAsStringAsync();

            // Simplified parsing
            var brief = result.Substring(0, Math.Min(500, result.Length));
            var followUp = DateTime.Today.AddDays(30); // Placeholder

            return new ComplianceSummary
            {
                ChunkTitle = chunkTitle,
                Brief = brief,
                FollowUpDate = followUp
            };
        }
    }

}
