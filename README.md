# InteractiveChatUI

Build Chat UI component for structured Exa search.

Let's create a chat interface prototype that handles text-based conversations and incorporates dynamic UI elements based on model responses.

Technologies available for use in this prototype:

- [Vercel AI SDK Core](https://sdk.vercel.ai/docs/ai-sdk-core/overview)
- [Vercel AI SDK UI](https://sdk.vercel.ai/docs/ai-sdk-ui/overview)
- [Exa Search API](https://docs.exa.ai/sdks/python-sdk-specification#getting-started)
- [Exa MCP Server](https://docs.exa.ai/examples/exa-mcp)

inspiration: <https://github.com/JamesSloan/VercelGenUI_MCP>

## Principle

Let X an agent that takes natural language queries and returns structured search result schemas and calls the Exa Search API to get the data with the schema and generate a UI based on the schema.

- Vercel AI SDK Core => create a chat agent that can process natural language queries and return structured search result schemas.
- Vercel UI SDK => create a chat UI that allows users to interact with the Exa Search API in a conversational manner.
- Exa Search API => provide real-time web search capabilities based on the schema defined by the agent.

### Vercel Generative User Interface

Generative user interfaces (generative UI) is the process of allowing a large language model (LLM) to go beyond text and "generate UI". This creates a more engaging and AI-native experience for users.

### Exa MCP

Exa MCP Server enables AI assistants like Claude to perform real-time web searches through the Exa Search API, allowing them to access up-to-date information from the internet in a safe and controlled way.

- Real-time web searches with optimized results
- Structured search responses (titles, URLs, content snippets)
- Support for specialized search types (web, academic, social media, etc.)
​
Exa MCP includes several specialized search tools:

| Tool | Description |
| --- | --- |
| web_search | General web search with optimized results and content extraction |
| research_paper_search | Specialized search focused on academic papers and research content |
| twitter_search | Finds tweets, profiles, and conversations on Twitter/X |
| company_research | Gathers detailed information about businesses by crawling company websites |
| crawling | Extracts content from specific URLs (articles, PDFs, web pages) |
| competitor_finder | Identifies competitors of a company by finding businesses with similar offerings |
