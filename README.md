# Sadda Hussain Butt - Portfolio Website

A modern, responsive personal portfolio website showcasing professional experience, projects, skills, and education. Built with clean HTML, Tailwind CSS, and vanilla JavaScript.

## 🌐 Live Website

Visit: [saddahussain.github.io](https://saddahussain.github.io)

## ✨ Features

- **Responsive Design** - Works seamlessly on desktop, tablet, and mobile devices
- **Modern UI** - Clean, professional dark theme with accent colors
- **Sticky Navigation** - Quick access to all sections from anywhere
- **Mobile Menu** - Hamburger menu for mobile devices
- **Performance Optimized** - Fast loading with minimal dependencies
- **SEO Friendly** - Meta tags and structured content
- **Analytics Ready** - Google Tag Manager integration for tracking

## 🏗️ Project Structure

```
saddahussain.github.io/
├── README.md                          # Project documentation
├── index.html                         # Home page
├── about.html                         # About section
├── experience.html                    # Work experience
├── projects.html                      # Portfolio projects
├── skills.html                        # Technical skills
├── education.html                     # Education & certifications
├── contact.html                       # Contact information
├── CNAME                              # GitHub Pages custom domain
├── css/
│   └── styles.css                     # Custom CSS styles
├── js/
│   └── script.js                      # JavaScript functionality
└── assets/
    ├── picture.png                    # Profile picture
    └── Sadda_Hussain_Android_8Y.pdf   # CV/Resume download
```

## 📄 Pages Overview

| Page | Description |
|------|-------------|
| **Home** (`index.html`) | Hero section with introduction and call-to-action |
| **About** (`about.html`) | Professional background and expertise overview |
| **Experience** (`experience.html`) | Work history and key achievements |
| **Projects** (`projects.html`) | Showcase of notable projects and applications |
| **Skills** (`skills.html`) | Technical skills and competencies |
| **Education** (`education.html`) | Academic background and certifications |
| **Contact** (`contact.html`) | Contact information and social links |

## 🛠️ Tech Stack

- **Frontend Framework**: HTML5 + Vanilla JavaScript
- **Styling**: 
  - Tailwind CSS (via CDN)
  - Custom CSS for enhanced styling
- **Icons**: Font Awesome 6.5.1
- **Analytics**: Google Tag Manager
- **Hosting**: GitHub Pages
- **Domain**: Custom domain via CNAME

## 🚀 Getting Started

### Prerequisites
- A web browser (no server required)
- A text editor (for modifications)
- Git (for version control)

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/saddahussain/saddahussain.github.io.git
   cd saddahussain.github.io
   ```

2. **Open in browser**
   - Option 1: Double-click `index.html`
   - Option 2: Use a local server (recommended)
     ```bash
     # Using Python 3
     python -m http.server 8000
     # Then visit http://localhost:8000
     ```

### Deployment

This site is configured for **GitHub Pages**:
1. Push changes to the `main` branch
2. GitHub automatically deploys the site
3. Site is available at your GitHub Pages URL

## 🎨 Customization

### Colors & Branding
Edit `css/styles.css` to change:
- Primary color: `#f16522` (orange)
- Dark theme colors: `#1a1c24`, `#23252c`

### Content Updates
1. Edit the relevant `.html` file
2. Update text, links, and images
3. Commit and push changes

### Adding New Pages
1. Create a new `.html` file with the same navbar/footer structure
2. Add link in navbar
3. Copy the structure from existing pages

## 📱 Responsive Breakpoints

- **Mobile**: < 768px (Tailwind `sm`)
- **Tablet**: 768px - 1024px (Tailwind `md`)
- **Desktop**: > 1024px (Tailwind `lg`)

## 🔍 SEO Features

- Meta descriptions on all pages
- Proper heading hierarchy (h1-h6)
- Semantic HTML structure
- Google Tag Manager integration for analytics
- Optimized page titles

## 📊 Analytics

Google Tag Manager is configured with ID: `GTM-TJLB3D5M`

To modify:
1. Update the GTM ID in the `<head>` section of all `.html` files
2. Configure conversion tracking and events in GTM dashboard

## 🔗 Social Links

- LinkedIn: [saddahussain](https://www.linkedin.com/in/saddahussain)
- CV Download: Available in navbar

## ⚡ Performance Tips

- Tailwind CSS loaded via CDN (consider building locally for production)
- Minimal JavaScript for faster load times
- Optimized images in assets folder
- Sticky navbar doesn't block content on mobile

## 🐛 Known Issues / Future Improvements

- [ ] Dark mode toggle option
- [ ] Blog section
- [ ] Projects filter/search functionality
- [ ] Email contact form backend
- [ ] Animation enhancements

## 💡 Tips for Maintenance

1. **Update CV**: Replace `assets/Sadda_Hussain_Android_8Y.pdf`
2. **Change Profile Picture**: Update `assets/picture.png`
3. **Add Projects**: Edit `projects.html` with new project cards
4. **Update Experience**: Modify `experience.html` with new roles
5. **Skills**: Update `skills.html` with current technologies

## 📝 Content Structure

Each page follows a consistent structure:
```html
<nav><!-- Responsive Navigation --></nav>
<section id="[section-name]"><!-- Main Content --></section>
<footer><!-- Footer --></footer>
```

## 🎯 Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## 📄 License

This portfolio website is personal and proprietary. Feel free to use it as inspiration for your own portfolio.

## 👤 About Sadda Hussain Butt

**Senior Android Developer** with 8+ years of experience building production-grade mobile applications. Expertise in:
- Kotlin & Jetpack Compose
- MVVM & Clean Architecture
- AI/LLM Integration (OpenAI GPT-4o, Groq LLaMA)
- Mobile App Security & Performance
- Team Leadership & Freelance Expertise

---

**Last Updated**: April 2026  
**Status**: Active & Maintained
