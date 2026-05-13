# Java Web Application

A nice Spring Boot web application that generates a `.war` file for deployment. with CICD

## Project Structure

```
java-web-app/
├── src/
│   ├── main/
│   │   ├── java/com/example/webapp/
│   │   │   ├── Application.java          # Main Spring Boot Application
│   │   │   └── controller/
│   │   │       └── HomeController.java   # Web Controllers
│   │   └── resources/
│   │       ├── templates/                # Thymeleaf HTML Templates
│   │       ├── static/
│   │       │   ├── css/style.css         # Styling
│   │       │   └── js/script.js          # JavaScript
│   │       └── application.properties    # Configuration
│   └── test/
│       └── java/com/example/webapp/
├── pom.xml                               # Maven Configuration
├── .gitignore                           # Git Ignore Rules
└── README.md                            # Documentation
```

## Technology Stack

- **Backend**: Java 11+, Spring Boot 3.1.5, Spring Web MVC
- **Frontend**: Thymeleaf, HTML5, CSS3, JavaScript
- **Build**: Apache Maven
- **Packaging**: WAR (Web Application Archive)
- **Version Control**: Git

## Building the Application

### Prerequisites
- Java 11 or higher
- Apache Maven 3.6+

### Build WAR File

```bash
mvn clean package
```

The WAR file will be created at: `target/webapp-1.0.0.war`

## Running the Application

### Development Mode (Spring Boot embedded Tomcat)

```bash
mvn spring-boot:run
```

The application will be available at: `http://localhost:8080`

### Production Mode (Using WAR file)

Deploy the `target/webapp-1.0.0.war` file to any Java application server:
- Apache Tomcat
- Jetty
- WildFly
- GlassFish

## Features

- 🏠 **Home Page** - Welcome page with feature cards
- 📝 **Message Board** - Add and display messages
- ℹ️ **About Page** - Project information and technology stack
- 🎨 **Responsive Design** - Mobile-friendly interface
- ⚡ **Modern UI** - Gradient backgrounds and smooth animations
- 🔧 **Spring Boot Configuration** - Production-ready setup

## Pages

1. **Home** (`/`) - Landing page with message board
2. **About** (`/about`) - Project information
3. **Health** (`/api/health`) - Application health status

## Maven Commands

```bash
# Clean build
mvn clean

# Compile
mvn compile

# Run tests
mvn test

# Build and package
mvn package

# Run with Spring Boot
mvn spring-boot:run

# Show dependencies
mvn dependency:tree
```

## Configuration

Edit `src/main/resources/application.properties` to configure:
- Server port
- Application context path
- Thymeleaf settings
- Logging levels

## Styling

The application uses a modern gradient color scheme:
- Primary Gradient: Purple (#667eea) to Pink (#764ba2)
- Clean and responsive design
- Mobile-optimized CSS

## Contributing

This is a sample application for learning purposes.

## License

MIT License

---

**Built with ❤️ using Spring Boot and Maven**
