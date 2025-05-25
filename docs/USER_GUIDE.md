# User Guide

Welcome to the Survey Data Filtering Dashboard - a powerful tool for analyzing and visualizing survey data.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Interface Overview](#interface-overview)
3. [Data Loading](#data-loading)
4. [Filtering Data](#filtering-data)
5. [Visualizations](#visualizations)
6. [Exporting Results](#exporting-results)
7. [Tips and Best Practices](#tips-and-best-practices)
8. [Troubleshooting](#troubleshooting)

## Getting Started

### System Requirements

- Python 3.8 or higher
- Modern web browser (Chrome, Firefox, Safari, Edge)
- Minimum 4GB RAM recommended
- CSV or Excel files with survey data

### Installation

```bash
# Clone the repository
git clone https://github.com/AlanSteinbarth/Filtrowanie-danych-z-ankiety.git
cd Filtrowanie-danych-z-ankiety

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

### First Launch

1. Open your web browser to `http://localhost:8501`
2. The application will load with sample survey data
3. Explore the interface using the sidebar controls

## Interface Overview

### Main Components

- **Sidebar**: Contains all filtering controls and options
- **Main Content Area**: Displays filtered data, charts, and metrics
- **Header**: Shows application title and key statistics
- **Footer**: Contains export options and additional tools

### Navigation

- Use the sidebar to apply filters
- Results update automatically as you change filters
- Charts and metrics refresh in real-time
- Download options are available in the main content area

## Data Loading

### Supported Formats

- CSV files (`.csv`)
- Excel files (`.xlsx`, `.xls`)
- TSV files (`.tsv`)

### Data Requirements

Your data file should contain:
- Headers in the first row
- Consistent data types in each column
- No completely empty rows
- UTF-8 encoding (recommended)

### Loading Your Data

1. Use the file uploader in the sidebar
2. Select your data file
3. Wait for processing confirmation
4. Review the data preview

### Data Validation

The application automatically validates:
- File format compatibility
- Column structure
- Data type consistency
- File size limits (max 200MB)

## Filtering Data

### Available Filter Types

#### Text Filters
- **Contains**: Find rows where text contains specific words
- **Exact Match**: Find exact text matches
- **Starts With**: Find text beginning with specific characters
- **Ends With**: Find text ending with specific characters

#### Numeric Filters
- **Range**: Filter by minimum and maximum values
- **Greater Than**: Values above a threshold
- **Less Than**: Values below a threshold
- **Equal To**: Exact numeric matches

#### Date Filters
- **Date Range**: Filter between two dates
- **Before Date**: Earlier than specified date
- **After Date**: Later than specified date
- **Specific Date**: Exact date matches

#### Categorical Filters
- **Multiple Selection**: Choose multiple categories
- **Single Selection**: Choose one category
- **Exclude**: Remove specific categories

### Applying Filters

1. **Select Columns**: Choose which columns to filter
2. **Set Criteria**: Define your filter conditions
3. **Apply**: Filters are applied automatically
4. **Clear**: Use the reset button to clear all filters

### Advanced Filtering

#### Combining Filters
- Filters work together using AND logic
- All conditions must be met for a row to appear
- Use multiple filters for precise data selection

#### Filter Persistence
- Filters remain active while you explore
- Clear individual filters or reset all
- Filter settings are not saved between sessions

## Visualizations

### Chart Types

#### Bar Charts
- Best for categorical data comparison
- Shows frequency distributions
- Interactive hover information

#### Line Charts
- Ideal for time series data
- Shows trends over time
- Multiple series support

#### Pie Charts
- Perfect for proportion visualization
- Shows percentage breakdowns
- Limited to top categories

#### Scatter Plots
- Great for correlation analysis
- Shows relationships between variables
- Supports trend lines

#### Histograms
- Excellent for distribution analysis
- Shows data frequency
- Customizable bin sizes

### Customizing Charts

1. **Chart Type**: Select from available options
2. **Columns**: Choose X and Y axes
3. **Grouping**: Add color coding by category
4. **Aggregation**: Sum, count, average, etc.

### Interactive Features

- **Zoom**: Click and drag to zoom in
- **Pan**: Hold and drag to move around
- **Hover**: See detailed information
- **Download**: Save charts as images

## Exporting Results

### Export Formats

#### Data Export
- **CSV**: Comma-separated values
- **Excel**: Microsoft Excel format
- **JSON**: JavaScript Object Notation

#### Chart Export
- **PNG**: High-quality images
- **SVG**: Scalable vector graphics
- **PDF**: Portable document format
- **HTML**: Interactive web format

### Export Process

1. **Filter Data**: Apply desired filters
2. **Select Format**: Choose export format
3. **Configure Options**: Set filename and options
4. **Download**: Click download button

### Export Options

- **Include Headers**: Add column names
- **Date Format**: Customize date display
- **Number Format**: Control decimal places
- **Encoding**: Choose character encoding

## Tips and Best Practices

### Data Preparation

- **Clean Data**: Remove empty rows and columns
- **Consistent Formats**: Use standard date and number formats
- **Meaningful Headers**: Use descriptive column names
- **Reasonable Size**: Files under 50MB load faster

### Efficient Filtering

- **Start Broad**: Begin with loose filters, then narrow down
- **Use Combinations**: Combine multiple filters for precision
- **Check Results**: Verify filter results make sense
- **Document Process**: Note successful filter combinations

### Performance Optimization

- **Smaller Datasets**: Filter to reduce data size
- **Simple Charts**: Use appropriate chart types
- **Clear Filters**: Reset when switching analysis focus
- **Close Unused Tabs**: Free up browser memory

### Visualization Best Practices

- **Choose Appropriate Charts**: Match chart type to data type
- **Limit Categories**: Use top 10-15 categories for clarity
- **Meaningful Colors**: Use consistent color schemes
- **Clear Labels**: Ensure axes and legends are readable

## Troubleshooting

### Common Issues

#### File Upload Problems

**Error**: "File format not supported"
- **Solution**: Ensure file is CSV or Excel format
- **Check**: File extension matches content

**Error**: "File too large"
- **Solution**: Reduce file size or split data
- **Limit**: Maximum 200MB file size

**Error**: "Encoding error"
- **Solution**: Save file with UTF-8 encoding
- **Alternative**: Try different text editor

#### Filtering Issues

**Problem**: No results after filtering
- **Check**: Filter criteria aren't too restrictive
- **Solution**: Broaden filter conditions
- **Verify**: Data actually contains expected values

**Problem**: Slow filtering performance
- **Cause**: Large dataset or complex filters
- **Solution**: Reduce data size or simplify filters
- **Tip**: Apply most selective filters first

#### Visualization Problems

**Issue**: Chart not displaying
- **Check**: Data exists after filtering
- **Verify**: Appropriate columns selected
- **Solution**: Choose different chart type

**Issue**: Chart looks wrong
- **Check**: Correct aggregation method
- **Verify**: Proper grouping columns
- **Solution**: Adjust chart configuration

### Getting Help

#### Self-Help Resources

1. **Documentation**: Check this user guide
2. **Examples**: Try with sample data
3. **FAQ**: Review frequently asked questions
4. **Error Messages**: Read error details carefully

#### Community Support

1. **GitHub Issues**: Report bugs and request features
2. **Discussions**: Ask questions and share tips
3. **Contributing**: Help improve the application

#### Reporting Issues

When reporting problems, include:
- **Operating System**: Windows, macOS, Linux
- **Browser**: Chrome, Firefox, Safari, etc.
- **Error Message**: Full text of any errors
- **Steps**: What you were doing when error occurred
- **Data Sample**: Small sample of problematic data (if possible)

### Contact Information

- **Developer**: Alan Steinbarth
- **Email**: alan.steinbarth@gmail.com
- **GitHub**: https://github.com/AlanSteinbarth
- **Project**: https://github.com/AlanSteinbarth/Filtrowanie-danych-z-ankiety

---

*Last updated: May 26, 2025*
*Version: 2.0.0*
