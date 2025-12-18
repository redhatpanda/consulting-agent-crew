# Company Knowledge Base

This directory contains the company knowledge base that powers RAG (Retrieval-Augmented Generation) for the consulting crew agents.

## Overview

The knowledge base enables all agents to:
- Access company-specific information automatically through RAG
- Search company documents using semantic search tools
- Maintain context about company strategy, capabilities, and organizational information
- Generate recommendations that align with company values and strategic priorities

## Knowledge Base Structure

```
knowledge/
├── company_overview.md          # Company profile, mission, values, structure
├── company_strategy.md          # Strategic initiatives, frameworks, decisions
├── company_capabilities.md      # Core capabilities, resources, gaps
├── user_preference.txt          # User preferences (example)
└── README.md                    # This file
```

## How It Works

### 1. Knowledge Source Integration
- The `crew.py` file automatically loads the knowledge directory as a `Knowledge` source
- This provides RAG capabilities to all agents at both crew and agent levels
- Agents can access company information through semantic search

### 2. RAG Tools Available
- **DirectorySearchTool**: Semantic search across all knowledge base files
- **FileReadTool**: Read specific files in detail when needed

### 3. Agent Access
All agents have access to:
- Company knowledge base through `knowledge` parameter
- RAG search tools through `tools` parameter
- Automatic context injection when generating recommendations

## Adding Company Knowledge

### For Deployment in Your Company

1. **Replace Example Files**: Update the example files with your actual company information:
   - `company_overview.md` - Your company profile
   - `company_strategy.md` - Your strategic initiatives
   - `company_capabilities.md` - Your capabilities and resources

2. **Add Additional Documents**: You can add any company documents:
   - Financial reports
   - Product documentation
   - Market research
   - Competitive analysis
   - Organizational charts
   - Process documentation
   - Policy documents
   - Historical project data

3. **Supported File Types**:
   - Markdown (`.md`)
   - Text files (`.txt`)
   - PDF (`.pdf`) - with PDFSearchTool
   - Word documents (`.docx`) - with DOCXSearchTool
   - JSON (`.json`) - with JSONSearchTool
   - CSV (`.csv`) - with CSVSearchTool

### Best Practices

1. **Organize by Topic**: Create subdirectories for different knowledge areas:
   ```
   knowledge/
   ├── strategy/
   ├── products/
   ├── financials/
   ├── operations/
   └── market_intelligence/
   ```

2. **Keep Documents Updated**: Regularly update knowledge base with latest information

3. **Use Clear Filenames**: Descriptive filenames help agents find relevant information

4. **Structure Content Well**: Use clear headings and sections in markdown files

5. **Include Metadata**: Add context about document purpose, date, and relevance

## How Agents Use Knowledge

### Automatic Context
- Agents automatically have company context available through the knowledge base
- No need to explicitly search unless looking for specific information

### Explicit Search
- Agents can use `DirectorySearchTool` to search for specific information
- Useful when agents need to find specific details or verify information

### Example Agent Behavior
When an agent needs company information:
1. **Automatic**: Knowledge base provides relevant context automatically
2. **Search**: Agent uses DirectorySearchTool if specific information is needed
3. **Read**: Agent uses FileReadTool to read specific documents in detail

## Updating Knowledge Base

### Adding New Documents
1. Add files to the `knowledge/` directory
2. Restart the crew (knowledge is loaded at initialization)
3. Agents will automatically have access to new documents

### Updating Existing Documents
1. Edit the markdown/text files directly
2. Restart the crew to reload knowledge
3. Changes are immediately available to agents

### Programmatic Updates
You can also update knowledge programmatically:
```python
# In crew.py __init__ method
knowledge_dir = "path/to/knowledge"
self.company_knowledge = Knowledge(source=knowledge_dir)
```

## Security Considerations

⚠️ **Important for Production Deployment:**

1. **Access Control**: Ensure knowledge base directory has appropriate file permissions
2. **Sensitive Information**: Be careful about including:
   - Financial data
   - Customer information
   - Proprietary strategies
   - Personal employee data

3. **Version Control**: Consider excluding sensitive knowledge from version control
4. **Encryption**: For sensitive deployments, consider encrypting knowledge base files

## Troubleshooting

### Agents Not Finding Information
- Check that files are in the `knowledge/` directory
- Verify file formats are supported
- Ensure crew is restarted after adding new files
- Check file permissions

### Performance Issues
- Large knowledge bases may slow down RAG searches
- Consider organizing into subdirectories
- Use specific search queries rather than broad searches

### Knowledge Not Loading
- Verify the path to knowledge directory is correct
- Check that `crewai_tools` package is installed
- Ensure knowledge directory exists and is readable

## Next Steps

1. **Customize**: Replace example files with your company information
2. **Expand**: Add more knowledge documents as needed
3. **Test**: Run the crew and verify agents use company knowledge correctly
4. **Iterate**: Continuously improve knowledge base based on agent performance




