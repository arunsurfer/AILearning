// See https://aka.ms/new-console-template for more information
using ComplianceMonitor.Models;
using ComplianceMonitor.Services;
using Microsoft.Extensions.Configuration;
using System.Text.Json;

using Microsoft.Extensions.Configuration;
using ComplianceMonitor.Services;

class Program
{
    static async Task Main(string[] args)
    {
        var config = new ConfigurationBuilder()
            .SetBasePath(AppContext.BaseDirectory)
            .AddJsonFile("appsettings.json")
            .Build();

        ILLMService llmService = config["LLMProvider"] switch
        {
            "OpenAI" => new OpenAILLMService(config["OpenAI:ApiKey"]),
            // Add ClaudeLLMService and GeminiLLMService here later
            _ => throw new Exception("Unsupported LLM provider")
        };

        var processor = new ComplianceProcessor(llmService);

        var textPath = Path.Combine(AppContext.BaseDirectory, "compliance_data.json");
        var fullText = await File.ReadAllTextAsync(textPath);

        var summaries = await processor.ProcessAsync(fullText);

        foreach (var summary in summaries)
        {
            Console.WriteLine($"\n {summary.ChunkTitle}");
            Console.WriteLine(summary.Brief);
            Console.WriteLine($"Follow-up: {summary.FollowUpDate?.ToString("yyyy-MM-dd")}");
        }
    }
}