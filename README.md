# Government Services Documentation Site

A Hugo-based documentation site with the Beautiful Hugo theme, featuring a comprehensive guide to various government services and online applications.

## Features

- **Categorized Navigation**: Left navigation menu organized by service categories
- **Responsive Design**: Mobile-friendly Beautiful Hugo theme
- **Comprehensive Content**: Step-by-step guides for government services
- **Search-Friendly**: SEO-optimized structure

## Service Categories

### 📜 Certificates
- Download Income Certificate Online
- Download Caste Certificate Online
- Apply for OBC Certificate Online
- Download Birth and Death Certificate Online
- Download Death Certificate Online
- Apply for Marriage Certificate Online
- Apply for First-Class Graduate Certificate

### 🍚 Ration Card Services
- Apply for New Ration Card Online
- Verify Mobile Number on Ration Card
- Remove Family Member from Ration Card
- Reactivate Deleted Ration Card
- Download Ration Card Application
- Download Ration Card Online

### 💳 PAN Card Services
- Retrieve Lost or Forgotten PAN Number
- Get e-PAN
- Reprint or Update PAN Card

### 🏛️ Welfare Schemes
- Apply for Pension Online

### 💻 Digital Services
- Download and Use DigiLocker

### 📋 Government Records / Corrections
- Correct Date of Birth in School

### 🛂 Passport Services
- Apply for a Passport

## Prerequisites

- Hugo (v0.92.2 or later)
- Git

## Installation

1. Clone or extract the project files
2. Navigate to the project directory:
   ```bash
   cd document_site
   ```

3. Install Hugo (if not already installed):
   ```bash
   # Ubuntu/Debian
   sudo apt-get update
   sudo apt-get install hugo
   
   # macOS
   brew install hugo
   
   # Windows
   # Download from https://github.com/gohugoio/hugo/releases
   ```

## Development

1. Start the development server:
   ```bash
   hugo server --bind 0.0.0.0 --port 1313
   ```

2. Open your browser and navigate to `http://localhost:1313`

3. The site will automatically reload when you make changes to content files.

## Building for Production

1. Build the static site:
   ```bash
   hugo --minify
   ```

2. The generated static files will be in the `public/` directory.

## Deployment Options

### Static Hosting (Recommended)
- **Netlify**: Connect your Git repository and deploy automatically
- **Vercel**: Import your project and deploy with zero configuration
- **GitHub Pages**: Use GitHub Actions to build and deploy
- **AWS S3 + CloudFront**: Upload the `public/` folder to S3

### Traditional Web Hosting
- Upload the contents of the `public/` folder to your web server's document root

## Project Structure

```
document_site/
├── config.toml              # Hugo configuration
├── content/                 # Content files
│   ├── _index.md           # Homepage content
│   ├── certificates/       # Certificate-related guides
│   ├── ration-card-services/
│   ├── pan-card-services/
│   ├── welfare-schemes/
│   ├── digital-services/
│   ├── government-records-corrections/
│   └── passport-services/
├── themes/
│   └── beautifulhugo/      # Beautiful Hugo theme
├── static/                 # Static assets
├── public/                 # Generated site (after build)
└── README.md              # This file
```

## Content Management

### Adding New Content

1. Create a new markdown file in the appropriate category folder:
   ```bash
   hugo new certificates/new-certificate-guide.md
   ```

2. Edit the front matter and content:
   ```yaml
   ---
   title: "New Certificate Guide"
   date: 2025-06-30T00:00:00Z
   draft: false
   type: "post"
   ---
   
   # Your content here
   ```

3. Update the navigation menu in `config.toml` if needed.

### Content Guidelines

- Use proper Hugo front matter format
- Include descriptive titles and dates
- Organize content by logical categories
- Use markdown formatting for better readability

## Customization

### Theme Customization
- Modify `config.toml` for site-wide settings
- Override theme templates by copying them to `layouts/`
- Add custom CSS in `static/css/`

### Navigation Menu
- Edit the `[menu]` section in `config.toml`
- Use hierarchical structure with parent-child relationships

## Troubleshooting

### Common Issues

1. **Hugo version compatibility**: Ensure you're using Hugo v0.92.2 or later
2. **Theme errors**: The Beautiful Hugo theme has been patched for compatibility
3. **Content not showing**: Check front matter format and file naming conventions

### Template Fixes Applied

The following template fixes have been applied for Hugo compatibility:
- `themes/beautifulhugo/layouts/partials/head.html`: Fixed `hugo.IsServer` to `.Site.IsServer`
- `themes/beautifulhugo/layouts/partials/nav.html`: Fixed `hugo.IsMultilingual` to `.Site.IsMultiLingual`
- `themes/beautifulhugo/layouts/partials/footer.html`: Fixed `.Site.Lastmod` to `now`

## Support

For issues related to:
- **Hugo**: Check the [Hugo documentation](https://gohugo.io/documentation/)
- **Beautiful Hugo theme**: Visit the [theme repository](https://github.com/halogenica/beautifulhugo)
- **Content**: Refer to the original government service portals

## License

This project uses the Beautiful Hugo theme, which is licensed under the MIT License. Content is provided for educational and informational purposes.

