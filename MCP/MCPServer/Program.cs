using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;
using System.Diagnostics; 

var builder = Host.CreateApplicationBuilder(args);

// 🔊 Enable detailed logging
builder.Logging.AddConsole(options => {
    options.LogToStandardErrorThreshold = LogLevel.Trace;
});

// 🧩 Register MCP server with STDIO transport
builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithToolsFromAssembly(typeof(EchoTool).Assembly); // Scan current assembly for tools

await builder.Build().RunAsync();

// 🔧 Define your MCP tools
[McpServerToolType]
public static class EchoTool
{
    [McpServerTool, Description("Echoes the message back to the client.")]
    public static string Echo(string message) => $"Hello from MCP: {message}";

    [McpServerTool, Description("Returns the message in reverse.")]
    public static string ReverseEcho(string message) {
       Debugger.Break(); // This will prompt to launch the debugger if not already attached
        Console.Error.WriteLine($"[DEBUG] ReverseEcho called with: {message}");


        char[] charArray = message.ToCharArray();
        Array.Reverse(charArray);
        return new string(charArray);
    }
}